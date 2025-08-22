import cv2
import numpy as np
import os

# 创建一个简单的测试图像
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :] = [255, 0, 0]  # 红色图像

# 测试不同路径
print("测试不同路径的保存能力:")

# 1. 英文路径
english_dir = r"H:\test_screenshots"
os.makedirs(english_dir, exist_ok=True)
english_path = os.path.join(english_dir, "test.png")
try:
    success = cv2.imwrite(english_path, image)
    print(f"英文路径保存结果: {success}")
except Exception as e:
    print(f"英文路径保存异常: {e}")

# 2. 中文路径
chinese_dir = r"H:\测试截图"
os.makedirs(chinese_dir, exist_ok=True)
chinese_path = os.path.join(chinese_dir, "测试.png")
try:
    success = cv2.imwrite(chinese_path, image)
    print(f"中文路径保存结果: {success}")
except Exception as e:
    print(f"中文路径保存异常: {e}")

# 3. 混合路径
mixed_dir = r"H:\test_测试"
os.makedirs(mixed_dir, exist_ok=True)
mixed_path = os.path.join(mixed_dir, "test_测试.png")
try:
    success = cv2.imwrite(mixed_path, image)
    print(f"混合路径保存结果: {success}")
except Exception as e:
    print(f"混合路径保存异常: {e}")

print("\n测试完成")