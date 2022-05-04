# import mysql.connector
# conn = mysql.connector.connect (port=3306,user='root', password='12345',buffered=True)
# cursor = conn.cursor()
# databases = ("show databases")
# cursor.execute(databases)
# db_names=[]
# for (databases) in cursor:
#     print(databases)
#     db_names.append(databases[0])

# table tsting
mydb = mysql.connector.connect(
        port=3306,
        user="root",
        password="12345", database=option
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    tb_names = ['None']
    for table_name in cursor:
        tb_names.append(table_name)
