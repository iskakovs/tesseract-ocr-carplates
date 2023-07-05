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

def carplate_extract(image, carplate_haar_cascade):
    carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5) # can be configured

    for x, y, w, h in carplate_rects:
        carplate_img = image[y+10:y+h, x+15:x+w-20] # can be configured

    return carplate_img

def enlarge_img(image, scale_percent):
    width = int(image.shape[1]*scale_percent/100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    plt.axis('off')
    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    return resized_image
