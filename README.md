# License Plate Recognition using OpenCV and Tesseract

This project is a simple License Plate Recognition (LPR) system developed using OpenCV and Tesseract OCR. It captures video from a webcam, detects license plates using Haar cascades, performs Optical Character Recognition (OCR) on the detected plates, and saves images of recognized plates.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Tesseract OCR (`pip install pytesseract`)
- Haar Cascade XML file for Russian license plates (`haarcascade_russian_plate_number.xml`)

Make sure to install Tesseract OCR and provide the correct path to the Tesseract executable in the script.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   
2. Install dependencies:

  bash
  Copy code
  pip install -r requirements.txt
  Run the script:
  
3.Run the script:

  bash
  Copy code
  python license_plate_recognition.py
  
4.Press 'q' to exit the application.

## Features
- Real-time License Plate Detection and Recognition: Utilizes OpenCV for real-time video processing and license plate detection, and Tesseract OCR for character - recognition.
- Image Capture: Saves images of recognized plates in the images directory.
- Customizable OCR Configuration: Allows customization of OCR configuration for better text recognition.

## License
- This project is licensed under the MIT License.
