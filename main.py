import matplotlib.pyplot as plt
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def open_img(img_path):
    carplate_img = cv2.imread(img_path)
    carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    plt.imshow(carplate_img)
    #plt.show()

    return carplate_img

