import os
import shutil
from video_processor import VideoProcessor
from advanced_video_processor import AdvancedVideoProcessor

def test_with_real_video():
    """使用真实视频文件测试"""
    print("使用真实视频文件测试...")
    
    # 真实视频文件路径（请根据实际情况修改）
    # 这里使用一个示例路径，您需要将其替换为实际存在的视频文件路径
    real_video_path = r"H:\6-黑桃大师GTO速成课（全79集）\9、线下策略\示例视频.mp4"
    
    # 检查视频文件是否存在
    if not os.path.exists(real_video_path):
        print(f"视频文件不存在: {real_video_path}")
        print("请提供一个实际存在的视频文件路径进行测试")
        return
    
    print(f"使用视频文件: {real_video_path}")
    
    # 测试VideoProcessor
    print("\n测试VideoProcessor...")
    video_output_dir = os.path.join(os.path.dirname(real_video_path), "视频文字变化截图")
    
    # 删除已存在的输出目录
    if os.path.exists(video_output_dir):
        shutil.rmtree(video_output_dir)
    
    # 创建VideoProcessor实例并处理视频
    video_processor = VideoProcessor(real_video_path, video_output_dir)
    video_screenshots = video_processor.process_video(interval=1.0)  # 每秒处理一帧
    
    print(f"VideoProcessor处理完成，生成了 {len(video_screenshots)} 张截图")
    if len(video_screenshots) > 0:
        print(f"第一张截图: {video_screenshots[0]}")
        if os.path.exists(video_screenshots[0]):
            print("截图文件存在")
        else:
            print("截图文件不存在")
    
    # 测试AdvancedVideoProcessor
    print("\n测试AdvancedVideoProcessor...")
    advanced_output_dir = os.path.join(os.path.dirname(real_video_path), "视频高级变化截图")
    
    # 删除已存在的输出目录
    if os.path.exists(advanced_output_dir):
        shutil.rmtree(advanced_output_dir)
    
    # 创建AdvancedVideoProcessor实例并处理视频
    advanced_processor = AdvancedVideoProcessor(real_video_path, advanced_output_dir)
    advanced_screenshots = advanced_processor.process_video(interval=1.0, method="combined")
    
    print(f"AdvancedVideoProcessor处理完成，生成了 {len(advanced_screenshots)} 张截图")
    if len(advanced_screenshots) > 0:
        print(f"第一张截图: {advanced_screenshots[0]}")
        if os.path.exists(advanced_screenshots[0]):
            print("截图文件存在")
        else:
            print("截图文件不存在")
    
    # 清理输出目录
    print("\n清理输出目录...")
    for dir_path in [video_output_dir, advanced_output_dir]:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"已删除目录: {dir_path}")
    
    print("\n测试完成")

if __name__ == "__main__":
    test_with_real_video()