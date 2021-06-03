# Transcript_Reader_2_Methods
A School Transcript Reader which gives data in a .csv or .txt file (stored in the same file after running the code).<br><br>
Note:This repo already contains test files (You can change "Sample_Transcript_1.pdf" to "Sample_Transcript_2.pdf" in the python files for different cases)<br>
<h2>Method 1:</h2>
So basically lets go for Method 1 which is using Google's Tesseract technology to convert image to text:<br>
In order to make this work you will firstly need to convert the pdf to an image either in python or through the internet (I did that through the internet)<br>
Note:(Make sure you run pip install pytesseract in the terminal to install the module)<br>
1)You will need to download Tesseract setup file over here:<br>
  https://github.com/UB-Mannheim/tesseract/wiki<br>
2)You will need to download the Repo<br>
3)Replace the "vazni" in tess.pytesseract.tesseract_cmd=r"C:\Users\vazni\AppData\Local\Programs\Tesseract-OCR\tesseract.exe" <br>with your
  username therefore it will be tess.pytesseract.tesseract_cmd=r"C:\Users\<USERNAME>\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"<br>
4)You are good to go!!!!!<br>
<br>
The main problem with this output is that it is not ordered and thus the data which you get will need to be refined alot using different<br>
modules like regex etc. This is why I have chosen "Method 2" as my means of getting ordered data from a transcript.
<br>
<h2>Method 2:</h2>
Method 2 is much better than Method 1 as I will be obtaining the output in the form of a data frame which is organised to some extent and will need a little refining
I will be using tabula in order to not only get the tables from the pdf file but also to convert them into an organised text file or csv file.<br>
Note:(Make sure that you run pip install tabula-py in the terminal to install the module)<br>
1)You will need to download the Repo<br>
2)You will need to download Java or else you will get a JavaNotFoundError<br>
3)You will need to type "Edit the system environment variables" in the Windows search bar and select it.<br>
4)You will need to click on "Environment Variables" under "Advanced".<br>
5)Under the System Variables click Path and then press the Edit... instead of New. <br>
  Then in the next screen (Edit environment variable for the Path variable) click New and add the address, <br>
  e.g. C:\Program Files (x86)\Java\jre1.8.0_201\bin. Press OK and the Path variable will be appended/updated.<br>
5)You are good to go!!!!!!
<br>
<h2>Please Note:</h2>
This code isnt perfect by any means, it is meant to be refined and used appropriately.<br>
I have done this solely to demonstrate how school transcripts(Either in .pdf or .png formats) can be tabulated by code.<br>
The data will need to be cleaned and refined in order to be presentable 
<br>
<h2>References:</h2>
https://www.youtube.com/watch?v=4DrCIVS5U3Y<br>
https://github.com/UB-Mannheim/tesseract/wiki (To download the tesseract.exe file on windows)<br>
https://towardsdatascience.com/scraping-table-data-from-pdf-files-using-a-single-line-in-python-8607880c750<br>
https://stackoverflow.com/questions/44490203/java-not-found-in-using-tabula-py<br>
