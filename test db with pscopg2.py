import os
import psycopg2
from psycopg2 import sql

#Defino nombre de usuario, base de datos y tabla
user = "pancho"
database = "backend"
table = "cotizacion"

default_password = '1234'
database_password = os.getenv('password') or default_password
#establishing the connection
conn = psycopg2.connect(database='postgres', user='postgres', password=database_password, host='db', port= '5432')

conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


#Verify if the User is created:
sqlu = '''SELECT rolname FROM pg_roles'''
cursor.execute(sqlu)
resultrole = cursor.fetchall()
print(f"the existing users are: {resultrole}")

if  (user,) in resultrole:
    print(f"User exist. Connecting to DataBase as {user} and verifying next step")
    conn.close()
    conn = psycopg2.connect(database='postgres', user=user, password=database_password, host="db", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    print(f"User exist, closing the connection as {user}, verifying next step")
    conn.close()
    conn = psycopg2.connect(database='postgres', user='postgres', password=database_password, host='db', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
else:
    print(f"Creating the user called {user}, and connecting to the DataBase as that {user}")
    cursor.execute(
        sql.SQL("CREATE USER {user} PASSWORD {default_password}").format(
        user=sql.Identifier(user),
        default_password=sql.Literal(default_password)))
    print(f"User {user} Created, now connecting to the DataBase as {user}")
    conn.close()
    conn = psycopg2.connect(database='postgres', user=user, password=database_password, host="db", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    print(f"User created, closing the connection as {user}, verifying next step")
    conn.close()
    conn = psycopg2.connect(database='postgres', user='postgres', password=database_password, host='db', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()




#____________________de aca para arriba ANDA____________________________________________________________________



#Preparing query to create a database
sqldb = '''SELECT datname FROM pg_database'''
cursor.execute(sqldb)
database_exist = cursor.fetchall()
print(f"the existing data base are: {database_exist}")
# Verify if I need to create the database or not.
# if <>
# else:
#Creating a database

if  (database,) in database_exist:
    print(f'DataBase exist. Connecting to DataBase named {database} as {user}')
    conn.close()
    conn = psycopg2.connect(database=database, user=user, password=database_password, host="db", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
else:
    print(f'Creating the DataBase called {database}, and connecting to the DataBase named {database} like {user}')
    cursor.execute(
        sql.SQL("CREATE DATABASE {database} OWNER {user}").format(
        database=sql.Identifier(database),
        user=sql.Literal(user)))
    print(f'''{database} Created, now connecting to the {database} as {user}
    
    CONECTED''')
    conn.close()
    conn = psycopg2.connect(database=database, user=user, password=database_password, host="db", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()

    sqlu = '''SELECT rolname FROM pg_roles'''
    cursor.execute(sqlu)
    resultrole = cursor.fetchall()
    sqldb = '''SELECT datname FROM pg_database'''
    cursor.execute(sqldb)
    database_exist = cursor.fetchall()
    #print(f"{resultrole} {database_exist}")
    if (user,) in resultrole and (database,) in database_exist:
        print('Everything is allright, work as you wish the database')
    else:
        print("Error, please check your code. Bye")





#print("Database created successfully........")
#
#
#
#
#
#
#
#
#
## Verify if I need to create the table or not.
## if <>:
## else:
##Creating the table
#sql = '''CREATE TABLE cotizacion(
#   Moneda VARCHAR(30),
#   CotizacionDolar INT
#);'''
#cursor.execute(sql)
#
## try:
#
## Generate a random value for the cotization.
## loop:
##     wait(1m)
##     cotizacion = random()
##     cursor.execute('insert into cotizacion values...')
#
## except...
##     close connection.
#
##Closing the connection
#conn.close()
#