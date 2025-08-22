"""测试配置文件"""
import unittest
import sys
import os

# 将项目根目录添加到Python路径中
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestConfig(unittest.TestCase):
    """测试配置类"""
    
    def test_imports(self):
        """测试是否能正确导入项目模块"""
        try:
            import main
            import config
            import video_processor
            import advanced_video_processor
        except ImportError as e:
            self.fail(f"无法导入模块: {e}")

if __name__ == '__main__':
    unittest.main()