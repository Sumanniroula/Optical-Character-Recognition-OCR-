try:
    import Image
except ImportError:
    from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


#print(pytesseract.image_to_string(Image.open('a32ae8963d4039d224edf9e83d9bf388.jpg')))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='eng'))
print(pytesseract.image_to_string(Image.open('hindi-letters.gif'), lang='hin'))