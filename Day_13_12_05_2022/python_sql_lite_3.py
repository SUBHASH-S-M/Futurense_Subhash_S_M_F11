import sqlite3
#fucntion without argument
def My_DB_execution():
    connection=sqlite3.connect("python.db")
    query="""create table student(id int,"name" text)"""
    execution=connection.execute(query)
    connection.commit()
    connection.close()

#fucntion without parameters
def My_DB_execution(table_name,db_name):
    connection=sqlite3.connect(db_name)
    query=f"""create table {table_name}(id int,"name" text)"""
    execution=connection.execute(query)
    connection.commit()
    connection.close()
#My_DB_execution("sports",'dhoni.db')

#fucntion without defualt arguments
def My_DB_execution(table_name,db_name='ipl.db'):
    connection=sqlite3.connect(db_name)
    query=f"""create table {table_name}(id int,"name" text)"""
    execution=connection.execute(query)
    connection.commit()
    connection.close()
#My_DB_execution("sports")



# defualt arguments can be in right side or complete pameters should be in default
#fucn(tname="sds",db) not corrrect function

def My_DB_execution(*col_name,table_name="student",db_name='testnew.db'):

    val='('
    for i in col_name:
        val+=i+","
    val=val[:len(val)-1]
    val+=')'
    print(val)
    query=f"""create table {table_name}{val}"""
    print(query)
    try:
        connection=''
        connection = sqlite3.connect(db_name)
        execution=connection.execute(query)
    except Exception as ex:
        print(ex)
    finally:
        if connection!='':
            connection.commit()
            connection.close()
My_DB_execution("id int","roll_num int","name text")

# def My_DB_execution(*col_name,table_name="student",db_name='testnew.db'):
#     connection=sqlite3.connect(db_name)
#     query = f"""create table {table_name}"""
#     for i in col_name:
#         query+=i+","
#     query=query[:len(query)-1]
#     execution=connection.execute(query)
#     connection.commit()
#     connection.close()
# My_DB_execution("id int","roll_num int","name text")
