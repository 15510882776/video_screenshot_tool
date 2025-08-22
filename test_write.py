import cv2
import numpy as np
import os

# 创建一个简单的测试图像
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :] = [255, 0, 0]  # 红色图像

# 原始目标路径
output_dir = r"H:\6-黑桃大师GTO速成课（全79集）\9、线下策略\9.1 游戏级别和筹码深度调整_截图"
filename = "test_write.png"
screenshot_path = os.path.join(output_dir, filename)

print(f"原始路径: {screenshot_path}")
print(f"目录是否存在: {os.path.exists(output_dir)}")

# 检查路径中的特殊字符
print("\n路径分析:")
path_parts = screenshot_path.split(os.sep)
for i, part in enumerate(path_parts):
    print(f"  [{i}] {part}")
    # 检查是否有特殊字符
    if any(ord(c) > 127 for c in part):
        print(f"      ^-- 包含非ASCII字符")

# 尝试规范化路径
normalized_path = os.path.normpath(screenshot_path)
print(f"\n规范化路径: {normalized_path}")

# 尝试使用不同的编码保存
print("\n尝试不同的保存方法:")

# 方法1: 直接保存
try:
    success = cv2.imwrite(screenshot_path, image)
    print(f"直接保存结果: {success}")
except Exception as e:
    print(f"直接保存异常: {e}")

# 方法2: 使用规范化路径
try:
    success = cv2.imwrite(normalized_path, image)
    print(f"规范化路径保存结果: {success}")
except Exception as e:
    print(f"规范化路径保存异常: {e}")

# 方法3: 检查路径长度
print(f"\n路径长度: {len(screenshot_path)} 字符")
if len(screenshot_path) > 260:
    print("警告: 路径可能过长 (超过260字符)")

# 方法4: 尝试保存到简单路径
simple_path = os.path.join(output_dir, "simple.png")
try:
    success = cv2.imwrite(simple_path, image)
    print(f"简单文件名保存结果: {success}")
    if success and os.path.exists(simple_path):
        print("简单文件名保存成功且文件存在")
        # 清理测试文件
        os.remove(simple_path)
except Exception as e:
    print(f"简单文件名保存异常: {e}")

# 列出目录中的文件
print("\n目录中的文件:")
try:
    files = os.listdir(output_dir)
    for file in files:
        print(f"  {file}")
except Exception as e:
    print(f"列出目录内容时出错: {e}")