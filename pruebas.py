import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import tkinter as tk
import mysql.connector
from fun_operativas import *
import time
 

#################################
        
# conexion = mysql.connector.connect(
#                                     host = 'localhost',
#                                     user = 'root',
#                                     passwd = '',
#                                     database = 'esart'

# )

# cursor = conexion.cursor()
# datos = (2, 'Astrid', 'Arguelles', '23', '100')

# try:
#     comando = f'INSERT INTO clientes2 (codigo, nombre, apellido, taller, pagado) values (%s,%s,%s,%s,%s)'
#     cursor.execute(comando, datos)
# except mysql.connector.Error as error:
#     print(error)
# finally:
#     conexion.commit()
#     cursor.close()
#     conexion.close()



# El programa que estoy haciendo es un programa administrativo para dar de alta talleres y tambien dar de alta clientes en dichos talleres, tiene funciones para consultar talleres, eliminar talleres, eliminar cursos, buscar cliente etc etc ahora el problema esta en que quiero llevar un control de gastos pero no se la logica de como hacerlo, ya que el negocio tiene ingresos de los clientes que se inscriben pero tambien hay gastos como, luz, agua, comida, materiales de los talleres etc etc no se como contabilizar eso mes con mes o semana con semana

password = '19-18-47-71-85-85-75-25-52-81-80-67-78-70-81'

#encriptador
()