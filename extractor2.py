import pytesseract
import cv2
import xlwt
from PIL import Image
from IPython.display import display
import xlwt
import re
import glob
import numpy
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
timepat=re.compile('\d{1,2}\:\d{1,2}\s*(AM|PM|am|pm)*')
#datpat=re.compile('(\d\d\D\D)(((\/*)+(-)*)+(\s)*)((\d\d\D\D)|(\w{1}))(((\/*)+(-)*)+(\s)*)(\d{2,4})')
#datpat2=re.compile('(\d\d)(\s|\/|-)(\w{3}|\d{2})(\D|\s|\/|-)(\d{2}\d{2})')
#datpat3=re.compile('(\d\d)(\s|\/|-)(\D{3}|\d{2}\D)(\D|\s|\/|-)(\d{2}\d{2})')
#imgtemp=Image.open("C:/Users/HEMANT/Training Data Set/Lyfe by Soul Garden Bistro/1.jpg")
#display(imgtemp)
#s=pytesseract.image_to_string(imgtemp)
print(pytesseract.image_to_string(imgtemp))
#if re
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
        ser=re.search(datpat3,s) 
        if ser is not None:
            print("File Name "+myFile+"\n Store Name:"+x[0]+"\nDate :"+re.search(datpat3,s).group())
print('Total images=',fc)



'''
print(X_data[0].size)
l=X_data[0].size
print(l)
for i in X_data:
    #w=i.size[0]
    #h=i.size[1]
    print(i.size)
    #if(w<h):
    #    s=pytesseract.image_to_string(image)
    #    print("File Name "+myFile+" Time :"+re.search(timepat,s).group())
#w,h=img.size
print(w,h)
w=img.size[0]
print(w)
img=Image.open('8.jpg')
print(img)
display(img)
s=pytesseract.image_to_string(img)
print(s)
#print(s)
x=s.splitlines()
#print(x)
for i in x:
    print(i)
    
#strname=re.compile
stradd=re.compile(r'((\w))(\,)))* )')
'''
'''
timepat=re.compile('\d{1,2}\:\d{1,2}\s*(AM|PM|am|pm)*')
print(re.search(timepat,s).group())
datpat=re.compile('(\d\d\D)(((\/*)+(-)*)+(\s)*)((\d\d\D)+(\w*))(((\/*)+(-)*)+(\s)*)(\d{2,4})')
print(re.search(datpat,s).group())
#print(re.search(re.compile('(\d\d)((\s{0,1})+(-*)+(\/*))((\w{3}))((\s{0,1})+(-*)+(\/*))((\d{2,4})+)'),s).groups())
'''
#datstr=

#print(datstr)
