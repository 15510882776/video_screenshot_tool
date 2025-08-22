import os
import sys
import argparse
import logging
from pathlib import Path
from typing import List

from video_processor import VideoProcessor
from advanced_video_processor import AdvancedVideoProcessor
from config import OCRConfig, VideoConfig

# 设置OCR路径
if OCRConfig.TESSERACT_CMD and os.path.exists(OCRConfig.TESSERACT_CMD):
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = OCRConfig.TESSERACT_CMD

def process_single_video(video_path: str, interval: float = VideoConfig.DEFAULT_INTERVAL, 
                         processor_type: str = "basic", method: str = "combined",
                         similarity_threshold: float = 0.95, hash_threshold: int = 10) -> bool:
    """
    处理单个视频文件
    :param video_path: 视频文件路径
    :param interval: 处理帧的时间间隔（秒）
    :return: 处理是否成功
    """
    if not os.path.exists(video_path):
        print(f"错误: 视频文件不存在: {video_path}")
        return False
        
    try:
        if processor_type == "basic":
            processor = VideoProcessor(video_path)
            screenshots = processor.process_video(interval)
        else:  # advanced
            processor = AdvancedVideoProcessor(video_path)
            # 使用支持自定义阈值的新方法
            screenshots = processor.extract_frames_with_custom_thresholds(interval, method, similarity_threshold, hash_threshold)
            
        print(f"处理完成: {video_path}")
        print(f"生成截图数量: {len(screenshots)}")
        print(f"截图保存位置: {processor.output_dir}")
        return True
    except Exception as e:
        print(f"处理视频时出错: {e}")
        return False

def process_multiple_videos(video_paths: List[str], interval: float = VideoConfig.DEFAULT_INTERVAL, 
                            processor_type: str = "basic", method: str = "combined") -> None:
    """
    处理多个视频文件
    :param video_paths: 视频文件路径列表
    :param interval: 处理帧的时间间隔（秒）
    """
    success_count = 0
    for video_path in video_paths:
        if process_single_video(video_path, interval, processor_type, method):
            success_count += 1
            
    print(f"\n批量处理完成: {success_count}/{len(video_paths)} 个视频处理成功")

def main():
    parser = argparse.ArgumentParser(
        description='自动提取视频中变化的截图',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\使用示例:
  python main.py video.mp4
  python main.py video1.mp4 video2.mp4
  python main.py video.mp4 --interval 0.5
  python main.py video.mp4 --processor advanced --method text
  python main.py *.mp4
        """
    )
    parser.add_argument('videos', nargs='*', help='视频文件路径（支持多个文件）')
    parser.add_argument('--interval', type=float, default=VideoConfig.DEFAULT_INTERVAL, 
                        help=f'处理帧的时间间隔（秒），默认为{VideoConfig.DEFAULT_INTERVAL}')
    parser.add_argument('--processor', choices=['basic', 'advanced'], default='basic',
                        help='处理器类型: basic(基础文字检测), advanced(高级综合检测), 默认为basic')
    parser.add_argument('--method', choices=['text', 'image', 'combined'], default='combined',
                        help='高级处理器的检测方法: text(文字变化), image(图像变化), combined(结合), 默认为combined')
    parser.add_argument('--version', action='version', version='视频变化截图工具 1.0')
    parser.add_argument('--gui', action='store_true', help='启动图形界面')
    
    args = parser.parse_args()
    
    # 启动图形界面
    if args.gui:
        print("正在启动图形界面...")
        try:
            from gui import main as gui_main
            print("成功导入GUI模块，正在启动...")
            gui_main()
            print("GUI界面启动完成")
        except ImportError as e:
            print(f"无法启动图形界面: {e}")
            print("请确保已安装tkinter库")
        except Exception as e:
            print(f"启动图形界面时发生错误: {e}")
            import traceback
            traceback.print_exc()
        return
    
    # 设置OCR路径
    if OCRConfig.TESSERACT_CMD and os.path.exists(OCRConfig.TESSERACT_CMD):
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = OCRConfig.TESSERACT_CMD
    
    # 检查是否提供了视频文件
    if not args.videos:
        parser.print_help()
        return
    
    # 设置OCR路径
    if OCRConfig.TESSERACT_CMD and os.path.exists(OCRConfig.TESSERACT_CMD):
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = OCRConfig.TESSERACT_CMD
    
    # 处理视频文件
    if len(args.videos) == 1:
        process_single_video(args.videos[0], args.interval, args.processor, args.method)
    else:
        process_multiple_videos(args.videos, args.interval, args.processor, args.method)

if __name__ == "__main__":
    main()