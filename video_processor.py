import cv2
import pytesseract
import numpy as np
from PIL import Image
import os
import hashlib
import time
import logging
from pathlib import Path
from typing import List, Tuple, Optional

# 设置OCR路径
try:
    from config import OCRConfig
    if OCRConfig.TESSERACT_CMD and os.path.exists(OCRConfig.TESSERACT_CMD):
        pytesseract.pytesseract.tesseract_cmd = OCRConfig.TESSERACT_CMD
except ImportError:
    pass  # 如果config模块不可用，则跳过

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VideoProcessor:
    def __init__(self, video_path: str, output_dir: Optional[str] = None):
        self.video_path = video_path
        self.video_name = Path(video_path).stem
        self.output_dir = output_dir or os.path.join(os.path.dirname(video_path), f"{self.video_name}_截图")
        self.previous_text = ""
        self.screenshot_count = 0
        
        # 创建输出目录
        os.makedirs(self.output_dir, exist_ok=True)
        
    def extract_frames_with_text_changes(self, interval: float = 1.0) -> List[str]:
        """
        提取视频中文字有变化的帧并保存截图
        :param interval: 处理帧的时间间隔（秒）
        :return: 截图文件路径列表
        """
        logger.info(f"开始处理视频: {self.video_path}")
        
        # 打开视频文件
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            logger.error(f"无法打开视频文件: {self.video_path}")
            return []
            
        fps = cap.get(cv2.CAP_PROP_FPS)
        # 确保frame_interval至少为1，避免除零错误
        frame_interval = max(1, int(fps * interval))  # 帧间隔
        frame_count = 0
        saved_screenshots = []
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # 按指定间隔处理帧
            if frame_count % frame_interval == 0:
                # 将BGR转换为RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(rgb_frame)
                
                # 提取文字
                current_text = self.extract_text_from_image(pil_image)
                
                # 检查文字是否发生变化
                if self.has_text_changed(current_text):
                    # 保存截图
                    screenshot_path = self.save_screenshot(frame, frame_count)
                    saved_screenshots.append(screenshot_path)
                    self.previous_text = current_text
                    logger.info(f"检测到文字变化，已保存截图: {screenshot_path}")
                    
            frame_count += 1
            
        cap.release()
        logger.info(f"处理完成，共保存 {len(saved_screenshots)} 张截图")
        return saved_screenshots
        
    def extract_text_from_image(self, image: Image.Image) -> str:
        """
        从图像中提取文字
        :param image: PIL图像对象
        :return: 提取的文字
        """
        try:
            # 使用pytesseract进行OCR识别
            text = pytesseract.image_to_string(image, lang='chi_sim+eng')
            return text.strip()
        except Exception as e:
            logger.error(f"OCR识别失败: {e}")
            return ""
            
    def has_text_changed(self, current_text: str) -> bool:
        """
        检查文字是否发生变化
        :param current_text: 当前帧提取的文字
        :return: 是否发生变化
        """
        # 如果是第一帧，认为有变化
        if not self.previous_text:
            return True
            
        # 比较文字内容（去除空白字符后）
        return current_text.strip() != self.previous_text.strip()
        
    def save_screenshot(self, frame: np.ndarray, frame_number: int) -> str:
        """
        保存截图
        :param frame: 视频帧
        :param frame_number: 帧编号
        :return: 截图文件路径
        """
        self.screenshot_count += 1
        filename = f"{self.video_name}_截图_{self.screenshot_count:03d}.png"
        screenshot_path = os.path.join(self.output_dir, filename)
        
        # 确保输出目录存在
        os.makedirs(self.output_dir, exist_ok=True)
        
        # 保存图像并检查是否成功
        # 使用PIL保存图像，因为它能正确处理中文路径
        try:
            # 将BGR转换为RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_frame)
            pil_image.save(screenshot_path, 'PNG')
            success = True
        except Exception as e:
            success = False
            logger.error(f"保存截图失败: {screenshot_path}, 错误: {e}")
        
        if not success:
            logger.error(f"保存截图失败: {screenshot_path}")
        return screenshot_path

    def process_video(self, interval: float = 1.0) -> List[str]:
        """
        处理视频并提取文字变化的截图
        :param interval: 处理帧的时间间隔（秒）
        :return: 截图文件路径列表
        """
        return self.extract_frames_with_text_changes(interval)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='自动提取视频中文字变化的截图')
    parser.add_argument('video_path', help='视频文件路径')
    parser.add_argument('--interval', type=float, default=1.0, help='处理帧的时间间隔（秒），默认为1.0')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.video_path):
        logger.error(f"视频文件不存在: {args.video_path}")
        return
        
    processor = VideoProcessor(args.video_path)
    screenshots = processor.process_video(args.interval)
    
    logger.info(f"处理完成，共生成 {len(screenshots)} 张截图，保存在: {processor.output_dir}")

if __name__ == "__main__":
    main()