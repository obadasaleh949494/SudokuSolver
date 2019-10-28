from PIL import Image
import os
import glob
import cv2
import pytesseract
import math


def DividImage():
    im = cv2.imread('2.jpg')
    img=[]
    imgheight,imgwidth,d =im.shape
    width=imgwidth/9
    height=imgheight/9
    w=math.floor(width)
    h=math.floor(height)
    rr=w/9
    r=math.ceil(rr)
    cc=h/9
    c=math.ceil(cc)
    xx=4
    yy=3
    e=w
    ee=h
    counter1=1
    counter2=1
    for x in range (9):
        yy=4
        ee=h
        for y in range ( 9):
          if y==3 or y==6:
                  yy=yy+3
          img=im[xx:e,yy:ee]
          name="cropped"+str(x)+str(y)+".png"
          cv2.imwrite(name , img)
          yy=ee+2
          ee=ee+h
          if y==7 :
              ee=ee-math.ceil(h/11)
          if counter1==3:
              yy=yy+6
          counter1=counter1+1

        xx=e+2
        e=e+w
        if x==7:
            e=e-math.ceil(w/11)
        if counter2==4 or counter2==7:
            xx=xx+6
        counter2=counter2+1

DividImage()
        
