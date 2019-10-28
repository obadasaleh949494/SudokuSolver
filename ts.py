try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


im = Image.open("thres.png")

result = pytesseract.image_to_string(im)

print(result)
