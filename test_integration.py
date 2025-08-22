import cv2
import numpy as np
from video_processor import VideoProcessor
from advanced_video_processor import AdvancedVideoProcessor
import os
import shutil

def create_test_video():
    """创建一个简单的测试视频"""
    print("创建测试视频...")
    
    # 测试视频文件路径（包含中文）
    test_video_dir = r"H:\6-黑桃大师GTO速成课（全79集）\9、线下策略"
    test_video_path = os.path.join(test_video_dir, "test_video.mp4")
    
    # 确保测试目录存在
    os.makedirs(test_video_dir, exist_ok=True)
    
    # 如果测试视频已存在，则删除
    if os.path.exists(test_video_path):
        os.remove(test_video_path)
    
    # 创建视频写入对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(test_video_path, fourcc, 1.0, (640, 480))
    
    # 生成测试帧
    for i in range(30):  # 30帧
        # 创建彩色图像
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # 每10帧改变一次颜色
        if i // 10 == 0:
            frame[:, :] = [255, 0, 0]  # 蓝色
        elif i // 10 == 1:
            frame[:, :] = [0, 255, 0]  # 绿色
        else:
            frame[:, :] = [0, 0, 255]  # 红色
        
        # 添加帧编号文本
        cv2.putText(frame, f'Frame {i}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # 写入帧
        out.write(frame)
    
    # 释放视频写入对象
    out.release()
    print(f"测试视频已创建: {test_video_path}")
    return test_video_path


def test_video_processor_integration():
    """测试VideoProcessor类的完整功能"""
    print("\n测试VideoProcessor类的完整功能...")
    
    # 创建测试视频
    test_video_path = create_test_video()
    
    # 创建输出目录
    output_dir = os.path.join(os.path.dirname(test_video_path), "9.1 游戏级别和筹码深度调整_截图")
    
    # 删除已存在的输出目录
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    # 创建VideoProcessor实例并处理视频
    processor = VideoProcessor(test_video_path, output_dir)
    screenshots = processor.process_video(interval=0.5)  # 每0.5秒处理一帧
    
    print(f"VideoProcessor处理完成，生成了 {len(screenshots)} 张截图")
    
    # 检查截图是否生成
    if len(screenshots) > 0:
        print(f"第一张截图路径: {screenshots[0]}")
        if os.path.exists(screenshots[0]):
            print("截图文件存在")
        else:
            print("截图文件不存在")
    else:
        print("没有生成截图")
    
    return output_dir


def test_advanced_video_processor_integration():
    """测试AdvancedVideoProcessor类的完整功能"""
    print("\n测试AdvancedVideoProcessor类的完整功能...")
    
    # 使用已创建的测试视频
    test_video_dir = r"H:\6-黑桃大师GTO速成课（全79集）\9、线下策略"
    test_video_path = os.path.join(test_video_dir, "test_video.mp4")
    
    # 创建输出目录
    output_dir = os.path.join(os.path.dirname(test_video_path), "9.1 游戏级别和筹码深度调整_高级截图")
    
    # 删除已存在的输出目录
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    # 创建AdvancedVideoProcessor实例并处理视频
    processor = AdvancedVideoProcessor(test_video_path, output_dir)
    screenshots = processor.process_video(interval=0.5, method="combined")
    
    print(f"AdvancedVideoProcessor处理完成，生成了 {len(screenshots)} 张截图")
    
    # 检查截图是否生成
    if len(screenshots) > 0:
        print(f"第一张截图路径: {screenshots[0]}")
        if os.path.exists(screenshots[0]):
            print("截图文件存在")
        else:
            print("截图文件不存在")
    else:
        print("没有生成截图")
    
    return output_dir


def cleanup(test_video_path, video_processor_output, advanced_processor_output):
    """清理测试文件"""
    print("\n清理测试文件...")
    
    # 删除测试视频
    if os.path.exists(test_video_path):
        os.remove(test_video_path)
        print(f"已删除测试视频: {test_video_path}")
    
    # 删除输出目录
    for dir_path in [video_processor_output, advanced_processor_output]:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"已删除目录: {dir_path}")


def main():
    test_video_path = None
    video_processor_output = None
    advanced_processor_output = None
    
    try:
        # 测试VideoProcessor
        video_processor_output = test_video_processor_integration()
        
        # 测试AdvancedVideoProcessor
        advanced_processor_output = test_advanced_video_processor_integration()
    except Exception as e:
        print(f"测试过程中出现错误: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # 清理
        if test_video_path:
            cleanup(test_video_path, video_processor_output, advanced_processor_output)
        print("\n集成测试完成")

if __name__ == "__main__":
    main()