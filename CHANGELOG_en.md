# Changelog

## [1.0.0] - 2023-XX-XX

### Added

- Implemented basic video processor that uses OCR to recognize text in video frames, detects text content changes, and captures frames
- Implemented advanced video processor that combines OCR text recognition and image similarity analysis for more accurate change detection
- Support for multiple detection modes: text-only detection, image-only detection, and combined detection
- Command-line interface with rich command-line options and batch processing support
- Graphical user interface for convenient operation
- Automatic creation of screenshot save directories with unified naming rules for screenshot files
- Support for multiple video formats (MP4, AVI, MOV, MKV, etc.)
- Included test scripts to verify functionality correctness
- Included usage example scripts to demonstrate various features
- Provided Windows batch scripts and Unix/Linux/Mac scripts to simplify usage
- Complete Chinese documentation and usage instructions

### Technical Features

- Video processing and image operations using OpenCV
- Text recognition integration with Tesseract OCR
- Image processing using Pillow
- Numerical computations using NumPy
- Image similarity analysis using scikit-image
- Image hashing using imagehash
- Graphical user interface built with Tkinter

### Known Issues

- Text recognition accuracy is affected by video quality and fonts
- Processing time depends on video length and frame interval settings
- It is recommended to adjust the processing interval according to video content to balance accuracy and processing speed