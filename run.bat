@echo off
setlocal

:: 检查Python是否已安装
echo 检查Python环境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未检测到Python。请先安装Python 3.7或更高版本。
    pause
    exit /b 1
)

echo Python环境检查通过

:: 检查pip是否可用
echo 检查pip...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未检测到pip。
    pause
    exit /b 1
)

echo pip检查通过

:: 安装依赖
echo 安装依赖包...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo 错误: 依赖包安装失败。
    pause
    exit /b 1
)

echo 依赖包安装完成

echo.
echo 使用方法:
echo 1. 将视频文件拖拽到此窗口并按回车运行
echo 2. 或者在命令行中运行: python main.py [视频文件路径]
echo.

:: 如果提供了视频文件参数，则直接处理
if "%1"=="" (
    echo 请将视频文件拖拽到此窗口，或按任意键退出...
    pause >nul
    exit /b 0
)

:: 处理视频文件
python main.py %*

pause