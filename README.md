# Transcript_Readeer_2_Methods
A School Transcript Reader which gives data in a .csv file.

<h2>Method 1:</h2>
So basically lets go for method 1 which is using Google's Tesseract technology to convert image to text:<br>
1)You will need to download Tesseract setup file over here:<br>
  https://github.com/UB-Mannheim/tesseract/wiki<br>
2)You will need to download the Method 1 file<br>
3)Replace the "vazni" in tess.pytesseract.tesseract_cmd=r"C:\Users\vazni\AppData\Local\Programs\Tesseract-OCR\tesseract.exe" with your<br>
  username therefore it will be tess.pytesseract.tesseract_cmd=r"C:\Users\<USERNAME>\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"<br>
4)You are good to go!!!!!<br>
<br>
The main problem with this output is that it is not ordered and thus the data which you get will need to be refined alot using different<br>
modules like regex etc. This is why I have chosen "Method 2" as my means of getting ordered data from a transcript.<br>


