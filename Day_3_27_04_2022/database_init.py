import mysql.connector
mydb = mysql.connector.connect(
  port=3306,
  user="root",
  password="12345",database='db_encrypt'
)
import pdf_encrypt_main
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
flag=False
for x in mycursor:
  if(x[0]=='DB_Encrypt'.lower()):
    flag=False
    #mycursor.execute("use db_encrypt")

if(flag):
  mycursor.execute("CREATE DATABASE DB_Encrypt")
  query_table='''CREATE TABLE Logfiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    File_Name VARCHAR(255),
    Number_of_pages int,
    Size_of_file int,
    Date date,
    Enc_time time,
    Password varchar(200))'''
  mycursor.execute(query_table)

import pdf_encrypt_main.py

mydb.commit()
mydb.close()

