import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import tkinter as tk
import mysql.connector
from fun_operativas import *
import time

 

#################################
        
conexion = mysql.connector.connect(
                                    host = 'localhost',
                                    user = 'root',
                                    passwd = '',
                                    database = 'esart'

)

cursor = conexion.cursor()


try:
    comando = f'SELECT * FROM gastos WHERE (dia>10)'
    cursor.execute(comando)
    info = cursor.fetchall()
    print(info)
except mysql.connector.Error as error:
    print(error)
finally:
    conexion.commit()
    cursor.close()
    conexion.close()



# El programa que estoy haciendo es un programa administrativo para dar de alta talleres y tambien dar de alta clientes en dichos talleres, tiene funciones para consultar talleres, eliminar talleres, eliminar cursos, buscar cliente etc etc ahora el problema esta en que quiero llevar un control de gastos pero no se la logica de como hacerlo, ya que el negocio tiene ingresos de los clientes que se inscriben pero tambien hay gastos como, luz, agua, comida, materiales de los talleres etc etc no se como contabilizar eso mes con mes o semana con semana

# Crear la ventana
