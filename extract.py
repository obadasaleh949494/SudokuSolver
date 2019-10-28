import cv2
from PIL import Image
src_path="C:/Users/hamza/Desktop/"
#gray image
img = cv2.imread("C:/Users/hamza/Desktop/sudoku.png")
image_sudoku_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#adaptive threshold
thresh = cv2.adaptiveThreshold(image_sudoku_gray,255,1,1,11,15)

#show image
cv2.imwrite(src_path + "thres.png", img)
