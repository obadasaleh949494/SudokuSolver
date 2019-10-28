from PIL import Image
import pytesseract
import setuptools
im = Image.open("Untitled.png")

text = pytesseract.image_to_string(im,lang='eng')

print(text)
