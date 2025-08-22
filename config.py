import os
from pathlib import Path

# OCR配置
class OCRConfig:
    # Tesseract OCR路径（Windows下需要配置）
    # TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    TESSERACT_CMD = r"d:\video_screenshot_tool\tesseract.exe"  # 使用项目目录中的tesseract
    
    # OCR语言
    LANGUAGES = 'chi_sim+eng'  # 中文简体+英文
    
# 视频处理配置
class VideoConfig:
    # 默认帧处理间隔（秒）
    DEFAULT_INTERVAL = 1.0
    
    # 视频编码格式
    VIDEO_CODECS = ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv']
    
# 文件路径配置
class PathConfig:
    # 临时文件目录
    TEMP_DIR = os.path.join(Path.home(), '.video_processor', 'temp')
    
    # 日志目录
    LOG_DIR = os.path.join(Path.home(), '.video_processor', 'logs')
    
# 创建必要的目录
os.makedirs(PathConfig.TEMP_DIR, exist_ok=True)
os.makedirs(PathConfig.LOG_DIR, exist_ok=True)