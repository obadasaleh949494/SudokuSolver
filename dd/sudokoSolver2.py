from PIL import Image, ImageDraw,ImageFont
import numpy as np
import os
import glob
import cv2
import pytesseract
import math



# def DeleteLines(path):
#     filter = False
#
#
#     img = cv2.imread(path)
#
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray,90,150,apertureSize = 3)
#     kernel = np.ones((3,3),np.uint8)
#     edges = cv2.dilate(edges,kernel,iterations = 1)
#     kernel = np.ones((5,5),np.uint8)
#     edges = cv2.erode(edges,kernel,iterations = 1)
#     cv2.imwrite('canny.jpg',edges)
#     lines=[]
#     lines = cv2.HoughLines(edges,1,np.pi/180,150)
#
#     if lines is None:
#         print('No lines were found')
#         return 0
#
#     if filter:
#         rho_threshold = 15
#         theta_threshold = 0.1
#
#         # how many lines are similar to a given one
#         similar_lines = {i : [] for i in range(len(lines))}
#         for i in range(len(lines)):
#             for j in range(len(lines)):
#                 if i == j:
#                     continue
#
#                 rho_i,theta_i = lines[i][0]
#                 rho_j,theta_j = lines[j][0]
#                 if abs(rho_i - rho_j) < rho_threshold and abs(theta_i - theta_j) < theta_threshold:
#                     similar_lines[i].append(j)
#
#         # ordering the INDECES of the lines by how many are similar to them
#         indices = [i for i in range(len(lines))]
#         indices.sort(key=lambda x : len(similar_lines[x]))
#
#         # line flags is the base for the filtering
#         line_flags = len(lines)*[True]
#         for i in range(len(lines) - 1):
#             if not line_flags[indices[i]]: # if we already disregarded the ith element in the ordered list then we don't care (we will not delete anything based on it and we will never reconsider using this line again)
#                 continue
#
#             for j in range(i + 1, len(lines)): # we are only considering those elements that had less similar line
#                 if not line_flags[indices[j]]: # and only if we have not disregarded them already
#                     continue
#
#                 rho_i,theta_i = lines[indices[i]][0]
#                 rho_j,theta_j = lines[indices[j]][0]
#                 if abs(rho_i - rho_j) < rho_threshold and abs(theta_i - theta_j) < theta_threshold:
#                     line_flags[indices[j]] = False # if it is similar and have not been disregarded yet then drop it now
#
#     print('number of Hough lines:', len(lines))
#
#     filtered_lines = []
#
#     if filter:
#         for i in range(len(lines)): # filtering
#             if line_flags[i]:
#                 filtered_lines.append(lines[i])
#
#         print('Number of filtered lines:', len(filtered_lines))
#     else:
#         filtered_lines = lines
#
#     for line in filtered_lines:
#         rho,theta = line[0]
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a*rho
#         y0 = b*rho
#         x1 = int(x0 + 1000*(-b))
#         y1 = int(y0 + 1000*(a))
#         x2 = int(x0 - 1000*(-b))
#         y2 = int(y0 - 1000*(a))
#
#         cv2.line(img,(x1,y1),(x2,y2),(255,255,255),2)
#
#     cv2.imwrite('FirstProcessing.png',img)
#     return len(lines)
#
#     #divide image to 81 image and store them
# def improveImage ():
#
#     # Read image with opencv
#     img = cv2.imread('FirstProcessing.png')
#     # Convert to gray
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # Apply dilation and erosion to remove some noise
#     kernel = np.ones((1, 1), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)
#
#     # Write image after removed noise
#     cv2.imwrite("removed_noise.png", img)
#
#     #  Apply threshold to get image with only black and white
#     img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 29, 2)
#
#      # Write the image after apply opencv to do some ...
#     cv2.imwrite("SecondProcessing.png", img)
#
#         #divid image to 81 image
# def DividImage():
#     im = cv2.imread('SecondProcessing.png')
#     imm=Image.open('SecondProcessing.png')
#     img=[]
#     imgwidth, imgheight =imm.size
#     width=imgwidth/9
#     height=imgheight/9
#     w=math.floor(width)
#     h=math.floor(height)
#     rr=w/9
#     r=math.ceil(rr)
#     cc=h/9
#     c=math.ceil(cc)
#     xx=4
#     yy=3
#     e=w
#     ee=h
#     counter1=1
#     counter2=1
#     for x in range (9):
#         yy=4
#         ee=h
#         for y in range ( 9):
#           img=im[xx:e,yy:ee]
#           name="cropped"+str(x)+str(y)+".png"
#           cv2.imwrite(name , img)
#           yy=ee+2
#           ee=ee+h
#           if counter1==3:
#               yy=yy+6
#           counter1=counter1+1
#
#         xx=e+2
#         e=e+w
#         if counter2==3:
#             xx=xx+6
#         counter2=counter2+1
#
#         # read data from image
#
# def ImageData():
#     string=''
#     try:
#         import Image
#     except ImportError:
#         from PIL import Image
#     import pytesseract
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#     for x in range (9):
#         for y in range (9):
#             name="cropped"+str(x)+str(y)+".png"
#
#             read = cv2.imread(name)
#             result = pytesseract.image_to_string(read, lang='eng', boxes=False, config='--psm 10 --eom 1 -c tessedit_char_whitelist=123456789')
#             print(result)
#             if not result:
#                 string=string+'0'
#             else:
#                 string=string+result
#
#     return string
#
# def MARGEE(A, B):
#     return [a+b for a in A for b in B]
# digits='123456789'
# rows='ABCDEFGHI'
# cols=digits
# sqs= MARGEE(rows, cols)
#
# Clist = ([MARGEE(rows, c) for c in cols] + [MARGEE(r, cols) for r in rows] +
#             [MARGEE(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
#
# units=dict((s,[u for u in Clist if s in u])for s in sqs)
# peers=dict((s,set(sum(units[s],[]))-set([s]))for s in sqs)
#
# def ParseGrid(grid):
#
#     values=dict((s,digits)for s in sqs)
#     for s,d in GridValues(grid).items():
#         if d in digits and not Assign(values,s,d):
#             return False
#     return values
#
#
# def GridValues(grid):
#
#     chars=[c for c in grid if c in digits or c in '0']
#     assert len(chars) == 81
#     return dict(zip(sqs, chars))
#
# def Assign(values,s,d):
#
#     other_values=values[s].replace(d,'')
#     if all(Remove(values,s,d2) for d2 in other_values):
#         return values
#     else:
#         return False
#
# def Remove(values,s,d):
#     if d not in values[s]:
#         return values
#     values[s]=values[s].replace(d,'')
#     if len(values[s])==0:
#         return False
#     elif len(values[s])==1:
#         d2=values[s]
#         if not all(Remove(values,s2,d2) for s2 in peers[s]):
#             return False
#     for u in units[s]:
#         dplaces=[s for s in u if d in values[s]]
#         if len(dplaces) == 0:
#             return False
#         elif len(dplaces) == 1:
#             if not Assign(values,dplaces[0],d):
#                 return False
#     return values
# def display(values):
#     ##width = 1+max(len(values[s]) for s in sqs)
#     ##line = '+'.join(['-'*(width*3)]*3)
#     res=[]
#     for r in rows:
#         ##print (''.join(values[r+c].center(width)+('' if c in '' else '')
#                       ##for c in cols))
#         ##if r in '': print ('')
#         ##print(''.join(values[r+c]for c in cols))
#         for c in cols:
#             res.append(''.join(values[r+c]))
#         ##for o in res:
#             ##print(''.join(res[o]))
#             ##print(len(res))
#
#     ##print
#     ##print (res[10])
#     lii=''.join(res)
#     return lii
#
# def solve(grid): return search(ParseGrid(grid))
#
# def search(values):
#     if values is False:
#         return False
#     if all(len(values[s]) == 1 for s in sqs):
#         return values
#     n,s = min((len(values[s]), s) for s in sqs if len(values[s]) > 1)
#     return some(search(Assign(values.copy(), s, d))
# 		for d in values[s])
#
# def some(seq):
#     for e in seq:
#         if e: return e
#     return False
#
#
#
# ###
#
#
# def EmptyCell(st):
#     arr=[]
#     for ind in range(81):
#         if st[ind]=='0':
#             arr.append(ind)
#     return arr
#
# # building the image
# def BuildImage (string,arr ):
#     if len(string) <81 :
#         print('the numbers less than 81 numbers')
#         return
#     img = Image.new('RGB', (550, 550), color = (255, 255, 255))
#
#     d = ImageDraw.Draw(img)
#     counter1=61
#     counter2=1
#     c1=1
#     c2=61
#     xx=0
#     f = ImageFont.truetype("arial.ttf", 30)
#     for xx in range(9):
#         c1=1
#         for yy in range (549):
#             if xx== 5 or xx==2:
#                 d.text((c1,c2-1), "_", fill=(0,0,0))
#                 d.text((c1,c2-2), "_", fill=(0,0,0))
#             d.text((c1,c2), "_", fill=(0,0,0))
#             c1=c1+1
#             yy=yy+1
#         c2=c2+61
#         xx=xx+1
#     for x in range(9):
#         counter2=1
#         for y in range (549):
#             if x== 5 or x==2:
#                 d.text((counter1-1,counter2), "|", fill=(0,0,0))
#                 d.text((counter1-2,counter2), "|", fill=(0,0,0))
#
#             d.text((counter1,counter2), "|", fill=(0,0,0))
#             counter2=counter2+1
#             y=y+1
#         counter1=counter1+61
#         x=x+1
#     w=30
#     h=30
#     i=0
#
#     for a in range (9):
#         w=30
#         for b in range (9):
#             if i in arr:
#                 print ('')
#                 d.text((w,h), string[i],fill=(255,0,0),font=f,)
#             else:
#                 d.text((w,h), string[i],fill=(0,0,0),font=f,)
#             i=i+1
#             w=w+61
#         h=h+61
#
#     img.save('solution.png')
#
# #DeleteLines('sodo1.png')
# #improveImage()
# #DividImage()
# st=ImageData()
# print(EmptyCell(st) )
# str=display(solve(st))
# print(str)
#
#
#
#
im = cv2.imread('C:/Users/hamza/Desktop/appliedProject/asd.jpg')
imm=Image.open('C:/Users/hamza/Desktop/appliedProject/asd.jpg')
img=[]
imgwidth, imgheight =imm.size
print (imgheight,imgwidth)
h,w,s=im.shape
print(h,w)
