import pytesseract
import cv2
import xlwt
from PIL import Image
from IPython.display import display
import xlwt
import re
import glob
import numpy
from google.cloud import vision
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
timepat=re.compile('\d{1,2}\:\d{1,2}\s*(AM|PM|am|pm)*')
#datpat=re.compile('(\d\d\D\D)(((\/*)+(-)*)+(\s)*)((\d\d\D\D)|(\w{1}))(((\/*)+(-)*)+(\s)*)(\d{2,4})')
#imgtemp=Image.open("C:/Users/HEMANT/Training Data Set/Burger King/2.jpg")
#display(imgtemp)
#s=pytesseract.image_to_string(imgtemp)
#print(pytesseract.image_to_string(imgtemp))
#if re
l=[]
X_data = []
fc=0
files = glob.glob ("C:/Users/HEMANT/Training Data Set/*/*.JPG")
for myFile in files:
    print(myFile)
    fc+=1
    image = Image.open(myFile)
    X_data.append (image)
    w=image.size[0]
    h=image.size[1]
    if(w<h):
        s=pytesseract.image_to_string(image)
        x=s.splitlines()
        if l.__contains__(x[1]):
            continue
            print(x[0:4])
        else:
            l.append(x[0:4])
            print(x[0:4])
        print()
        #ser=re.search(timepat,s) 
        #if ser is not None:
         #   print("File Name "+myFile+"\n Store Name:"+x[0]+"\nDate :"+re.search(timepat,s).group())
print('Total images=',fc)