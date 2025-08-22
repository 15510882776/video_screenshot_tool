#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
视频变化截图工具使用示例
========================

这个脚本展示了如何使用视频变化截图工具的各种功能。
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from main import process_single_video, process_multiple_videos


def example_basic_usage():
    """基础使用示例"""
    print("=== 基础使用示例 ===")
    
    # 假设我们有一个视频文件
    video_file = "example.mp4"
    
    # 检查文件是否存在
    if not os.path.exists(video_file):
        print(f"警告: 视频文件 '{video_file}' 不存在，此为演示代码")
        print("请将 'example.mp4' 替换为实际的视频文件路径")
        return
    
    # 使用基础处理器处理单个视频
    print(f"处理视频: {video_file}")
    success = process_single_video(video_file, interval=1.0, processor_type="basic")
    
    if success:
        print("处理成功完成")
    else:
        print("处理失败")


def example_advanced_usage():
    """高级使用示例"""
    print("\n=== 高级使用示例 ===")
    
    # 假设我们有多个视频文件
    video_files = ["example1.mp4", "example2.mp4", "example3.mp4"]
    
    # 检查文件是否存在
    existing_files = [f for f in video_files if os.path.exists(f)]
    
    if not existing_files:
        print(f"警告: 视频文件 {video_files} 不存在，此为演示代码")
        print("请将文件名替换为实际的视频文件路径")
        return
    
    # 使用高级处理器批量处理视频，仅检测文字变化
    print(f"批量处理视频: {existing_files}")
    process_multiple_videos(existing_files, interval=0.5, 
                           processor_type="advanced", method="text")
    
    print("批量处理完成")


def example_custom_output():
    """
    自定义输出目录示例
    注意: 这需要修改VideoProcessor类以支持自定义输出目录
    """
    print("\n=== 自定义输出目录示例 ===")
    
    video_file = "example.mp4"
    
    if not os.path.exists(video_file):
        print(f"警告: 视频文件 '{video_file}' 不存在，此为演示代码")
        return
    
    # 通常输出目录是自动确定的，但可以通过修改代码支持自定义目录
    print("输出目录通常与视频文件在同一目录下，名为'视频名_截图'")
    print("可以通过修改VideoProcessor类来支持自定义输出目录")


def main():
    """主函数"""
    print("视频变化截图工具使用示例")
    print("=" * 40)
    
    # 运行各种示例
    example_basic_usage()
    example_advanced_usage()
    example_custom_output()
    
    print("\n" + "=" * 40)
    print("更多使用方法请参考README.md文件")


if __name__ == "__main__":
    main()