import cv2
import numpy as np
from PIL import Image
import os

# 创建测试图像
img = np.zeros((100, 100, 3), dtype=np.uint8)

# 测试路径（包含中文字符）
test_path = r"H:\6-黑桃大师GTO速成课（全79集）\9、线下策略\9.1 游戏级别和筹码深度调整_截图\test_fix.png"

print(f"测试路径: {test_path}")

# 确保目录存在
output_dir = os.path.dirname(test_path)
if not os.path.exists(output_dir):
    print(f"目录不存在，正在创建: {output_dir}")
    os.makedirs(output_dir)
    print(f"目录创建完成: {output_dir}")
else:
    print(f"目录已存在: {output_dir}")

# 使用PIL保存图像
try:
    # 将BGR转换为RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 转换为PIL图像
    pil_image = Image.fromarray(rgb_img)
    # 保存图像
    pil_image.save(test_path)
    print("使用PIL保存成功")
    
    # 检查文件是否存在
    if os.path.exists(test_path):
        print("文件保存成功")
        # 清理测试文件
        os.remove(test_path)
        print("测试文件已清理")
    else:
        print("文件保存失败或不存在")
except Exception as e:
    print(f"使用PIL保存失败: {e}")

print("测试完成")