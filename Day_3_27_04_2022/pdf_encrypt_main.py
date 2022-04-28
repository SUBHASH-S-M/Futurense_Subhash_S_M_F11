# importing required modules
import PyPDF2
import os
from python_date_extraction import time_now
from python_mail_masking_smtp import *
from pyhton_encryption import *
import time
from datetime import datetime
import tkinter
import pandas as pd
from tkinter import filedialog
from tkinter import *

#Tkinter window withdrawl
root = Tk()
root.withdraw()
# folder selection
folder_selected = filedialog.askdirectory()
files_in_dir=os.listdir(folder_selected)
#print(files_in_dir)
arr=[]
for file_name in files_in_dir:
    temp=[]
    out=PyPDF2.PdfFileWriter()
    #print(file_name)
    if file_name[-3:] != "pdf":
        continue
    try:
        # creating a pdf file object
        pdfFileObj = open(file_name, 'rb')
    except:
        #print("The file is already encrypted visit the log for more details")
        continue

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted:
        continue
    else:
        print("Not encrypted")

    # printing number of pages in pdf file
    num_of_pages=pdfReader.numPages
    for each_page in range(num_of_pages):
        page=pdfReader.getPage(each_page)
        out.addPage(page)
    current_time = datetime.now()
    format = "%y_%b_%d_%H_%M_%S"
    current_time = datetime.strftime(current_time, format)
    password=encrypt_message(file_name)
    out.encrypt(password)
    decrypted_filename=file_name[0]+password+".pdf"

    with open(decrypted_filename,"wb") as out_file:
        out.write(out_file)
    statinfo = os.stat(decrypted_filename)
    today = datetime.now()
    temp.extend([file_name,num_of_pages,statinfo.st_size,
                time_now(today),current_time
                ,password])
    arr.append(tuple(temp))
    time.sleep(1)
    # closing the pdf file object
    pdfFileObj.close()
print(arr)
import mysql.connector
mydb = mysql.connector.connect(
  port=3306,
  user="root",
  password="12345",database='db_encrypt'
)
mycursor = mydb.cursor()
#print(arr)
sql = "INSERT INTO logfiles (File_Name ,Number_of_pages ,Size_of_file ,Date ,Enc_time ,Password)VALUES (%s, %s,%s, %s,%s, %s)"
val = arr
mycursor.executemany(sql, val)
mydb.commit()




