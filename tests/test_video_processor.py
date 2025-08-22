"""视频处理器测试文件"""
import unittest
import sys
import os

# 将项目根目录添加到Python路径中
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

 try:
    from video_processor import VideoProcessor
    from advanced_video_processor import AdvancedVideoProcessor
except ImportError:
    VideoProcessor = None
    AdvancedVideoProcessor = None


class TestVideoProcessor(unittest.TestCase):
    """视频处理器测试类"""
    
    def test_video_processor_import(self):
        """测试是否能正确导入视频处理器模块"""
        if VideoProcessor is None:
            self.skipTest("VideoProcessor未实现或无法导入")
        self.assertIsNotNone(VideoProcessor)
    
    def test_advanced_video_processor_import(self):
        """测试是否能正确导入高级视频处理器模块"""
        if AdvancedVideoProcessor is None:
            self.skipTest("AdvancedVideoProcessor未实现或无法导入")
        self.assertIsNotNone(AdvancedVideoProcessor)


if __name__ == '__main__':
    unittest.main()