import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mundolibre",
        database="prueba"
    )
    if conexion.is_connected():
        print("Conexion exitosa a la base de datos 'prueba' usando Python!")
        conexion.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
