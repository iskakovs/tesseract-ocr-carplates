# Car Plate Detection using Tesseract OCR

This project aims to detect and extract license plate information from car images using Tesseract OCR. It is implemented in Python and provides a simple and easy-to-use interface for detecting and extracting car plate numbers from images.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatic detection of license plates in car images
- Extraction of license plate numbers using Tesseract OCR
- Supports various image formats, such as JPEG, PNG, and BMP
- Configurable options for preprocessing and OCR settings
- Simple and intuitive Python API for easy integration into existing projects

## Installation

1. Clone the repository:

```shell
git clone https://github.com/iskakovs/car-plate-detection.git
```

2. Install the required dependencies:

```shell
pip install -r requirements.txt
```

3. Download the Tesseract OCR engine and language data. Refer to the [Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract) for instructions specific to your operating system.

4. Place the Tesseract OCR executable and language data files in the appropriate directory. Update the `config.py` file with the correct file paths.

## Usage

1. Import the `car_plate_detector` module:

```python
from car_plate_detector import CarPlateDetector
```

2. Create an instance of the `CarPlateDetector` class:

```python
detector = CarPlateDetector()
```

3. Load an image:

```python
image = detector.load_image('path/to/image.jpg')
```

4. Detect license plates in the image:

```python
plates = detector.detect_plates(image)
```

5. Extract the license plate numbers using Tesseract OCR:

```python
for plate in plates:
    plate_number = detector.extract_plate_number(plate)
    print("Detected plate number:", plate_number)
```

For more detailed examples and usage instructions, please refer to the [documentation](#link-to-documentation) of the project.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality of the project, please open a new issue or submit a pull request. Make sure to follow the project's coding style and guidelines.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

---

Thank you for your interest in the Car Plate Detection project! If you have any questions or need further assistance, please don't hesitate to reach out.
