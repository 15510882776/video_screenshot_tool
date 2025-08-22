import cv2
import numpy as np
from video_processor import VideoProcessor
from advanced_video_processor import AdvancedVideoProcessor
import os
import shutil

def test_video_processor():
    """测试VideoProcessor类"""
    print("测试VideoProcessor类...")
    
    # 创建测试视频文件路径（包含中文）
    test_video_dir = r"H:\6-黑桃大师GTO速成课（全79集）\9、线下策略"
    test_video_path = os.path.join(test_video_dir, "test_video.mp4")
    
    # 创建测试输出目录
    output_dir = os.path.join(test_video_dir, "9.1 游戏级别和筹码深度调整_截图")
    
    # 确保测试目录存在
    os.makedirs(test_video_dir, exist_ok=True)
    
    # 创建一个简单的测试视频（如果不存在）
    if not os.path.exists(test_video_path):
        # 创建测试图像
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        img[:, :] = [255, 0, 0]  # 红色图像
        
        # 保存为图像文件
        cv2.imwrite(test_video_path.replace('.mp4', '.png'), img)
        print(f"已创建测试图像: {test_video_path.replace('.mp4', '.png')}")
        
        # 为测试目的，我们直接使用图像文件作为视频文件
        # 在实际应用中，这里应该是一个真实的视频文件
    
    # 创建VideoProcessor实例
    processor = VideoProcessor(test_video_path, output_dir)
    
    # 检查输出目录是否已创建
    if os.path.exists(output_dir):
        print(f"输出目录已存在: {output_dir}")
    else:
        print(f"输出目录不存在: {output_dir}")
    
    print("VideoProcessor测试完成")


def test_advanced_video_processor():
    """测试AdvancedVideoProcessor类"""
    print("\n测试AdvancedVideoProcessor类...")
    
    # 创建测试视频文件路径（包含中文）
    test_video_dir = r"H:\6-黑桃大师GTO速成课（全79集）\9、线下策略"
    test_video_path = os.path.join(test_video_dir, "test_video.mp4")
    
    # 创建测试输出目录
    output_dir = os.path.join(test_video_dir, "9.1 游戏级别和筹码深度调整_高级截图")
    
    # 创建AdvancedVideoProcessor实例
    processor = AdvancedVideoProcessor(test_video_path, output_dir)
    
    # 检查输出目录是否已创建
    if os.path.exists(output_dir):
        print(f"输出目录已存在: {output_dir}")
    else:
        print(f"输出目录不存在: {output_dir}")
    
    print("AdvancedVideoProcessor测试完成")


def cleanup():
    """清理测试文件"""
    test_video_dir = r"H:\6-黑桃大师GTO速成课（全79集）\9、线下策略"
    
    # 删除测试创建的目录
    for dir_name in ["9.1 游戏级别和筹码深度调整_截图", "9.1 游戏级别和筹码深度调整_高级截图"]:
        dir_path = os.path.join(test_video_dir, dir_name)
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"已删除目录: {dir_path}")

if __name__ == "__main__":
    try:
        test_video_processor()
        test_advanced_video_processor()
    finally:
        # 清理测试文件
        cleanup()
        print("\n测试完成并已清理")