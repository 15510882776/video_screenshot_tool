#!/bin/bash

# 检查Python是否已安装
echo "检查Python环境..."
if ! command -v python3 &> /dev/null
then
    echo "错误: 未检测到Python3。请先安装Python 3.7或更高版本。"
    exit 1
fi

echo "Python环境检查通过"

# 检查pip是否可用
echo "检查pip..."
if ! command -v pip3 &> /dev/null
then
    echo "错误: 未检测到pip3。"
    exit 1
fi

echo "pip检查通过"

# 安装依赖
echo "安装依赖包..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "错误: 依赖包安装失败。"
    exit 1
fi

echo "依赖包安装完成"

echo ""
echo "使用方法:"
echo "1. 在命令行中运行: python3 main.py [视频文件路径]"
echo "2. 或者: ./run.sh [视频文件路径]"
echo ""

# 如果提供了视频文件参数，则直接处理
if [ $# -eq 0 ]; then
    echo "请提供视频文件路径作为参数"
    echo "例如: ./run.sh video.mp4"
    exit 0
fi

# 处理视频文件
python3 main.py "$@"

read -p "按回车键退出..."