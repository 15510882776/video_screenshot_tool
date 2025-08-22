# Video Change Screenshot Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is an automated video processing tool that can detect changes in video content (either visual or textual) and automatically capture corresponding screenshots.

## Key Features

- Automatically detect changes in text content within videos
- Automatically detect changes in visual content within videos
- Automatically capture video frames when content changes
- Save screenshots in the same directory as the video
- Support for multiple video formats (MP4, AVI, MOV, MKV, etc.)
- Configurable processing interval
- Support for batch processing of multiple video files
- Multiple detection modes (text only, image only, combined detection)
- Both graphical user interface and command-line interface

## Installation Requirements

### System Dependencies

1. **Python 3.7 or higher**
2. **Tesseract OCR** - for text recognition
   - Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki)
   - macOS: `brew install tesseract`
   - Linux: `sudo apt install tesseract-ocr`
3. **Chinese language pack** (for Chinese text recognition)
   - Windows: Select Chinese language pack during installation
   - macOS/Linux: `sudo apt install tesseract-ocr-chi-sim` or equivalent command

### Python Dependencies

```bash
pip install -r requirements.txt
```

### Development Dependencies

- `flake8`: For code style checking
- `mypy`: For type checking

## Installation Steps

1. Clone or download this repository
2. Install system dependencies (Python 3.7+ and Tesseract OCR)
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure Tesseract path (if needed):
   Set the `TESSERACT_CMD` variable in `config.py` to the path of the Tesseract executable

## Usage

### Command Line Usage

```bash
# Process a single video file (basic text detection)
python main.py video.mp4

# Process a single video file (advanced combined detection)
python main.py video.mp4 --processor advanced

# Process a single video file (text change detection only)
python main.py video.mp4 --processor advanced --method text

# Process a single video file (image change detection only)
python main.py video.mp4 --processor advanced --method image

# Process multiple video files
python main.py video1.mp4 video2.mp4

# Set processing interval (seconds)
python main.py video.mp4 --interval 0.5

# Launch the graphical interface
python main.py --gui

# Process all MP4 files in the current directory
python main.py *.mp4
```

### Graphical Interface Usage

Run the following command to launch the graphical interface:

```bash
python main.py --gui
```

The graphical interface provides an intuitive way to operate, allowing users to select video files, set parameters, and start processing through simple clicks.

### Configuration

If Tesseract OCR is not installed in the system PATH, you need to set the path in `config.py`:

```python
# config.py
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows example
```

## Output Description

Screenshots will be saved in the same directory as the video file, in a folder named `video_name_screenshots`. The screenshot files will be named `video_name_screenshot_001.png`, `video_name_screenshot_002.png`, etc.

## Working Principle

### Basic Processor
1. Read video frames at set time intervals
2. Perform OCR text recognition on each frame
3. Compare the text content of the current frame with the previous frame
4. If text changes are detected, save the current frame as a screenshot
5. Save the screenshot to the specified directory

### Advanced Processor
1. Read video frames at set time intervals
2. Perform change detection based on the selected method:
   - Text only: Perform OCR text recognition on each frame and compare text content changes
   - Image only: Calculate the Structural Similarity Index (SSIM) or perceptual hash difference between frames
   - Combined detection: Perform both text and image change detection, saving screenshots when either detects changes
3. Save the screenshots to the specified directory

## Project Structure

```
video_screenshot_tool/
├── advanced_video_processor.py  # Advanced video processor (image and text change detection)
├── CHANGELOG.md                 # Changelog
├── CHANGELOG_en.md              # Changelog (English)
├── CODE_OF_CONDUCT.md           # Code of Conduct
├── CODE_OF_CONDUCT_en.md        # Code of Conduct (English)
├── CONTRIBUTING.md              # Contribution Guidelines
├── CONTRIBUTING_en.md           # Contribution Guidelines (English)
├── config.py                    # Configuration file
├── example_usage.py             # Usage examples
├── gui.py                       # Graphical user interface
├── icon.svg                     # Application icon
├── LICENSE                      # License file
├── main.py                      # Main program entry
├── MANIFEST.in                  # Packaging configuration file
├── mypy.ini                     # Type checking configuration file
├── PROJECT_SUMMARY.md           # Project summary
├── README.md                    # Detailed documentation (Chinese)
├── README_en.md                 # Detailed documentation (English)
├── requirements.txt             # Python dependencies list
├── run.bat                      # Windows batch script
├── run.sh                       # Unix/Linux/Mac script
├── setup.py                     # Project installation and packaging configuration
├── test_tool.py                 # Test tool
├── video_processor.py           # Basic video processor (text change detection only)
├── .flake8                      # Code quality checking configuration file
├── tests/                       # Test directory
│   ├── __init__.py              # Test module initialization file
│   ├── test_config.py           # Test configuration file
│   └── test_video_processor.py  # Video processor test file
└── .github/
    └── workflows/
        ├── codeql.yml           # Code quality checking workflow
        ├── release.yml          # Release workflow
        └── test.yml             # Test workflow
```

## Installation

### Installing from source

```bash
pip install -r requirements.txt
```

### Installing as a package

```bash
pip install -e .
```

This will install the project and its dependencies, and create a command-line entry point `video-screenshot`.

## Contributing

Contributions are welcome! Please check out our [Contribution Guidelines](CONTRIBUTING_en.md) and [Code of Conduct](CODE_OF_CONDUCT_en.md) for more information.

## GitHub Actions

This project uses GitHub Actions for continuous integration and continuous deployment:

- `test.yml`: Runs tests on multiple Python versions to ensure code quality
- `release.yml`: Automatically builds executables and creates GitHub Releases when new tags are pushed

## Test Tool

The project includes a simple test script to verify that the basic functionality of the tool is working correctly:

```bash
python test_tool.py
```

This script creates a test video, then processes it using both the basic and advanced processors to verify that the screenshot function is working properly.

## Usage Examples

The project includes a usage example script that demonstrates how to use the various features of the tool:

```bash
python example_usage.py
```

This script includes example code for basic usage, advanced usage, and custom output directories.

## Run Scripts

To simplify usage, the project provides run scripts:

- Windows: `run.bat`
- Unix/Linux/Mac: `run.sh`

These scripts will automatically install dependencies and provide a simple way to use the tool.

## Steps to Upload to GitHub

1. Install Git:
   - Visit the [Git website](https://git-scm.com/downloads) to download Git for Windows
   - Run the installer and follow the prompts to complete the installation
   - Verify the installation: Run `git --version` in the command line

2. Create a new repository on GitHub:
   - Log in to your GitHub account
   - Click the "+" icon in the upper right corner and select "New repository"
   - Enter a repository name (e.g., video-screenshot-tool)
   - Choose whether to make it Public or Private
   - Do not initialize with a README, .gitignore, or license
   - Click "Create repository"

3. Initialize the Git repository locally and push the code:
   ```bash
   # Open command line tool and navigate to the project directory
   cd /path/to/video_screenshot_tool
   
   # Initialize Git repository
   git init
   
   # Add all files to staging area
   git add .
   
   # Commit changes
   git commit -m "Initial commit"
   
   # Add remote repository (use the URL of the repository you created on GitHub)
   git remote add origin https://github.com/yourusername/video-screenshot-tool.git
   
   # Push to GitHub
   git branch -M main
   git push -u origin main
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please contact us through GitHub Issues.