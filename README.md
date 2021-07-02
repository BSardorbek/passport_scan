# passport_scan
Biometrik passportdan malumotlarni o'qib olish dasturi

Passport malumotlari Internetdan olindi!

# Ubuntu 20.04
````
sudo apt-get update
````
````
sudo apt install libopencv-dev python3-opencv
````
````
python3 -c “import cv2; print(cv2.__version__)”
````
````
sudo apt install tesseract-ocr
````
````
sudo apt install libtesseract-dev
````
````
tesseract --version
````

# Windows

1. Install tesseract using windows installer available [here](https://github.com/UB-Mannheim/tesseract/wiki).
2. Note the tesseract path from the installation. Default installation path at the time of this edit was: `C:\Program Files\Tesseract-OCR\`. It may change so please check the installation path.
**WARNING: Tesseract should be either installed in the directory which is suggested during the installation or in a new directory. The uninstaller removes the whole installation directory. If you installed Tesseract in an existing directory, that directory will be removed with all its subdirectories and files.**
4. In cmd: `pip install -r requirements.txt`
5. Set the tesseract path in the script before calling  `image_to_string`:
`pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`