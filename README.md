# Extracting data from bills/invoices

Packages used:

 pytesseract – For extracting text from images and perform OCR operations

 tesseract-OCR – Tesseract is an optical character recognition engine for various operating systems. It is free software, released under the Apache License, Version 2.0.

 regex – To identify patterns in text.

 xlwt – generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.

 opencv –openCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

```bash
pip install tesseract
pip install opencv
pip install xlwt 
pip install regex
```




Extract neccessary information from bill/invoice.

This project extracts Store name, Store address, Date and time, Invoice number, Total Bill Amount and Items from a given bill/invoice image.

Segmentation is used for each required field in the bill using semantic segmentation technique.

## Project Desciption
It takes the input of bill/invoice as jpeg image and extracts the data from it and then produces the output in a spreadsheet.
The program initially extracts the text from the image of invoice/bill and then the from the extracted text in various groups of text patterns
or text groups are categorized into various categories like Store name, Store address, Date and time, Invoice number, Total Bill Amount and Items.
The patterns of the text categories are identified using regex format.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
