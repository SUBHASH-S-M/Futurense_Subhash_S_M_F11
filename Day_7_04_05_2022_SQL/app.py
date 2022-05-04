import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
conn = mysql.connector.connect (port=3306,user='root', password='12345',buffered=True)
cursor = conn.cursor()
databases = ("show databases")
cursor.execute(databases)

db_names=['None']
for (databases) in cursor:
    #print(databases)
    db_names.append(databases[0])
option = st.selectbox('Choose the DB you want',tuple(db_names))
st.write('You selected:', option)

if(option=='None'):
    option='sakila'
mydb = mysql.connector.connect(port=3306,user="root",password="12345", database=option)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
tb_names = ['None']
for table_name in mycursor:
    tb_names.append(table_name[0])
dropdown = st.selectbox('Choose the table you want', tuple(tb_names))
record="None"
col_name=["None"]
if(option!='None' and dropdown!='None'):
    sql_select_Query = "select * from {}".format(dropdown)

    mycursor.execute(sql_select_Query)
    # get all records
    records = mycursor.fetchall()
    #print("Total number of rows in table: ", mycursor.rowcount)

    #print("\nPrinting each row")

    sequence = mycursor.column_names
    col_name.append("ALL")
    for i in sequence:
        col_name.append(i)

col_down = st.selectbox('Choose the coloumns u want',tuple(col_name))
val=False
#print(option,dropdown,col_down)
if(col_down=='ALL'):

    query="SELECT * FROM {}".format(dropdown)
    mycursor.execute(query)
    val = mycursor.fetchall()
# print(val)

elif(col_down!='None' and col_down!='ALL'):
    query = "SELECT {} FROM {}".format(col_down,dropdown)
    mycursor.execute(query)
    val= mycursor.fetchall()
if(col_down=='ALL'):
    col_n=col_name[2:]
    re=[]
    for i in val:

        for j in range(len(col_n)):
            print(col_n[j], ":", i[j])
        print()

else:
    col_n=col_down[:]
    #print(col_n)
    #print(val)
    for i in val:
        print(col_n, ":", i[0])
        print()
df = pd.DataFrame(val,columns=(col_n))

st.table(df)






