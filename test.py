import cv2
import numpy as np
import pytesseract
from PIL import Image
import os
import glob
src_path="C:/Users/hamza/Desktop/appliedProject"


# Read image with opencv
img = cv2.imread("C:/MusicUsers/hamza/Desktop/appliedProject/sudoku.png")
# Convert to gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

# Write image after removed noise
cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
#img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 29, 2)
    # Write the image after apply opencv to do some ...
cv2.imwrite(src_path + "thres.png", img)


#imgwidth, imgheight = im.size

img2=[]
img2=img[0:27,0:27]
cv2.imwrite("cropped.png", img2)
#fill image up
inputImage = img2

outputImage = cv2.copyMakeBorder(inputImage,150,150,150,150,cv2.BORDER_CONSTANT,value=[255,255,255])

resized = cv2.resize(inputImage, (128,128), interpolation = cv2.INTER_AREA)

#resized = cv2.adaptiveThreshold(outputImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,31, 2)
resized = cv2.dilate(resized, kernel, iterations=1)
resized = cv2.erode(resized, kernel, iterations=1)

cv2.imwrite('output.jpg', outputImage)
cv2.imwrite('resized.jpg', resized)
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

result = pytesseract.image_to_string(resized)

print(result )
