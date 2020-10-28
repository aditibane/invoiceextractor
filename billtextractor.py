import pytesseract
import cv2
import xlwt
from PIL import Image
from IPython.display import display
import xlwt
import re
import glob
import numpy
import os
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
timepat=re.compile('\d{1,2}\:\d{1,2}\s*(AM|PM|am|pm)*')

datpat4=re.compile('((\d\d)(\s|\/|-)((\w{3})|(\d{2}))(\s|\/|-)(\d{2,4}\s))|(\w{3}(\s|\')\d{2}\s\d{4})')

image = Image.open("C:/Users/HEMANT/Training Data Set/Burger King/1.jpg")
#display(image)
s=pytesseract.image_to_string(image)
    #print("Image ",fc," ",pytesseract.image_to_osd(image))
x=s.splitlines()
datser=re.search(datpat4,s) 
timser=re.search(timepat,s) 
#fprint("\nDate:"+re.search(datpat4,s).group()+"\nTime:"+re.search(timepat,s).group())
datetime=""
datetime+=str(re.search(datpat4,s).group())[:-1] +"  "+str(re.search(timepat,s).group())
#datetime#
#print(datetime)
y=0
if str(x[0]).find("INVOICE")==-1:
    y=0
else:
    y=1
store_name = x[y]
store_address = "".join(x[y+1:y+4])
    
date_keywords = ["Date","Purchase Date","Time"]
invoice_keywords = ["Bill No","Invoice:","Invoice :","Invoice No:","Invoice No :","Invoice No", "ill No"]
invoice_num,amount,date,time = "","","",""
amount_keywords = ["total","Grand Total","SubTotal","Sub Total","Final Amount","Net Payable","otal"]
item_keywords = ["hsn","Item","Items","Qty","hsh"]
item_flag = 0
items = []
date_regex = r'(\d{1,2}/\d{1,2}/\d{1,2})'
for i in range(4,len(x)):
    string = x[i]
    if any(x in string for x in item_keywords):
        item_flag = 1
        continue
    for ext in invoice_keywords:
        if ext in string and invoice_num == "":
            invoice_num = string.replace(ext,"").strip()
    if any(ext1 in string for ext1 in amount_keywords) and amount == "":
        for i in string.lower():
            if i.isdigit() or i==".":
                amount += i
            elif i == " ":
                amount = ""
    else:
            for ext2 in date_keywords: 
                if ext2 in string and date == "":
                    date = string.replace(ext2,"").strip()
                
            if date == "":
                try:
                    date = re.search(date_regex, string).group()
                except AttributeError:
                    try:
                        date = re.search(r'\d{2,4}-\[a-zA-Z]{3}-\d{2,4}', string).group()
                    except AttributeError:
                        date = ""
                    
                try:
                    time = re.search(r'\d{1,2}:\d{1,2}:\d{1,2}', string).group()
                except AttributeError:
                    time = ""
    
            if amount=="" and item_flag == 1:
                string = string.split()
                for i in string:
                    if i.isdigit() == False:
                        items.append(" ".join(string))
                        break
            if amount != "":
                item_flag = 0    

#print(s)
det=xlwt.Workbook()
style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold off',num_format_str='#,##0.00')
ws=det.add_sheet("Details Sheet 1")
ws.write(0,0,'Store Name',style0)
ws.write(0,1,store_name,style0)
ws.write(1,0,'Store Address',style0)
ws.write(1,1,store_address,style0)
ws.write(2,0,'Date and Time of Invoice',style0)
ws.write(2,1,datetime)
ws.write(3,0,'Invoice Number',style0)
ws.write(3,1,str(invoice_num),style0)
ws.write(4,0,'Total Bill Amount',style0)
ws.write(4,1,str(amount),style0)
ws.write(5,0,'Items',style0)
ws.write(5,1,items,style0)
nam=store_name.replace('.',"")
nam2=nam.replace(' ',"")
print(nam2)
det.save(nam+".xls")
fname=""
fname+=store_name+".xls"
comm="start excel.exe "+nam2+".xls"
#os.system(comm)
