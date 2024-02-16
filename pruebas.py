import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import tkinter as tk
import mysql.connector
from fun_operativas import *
import time
import pandas as pd
 

#################################
        
# conexion = mysql.connector.connect(
#                                     host = 'localhost',
#                                     user = 'root',
#                                     passwd = '',
#                                     database = 'esart'

# )

# cursor = conexion.cursor()


# try:
#     comando = f'SELECT * FROM gastos WHERE (dia>10)'
#     cursor.execute(comando)
#     info = cursor.fetchall()
#     print(info)
# except mysql.connector.Error as error:
#     print(error)
# finally:
#     conexion.commit()
#     cursor.close()
#     conexion.close()


datos_base_de_datos = [
    {'nombre': 'Juan', 'edad': 30},
    {'nombre': 'María', 'edad': 25},
    {'nombre': 'Pedro', 'edad': 35}
]

# Crea un DataFrame de Pandas
df = pd.DataFrame(datos_base_de_datos)

# Guarda el DataFrame en un archivo Excel
nombre_archivo = 'datos.xlsx'
df.to_excel(nombre_archivo, index=False)

print(f"Archivo Excel '{nombre_archivo}' creado exitosamente.")
