import pytesseract as tess
tess.pytesseract.tesseract_cmd=r"C:\Users\vazni\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
from PIL import Image

img=Image.open("Sample_Transcript_1.png")
text=tess.image_to_string(img)
try: 
    with open("Transcript.txt", "w") as file:
        file.write(text)
except OSError: 
    print('Failed creating the file') 
else: 
    print('File created')
print(text)

