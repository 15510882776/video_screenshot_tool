import os
import sys
import tempfile
import shutil
import unittest
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from video_processor import VideoProcessor
from advanced_video_processor import AdvancedVideoProcessor


def create_test_video(output_path, duration=5):
    """
    创建一个简单的测试视频
    :param output_path: 输出视频路径
    :param duration: 视频时长（秒）
    """
    import cv2
    import numpy as np
    
    # 视频参数
    width, height = 640, 480
    fps = 30
    total_frames = duration * fps
    
    # 创建视频写入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
    
    for i in range(total_frames):
        # 创建黑色背景
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # 添加一些变化的文本
        time_sec = i / fps
        text = f"Time: {time_sec:.1f}s"
        
        # 在不同时间显示不同文字
        if time_sec < duration / 3:
            cv2.putText(frame, "Section 1", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
            cv2.putText(frame, text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        elif time_sec < 2 * duration / 3:
            cv2.putText(frame, "Section 2", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            cv2.putText(frame, text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Section 3", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            cv2.putText(frame, text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # 写入帧
        out.write(frame)
    
    # 释放资源
    out.release()
    print(f"测试视频已创建: {output_path}")


def test_basic_processor(video_path):
    """
    测试基础视频处理器
    :param video_path: 视频路径
    """
    print("\n=== 测试基础视频处理器 ===")
    
    try:
        processor = VideoProcessor(str(video_path))
        screenshots = processor.process_video(interval=1.0)
        
        print(f"基础处理器结果:")
        print(f"  - 生成截图数量: {len(screenshots)}")
        print(f"  - 截图保存位置: {processor.output_dir}")
        
        # 验证截图文件存在
        for screenshot in screenshots:
            if os.path.exists(screenshot):
                print(f"  - 截图文件存在: {os.path.basename(screenshot)}")
            else:
                print(f"  - 截图文件缺失: {os.path.basename(screenshot)}")
                
        return True
    except Exception as e:
        print(f"基础处理器测试失败: {e}")
        return False


def test_advanced_processor(video_path):
    """
    测试高级视频处理器
    :param video_path: 视频路径
    """
    print("\n=== 测试高级视频处理器 ===")
    
    try:
        processor = AdvancedVideoProcessor(str(video_path))
        
        # 测试不同方法
        methods = ["text", "image", "combined"]
        for method in methods:
            print(f"\n测试方法: {method}")
            screenshots = processor.process_video(interval=1.0, method=method)
            
            print(f"  - 生成截图数量: {len(screenshots)}")
            
            # 验证截图文件存在
            for screenshot in screenshots:
                if os.path.exists(screenshot):
                    print(f"  - 截图文件存在: {os.path.basename(screenshot)}")
                else:
                    print(f"  - 截图文件缺失: {os.path.basename(screenshot)}")
                    
        return True
    except Exception as e:
        print(f"高级处理器测试失败: {e}")
        return False


def run_all_tests():
    """
    运行所有单元测试
    """
    # 发现并运行tests目录下的所有测试
    loader = unittest.TestLoader()
    start_dir = os.path.join(project_root, 'tests')
    suite = loader.discover(start_dir, pattern='test*.py')
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def main():
    """
    主测试函数
    """
    print("视频变化截图工具测试脚本")
    print("=" * 40)
    
    # 创建临时目录
    temp_dir = Path(tempfile.mkdtemp(prefix="video_test_"))
    print(f"临时测试目录: {temp_dir}")
    
    try:
        # 创建测试视频
        video_path = temp_dir / "test_video.mp4"
        create_test_video(video_path, duration=5)
        
        if not video_path.exists():
            print("错误: 测试视频创建失败")
            return
            
        # 测试基础处理器
        basic_success = test_basic_processor(video_path)
        
        # 测试高级处理器
        advanced_success = test_advanced_processor(video_path)
        
        # 运行单元测试
        print("\n" + "=" * 40)
        print("运行单元测试:")
        unit_tests_success = run_all_tests()
        
        # 汇总结果
        print("\n" + "=" * 40)
        print("测试结果汇总:")
        print(f"  - 基础处理器: {'通过' if basic_success else '失败'}")
        print(f"  - 高级处理器: {'通过' if advanced_success else '失败'}")
        print(f"  - 单元测试: {'通过' if unit_tests_success else '失败'}")
        print(f"  - 整体测试: {'通过' if basic_success and advanced_success and unit_tests_success else '失败'}")
        
    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # 清理临时目录
        try:
            shutil.rmtree(temp_dir)
            print(f"\n已清理临时目录: {temp_dir}")
        except Exception as e:
            print(f"清理临时目录失败: {e}")


if __name__ == "__main__":
    main()