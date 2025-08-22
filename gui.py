import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import os
import sys
from pathlib import Path

from main import process_single_video
from config import OCRConfig


class VideoProcessorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("视频变化截图工具")
        self.root.geometry("600x500")
        
        # 设置窗口图标（如果有的话）
        try:
            # 检查图标文件是否存在
            if os.path.exists('icon.ico'):
                self.root.iconbitmap('icon.ico')
            elif os.path.exists('icon.svg'):
                # 如果有SVG图标，暂时不设置（tkinter不直接支持SVG）
                pass
        except Exception as e:
            # 忽略图标加载错误
            print(f"警告: 无法加载窗口图标: {e}")
        
        # 存储选中的文件
        self.selected_files = []
        
        # 创建界面
        self.create_widgets()
        
    def create_widgets(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # 视频文件选择
        ttk.Label(main_frame, text="视频文件:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        file_frame = ttk.Frame(main_frame)
        file_frame.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        file_frame.columnconfigure(0, weight=1)
        
        self.file_entry = ttk.Entry(file_frame, width=50)
        self.file_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        ttk.Button(file_frame, text="浏览...", command=self.browse_files).grid(row=0, column=1)
        
        # 文件列表
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        ttk.Label(list_frame, text="选中的文件:").grid(row=0, column=0, sticky=tk.W)
        
        # 创建列表框和滚动条
        listbox_frame = ttk.Frame(list_frame)
        listbox_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        listbox_frame.columnconfigure(0, weight=1)
        listbox_frame.rowconfigure(0, weight=1)
        
        self.file_listbox = tk.Listbox(listbox_frame, height=6)
        self.file_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.file_listbox.configure(yscrollcommand=scrollbar.set)
        
        # 删除按钮
        ttk.Button(list_frame, text="删除选中", command=self.remove_selected).grid(row=2, column=0, sticky=tk.W)
        ttk.Button(list_frame, text="清空列表", command=self.clear_list).grid(row=2, column=1, sticky=tk.W)
        
        # 分隔线
        ttk.Separator(main_frame, orient='horizontal').grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # 处理器类型选择
        ttk.Label(main_frame, text="处理器类型:").grid(row=3, column=0, sticky=tk.W, pady=5)
        
        self.processor_var = tk.StringVar(value="basic")
        processor_frame = ttk.Frame(main_frame)
        processor_frame.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=5)
        
        ttk.Radiobutton(processor_frame, text="基础（仅文字检测）", variable=self.processor_var, 
                       value="basic").grid(row=0, column=0, sticky=tk.W)
        ttk.Radiobutton(processor_frame, text="高级（综合检测）", variable=self.processor_var, 
                       value="advanced").grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        # 高级处理器选项
        self.method_frame = ttk.Frame(main_frame)
        self.method_frame.grid(row=4, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(self.method_frame, text="检测方法:").grid(row=0, column=0, sticky=tk.W)
        
        self.method_var = tk.StringVar(value="combined")
        method_subframe = ttk.Frame(self.method_frame)
        method_subframe.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        ttk.Radiobutton(method_subframe, text="仅文字", variable=self.method_var, 
                       value="text").grid(row=0, column=0, sticky=tk.W)
        ttk.Radiobutton(method_subframe, text="仅画面", variable=self.method_var, 
                       value="image").grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        ttk.Radiobutton(method_subframe, text="综合", variable=self.method_var, 
                       value="combined").grid(row=0, column=2, sticky=tk.W, padx=(10, 0))
        
        # 初始隐藏高级选项
        self.method_frame.grid_remove()
        
        # 绑定处理器类型变化事件
        self.processor_var.trace('w', self.on_processor_change)
        
        # 帧间隔设置
        ttk.Label(main_frame, text="帧间隔（秒）:").grid(row=5, column=0, sticky=tk.W, pady=5)
        
        self.interval_var = tk.StringVar(value="1.0")
        ttk.Entry(main_frame, textvariable=self.interval_var, width=10).grid(row=5, column=1, sticky=tk.W, pady=5)
        
        # 图像相似度阈值设置
        ttk.Label(main_frame, text="图像相似度阈值:").grid(row=6, column=0, sticky=tk.W, pady=5)
        
        self.similarity_threshold_var = tk.StringVar(value="0.95")
        ttk.Entry(main_frame, textvariable=self.similarity_threshold_var, width=10).grid(row=6, column=1, sticky=tk.W, pady=5)
        
        # 哈希差异阈值设置
        ttk.Label(main_frame, text="哈希差异阈值:").grid(row=7, column=0, sticky=tk.W, pady=5)
        
        self.hash_threshold_var = tk.StringVar(value="10")
        ttk.Entry(main_frame, textvariable=self.hash_threshold_var, width=10).grid(row=7, column=1, sticky=tk.W, pady=5)
        
        # 分隔线
        ttk.Separator(main_frame, orient='horizontal').grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # 进度条
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=9, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # 状态标签
        self.status_var = tk.StringVar(value="就绪")
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var)
        self.status_label.grid(row=10, column=0, columnspan=3, sticky=tk.W, pady=5)
        
        # 开始处理按钮
        self.start_button = ttk.Button(main_frame, text="开始处理", command=self.start_processing)
        self.start_button.grid(row=11, column=0, columnspan=3, pady=10)
        
        # 绑定关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_processor_change(self, *args):
        """当处理器类型改变时的回调函数"""
        if self.processor_var.get() == "advanced":
            self.method_frame.grid()
        else:
            self.method_frame.grid_remove()
            
    def browse_files(self):
        """浏览并选择视频文件"""
        files = filedialog.askopenfilenames(
            title="选择视频文件",
            filetypes=[
                ("视频文件", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv"),
                ("所有文件", "*.*")
            ]
        )
        
        if files:
            for file in files:
                if file not in self.selected_files:
                    self.selected_files.append(file)
                    self.file_listbox.insert(tk.END, os.path.basename(file))
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, "; ".join([os.path.basename(f) for f in self.selected_files]))
            
    def remove_selected(self):
        """删除选中的文件"""
        selection = self.file_listbox.curselection()
        if selection:
            index = selection[0]
            self.file_listbox.delete(index)
            del self.selected_files[index]
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, "; ".join([os.path.basename(f) for f in self.selected_files]))
        else:
            messagebox.showwarning("警告", "请先选择要删除的文件")
            
    def clear_list(self):
        """清空文件列表"""
        self.file_listbox.delete(0, tk.END)
        self.selected_files.clear()
        self.file_entry.delete(0, tk.END)
        
    def validate_inputs(self):
        """验证用户输入"""
        if not self.selected_files:
            messagebox.showerror("错误", "请至少选择一个视频文件")
            return False
            
        try:
            interval = float(self.interval_var.get())
            if interval <= 0:
                raise ValueError("间隔必须大于0")
        except ValueError as e:
            messagebox.showerror("错误", f"帧间隔设置无效: {e}")
            return False
            
        return True
        
    def start_processing(self):
        """开始处理视频文件"""
        if not self.validate_inputs():
            return
            
        # 禁用开始按钮，显示进度条
        self.start_button.config(state=tk.DISABLED)
        self.progress.start()
        self.status_var.set("正在处理...")
        
        # 在新线程中处理文件，避免界面冻结
        threading.Thread(target=self.process_files, daemon=True).start()
        
    def process_files(self):
        """在后台线程中处理文件"""
        try:
            interval = float(self.interval_var.get())
            processor_type = self.processor_var.get()
            method = self.method_var.get() if processor_type == "advanced" else "combined"
            
            # 获取阈值参数
            similarity_threshold = float(self.similarity_threshold_var.get())
            hash_threshold = int(self.hash_threshold_var.get())
            
            success_count = 0
            total_files = len(self.selected_files)
            
            for i, file_path in enumerate(self.selected_files):
                self.root.after(0, self.status_var.set, f"正在处理 ({i+1}/{total_files}): {os.path.basename(file_path)}")
                
                if process_single_video(file_path, interval, processor_type, method, similarity_threshold, hash_threshold):
                    success_count += 1
                    
            # 处理完成
            self.root.after(0, self.on_processing_complete, success_count, total_files)
            
        except Exception as e:
            self.root.after(0, self.on_processing_error, str(e))
            
    def on_processing_complete(self, success_count, total_files):
        """处理完成的回调函数"""
        self.progress.stop()
        self.start_button.config(state=tk.NORMAL)
        self.status_var.set(f"处理完成: {success_count}/{total_files} 个文件处理成功")
        
        messagebox.showinfo(
            "处理完成", 
            f"批量处理完成:\n成功处理: {success_count}/{total_files} 个文件"
        )
        
    def on_processing_error(self, error_message):
        """处理出错的回调函数"""
        self.progress.stop()
        self.start_button.config(state=tk.NORMAL)
        self.status_var.set("处理出错")
        
        messagebox.showerror("处理出错", f"处理过程中发生错误:\n{error_message}")
        
    def on_closing(self):
        """窗口关闭事件"""
        if self.progress.instate(['active']):
            if messagebox.askokcancel("确认退出", "正在处理文件，确定要退出吗？"):
                self.root.destroy()
        else:
            self.root.destroy()


def main():
    print("GUI main函数开始执行...")
    # 设置OCR路径
    if OCRConfig.TESSERACT_CMD and os.path.exists(OCRConfig.TESSERACT_CMD):
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = OCRConfig.TESSERACT_CMD
        print("OCR路径设置完成")
    
    print("正在创建Tk根窗口...")
    root = tk.Tk()
    print("Tk根窗口创建完成")
    app = VideoProcessorGUI(root)
    print("GUI应用创建完成，正在启动主循环...")
    root.mainloop()
    print("GUI主循环结束")


if __name__ == "__main__":
    main()