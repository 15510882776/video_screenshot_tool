# 视频变化截图工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

这是一个自动处理视频文件的工具，能够检测视频中画面或文字内容的变化并自动截取相应的画面。

## 功能特点

- 自动检测视频中文字内容的变化
- 自动检测视频中画面内容的变化
- 在内容发生变化时自动截取视频画面
- 将截图保存到与视频相同的目录下
- 支持多种视频格式（MP4, AVI, MOV, MKV等）
- 可配置处理间隔时间
- 支持批量处理多个视频文件
- 支持多种检测模式（仅文字、仅画面、综合检测）
- 提供图形用户界面和命令行界面

## 安装要求

### 系统依赖

1. **Python 3.7或更高版本**
2. **Tesseract OCR** - 用于文字识别
   - Windows: 从[这里](https://github.com/UB-Mannheim/tesseract/wiki)下载安装
   - macOS: `brew install tesseract`
   - Linux: `sudo apt install tesseract-ocr`
3. **中文语言包**（用于识别中文）
   - Windows: 安装时选择中文语言包
   - macOS/Linux: `sudo apt install tesseract-ocr-chi-sim` 或相应命令

### Python依赖

```bash
pip install -r requirements.txt
```

### 开发依赖

- `flake8`: 用于代码风格检查
- `mypy`: 用于类型检查

## 安装步骤

1. 克隆或下载本仓库
2. 安装系统依赖（Python 3.7+ 和 Tesseract OCR）
3. 安装Python依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 配置Tesseract路径（如果需要）：
   在 `config.py` 中设置 `TESSERACT_CMD` 变量为Tesseract可执行文件的路径

## 使用方法

### 命令行使用

```bash
# 处理单个视频文件（基础文字检测）
python main.py video.mp4

# 处理单个视频文件（高级综合检测）
python main.py video.mp4 --processor advanced

# 处理单个视频文件（仅检测文字变化）
python main.py video.mp4 --processor advanced --method text

# 处理单个视频文件（仅检测画面变化）
python main.py video.mp4 --processor advanced --method image

# 处理多个视频文件
python main.py video1.mp4 video2.mp4

# 设置处理间隔（秒）
python main.py video.mp4 --interval 0.5

# 启动图形界面
python main.py --gui

# 处理当前目录下所有MP4文件
python main.py *.mp4
```

### 图形界面使用

直接运行以下命令启动图形界面：

```bash
python main.py --gui
```

图形界面提供了直观的操作方式，用户可以通过简单的点击操作选择视频文件、设置参数并启动处理。

### 配置

如果Tesseract OCR没有安装在系统PATH中，需要在`config.py`中设置路径：

```python
# config.py
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows示例
```

## 输出说明

截图将保存在与视频文件相同的目录下，文件夹名为`视频名_截图`，截图文件命名为`视频名_截图_001.png`、`视频名_截图_002.png`等。

## 工作原理

### 基础处理器
1. 以设定的时间间隔逐帧读取视频
2. 对每一帧进行OCR文字识别
3. 比较当前帧与前一帧的文字内容
4. 如果检测到文字变化，则保存当前帧为截图
5. 将截图保存到指定目录

### 高级处理器
1. 以设定的时间间隔逐帧读取视频
2. 根据选择的检测方法进行变化检测：
   - 仅文字：对每一帧进行OCR文字识别，比较文字内容变化
   - 仅画面：计算帧间的结构相似性指数(SSIM)或感知哈希差异
   - 综合检测：同时进行文字和画面变化检测，任一有变化即保存截图
3. 将截图保存到指定目录

## 项目结构

```
video_screenshot_tool/
├── advanced_video_processor.py  # 高级视频处理器（图像和文字变化检测）
├── CHANGELOG.md                 # 更新日志
├── CHANGELOG_en.md              # 更新日志（英文）
├── CODE_OF_CONDUCT.md           # 行为准则
├── CODE_OF_CONDUCT_en.md        # 行为准则（英文）
├── CONTRIBUTING.md              # 贡献指南
├── CONTRIBUTING_en.md           # 贡献指南（英文）
├── config.py                    # 配置文件
├── example_usage.py             # 使用示例
├── gui.py                       # 图形用户界面
├── icon.svg                     # 应用程序图标
├── LICENSE                      # 许可证文件
├── main.py                      # 主程序入口
├── MANIFEST.in                  # 打包配置文件
├── mypy.ini                     # 类型检查配置文件
├── PROJECT_SUMMARY.md           # 项目总结
├── README.md                    # 详细说明文档（中文）
├── README_en.md                 # 详细说明文档（英文）
├── requirements.txt             # Python依赖列表
├── run.bat                      # Windows批处理脚本
├── run.sh                       # Unix/Linux/Mac脚本
├── setup.py                     # 项目安装和打包配置
├── test_tool.py                 # 测试工具
├── video_processor.py           # 基础视频处理器（仅文字变化检测）
├── .flake8                      # 代码质量检查配置文件
├── tests/                       # 测试目录
│   ├── __init__.py              # 测试模块初始化文件
│   ├── test_config.py           # 测试配置文件
│   └── test_video_processor.py  # 视频处理器测试文件
└── .github/
    └── workflows/
        ├── codeql.yml           # 代码质量检查工作流
        ├── release.yml          # 发布工作流
        └── test.yml             # 测试工作流
```

## 安装

### 从源码安装

```bash
pip install -r requirements.txt
```

### 作为包安装

```bash
pip install -e .
```

这将安装项目及其依赖，并创建一个命令行入口点 `video-screenshot`。

## 贡献

欢迎贡献！请查看我们的[贡献指南](CONTRIBUTING.md)和[行为准则](CODE_OF_CONDUCT.md)了解更多信息。

## GitHub Actions

本项目使用 GitHub Actions 进行持续集成和持续部署：

- `test.yml`: 在多个 Python 版本上运行测试，确保代码质量
- `release.yml`: 在发布新标签时自动构建可执行文件并创建 GitHub Release

## 测试工具

项目包含一个简单的测试脚本，用于验证工具的基本功能是否正常工作：

```bash
python test_tool.py
```

该脚本会创建一个测试视频，然后使用基础和高级处理器进行处理，验证截图功能是否正常。

## 使用示例

项目包含一个使用示例脚本，展示了如何使用工具的各种功能：

```bash
python example_usage.py
```

该脚本包含了基础使用、高级使用和自定义输出目录的示例代码。

## 运行脚本

为了简化使用，项目提供了运行脚本：

- Windows: `run.bat`
- Unix/Linux/Mac: `run.sh`

这些脚本会自动安装依赖并提供简单的使用方式。

## 上传到GitHub的步骤

1. 安装Git：
   - 访问 [Git官网](https://git-scm.com/downloads) 下载适用于Windows的Git
   - 运行安装程序并按照提示完成安装
   - 验证安装：在命令行中运行 `git --version`

2. 在GitHub上创建新的仓库：
   - 登录GitHub账户
   - 点击右上角的"+"号，选择"New repository"
   - 输入仓库名称（例如：video-screenshot-tool）
   - 选择是否公开（Public）或私有（Private）
   - 不要初始化README、.gitignore或license
   - 点击"Create repository"

3. 在本地初始化Git仓库并推送代码：
   ```bash
   # 打开命令行工具并导航到项目目录
   cd /path/to/video_screenshot_tool
   
   # 初始化Git仓库
   git init
   
   # 添加所有文件到暂存区
   git add .
   
   # 提交更改
   git commit -m "Initial commit"
   
   # 添加远程仓库（使用你在GitHub上创建的仓库URL）
   git remote add origin https://github.com/yourusername/video-screenshot-tool.git
   
   # 推送到GitHub
   git branch -M main
   git push -u origin main
   ```

## 许可证

本项目采用MIT许可证，详情请见 [LICENSE](LICENSE) 文件。

## 联系方式

如有任何问题或建议，请通过GitHub Issues与我们联系。