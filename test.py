import os
import psycopg2
from psycopg2 import sql
from psycopg2.errors import DuplicateObject, DuplicateDatabase
#Defino nombre de usuario, base de datos y tabla
user = "pancho"
database = "backend"
table = "cotizacion"

default_password = '1234'
database_password = os.getenv('password') or default_password


def inicializar_base_y_usuario():
    #establishing the connection
    conn = psycopg2.connect(database='postgres', user='postgres', password=database_password, host='db', port= '5432')

    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE USER pancho password 'pancho'")
    except DuplicateObject:
        print("el usuario ya estaba creado, no lo creo. Sigo todo ok.")

    try:
        cursor.execute("CREATE DATABASE backend OWNER pancho")
    except DuplicateDatabase:
        print("La DB ya existia, no pasa nada, sigo ok.")

    conn.close()


def conectarse_a_db():
    pass

def insertar_valor(conexion):
    pass

conn = psycopg2.connect(database='backend', user='pancho', password='pancho', host='db', port= '5432')
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()




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