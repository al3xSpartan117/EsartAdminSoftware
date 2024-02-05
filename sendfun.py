import mysql.connector
from index import *

####################### BUSCAR CLIENTE ############################
def extraer_cliente_pcodigo__bd(id):
    conexion = mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor = conexion.cursor()

    try:
        comando = f'SELECT * FROM clientes WHERE codigo = %s'
        cursor.execute(comando, (id,))
        resultado = cursor.fetchall()
        if resultado:
            return resultado
        else:
            return 'NO INFO'
    except mysql.connector.Error as error:
        print(error)
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()

def extraer_nombres_bd():
    conexion = mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor = conexion.cursor()

    try:
        comando = f'SELECT * FROM clientes'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        if resultado:
            return resultado
        else:
            return 'NO INFO'
    except mysql.connector.Error as error:
        print(error)
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()
    


####################### DAR DE ALTA UN CURSO ######################
def envio_bd_curso(info):
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor1 = conexion1.cursor() 
    try:
        comando = "insert into cursos(nombre, costo, dia, mes, anio, horario, disponibilidad, gasto_materiales) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor1.execute(comando, info)
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
        return False
    finally:
        conexion1.commit()
        cursor1.close()
        conexion1.close()


##################################### DAR DE BAJA CURSO ####################################

def eliminar_curso_db(id):
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor1 = conexion1.cursor() 
    
    try:
        sql_delete = "DELETE FROM cursos WHERE codigo = %s"
        cursor1.execute(sql_delete, (id,))
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        conexion1.commit()
        cursor1.close()
        conexion1.close()

    verificar_eliminado = consultar_info_bd(id)
    print(f'VERIFICAR ELIMINADO ES: {verificar_eliminado}')
    if verificar_eliminado == False:#EL QUE RETORNE FALSE SIGNIFICA QUE SI SE ELIMINO PORQUE FUE FALSO EL BUSCAR EL ID
        return True
    else:
        return False


def consultar_info_bd(id):
    id = int(id)
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor1 = conexion1.cursor() 
    try:
        comando = 'SELECT * FROM cursos WHERE codigo = %s'
        cursor1.execute(comando, (id,))
        informacion = cursor1.fetchone()
        if informacion:
            lista_info = []
            for i in informacion:
                lista_info.append(i)
            return lista_info
        else:
            print(f"No se encontró ninguna fila con el ID {id}")
            return False
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
        return 'ERROR'

    finally:
        conexion1.commit()
        cursor1.close()
        conexion1.close()

def eliminar_clientes_curso_bd(id):
    conexion = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='',
                                       database='esart')
    
    cursor = conexion.cursor()
    try:
        comando = f'DELETE FROM clientes WHERE taller = %s'
        cursor.execute(comando, (id,))
    except mysql.connector.Error as error:
        print(error)
        return('ERROR')
    finally:
        cursor.close()
        conexion.commit()
        conexion.close()


    
######################### INSCRIBIR UN CLIENTE ####################
def extraer_talleres_bd(mes, anio):
    print(f'FUNCION EXTRAER TALLERES. mes= {mes} anio= {anio[2:]}')
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor = conexion1.cursor() 

    try:
        # Construir la consulta SQL con la condición de fecha
        consulta_sql = f"SELECT * FROM cursos WHERE mes = '{mes}' AND anio = '{anio[2:]}'"

        # Ejecutar la consulta
        cursor.execute(consulta_sql)

        # Obtener los resultados
        resultados = cursor.fetchall()
        if resultados:
            return resultados
        else:
            return 'NOT FOUND'
    except mysql.connector.Error as error:
        return 'ERROR'
    except ConnectionRefusedError:
        return 'ERROR'
    except Exception:
        return 'ERROR'
    finally:
        conexion1.commit()
        cursor.close()
        conexion1.close()

def extraer_costo_bd(codigo):   #TAMBIEN SE UTILIZA EN CONSULTAR TALLER
    conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    
    cursor = conexion.cursor()
    try:
        comando = f'SELECT costo FROM cursos WHERE codigo = %s'
        cursor.execute(comando, (codigo,))
        costo = cursor.fetchall()
        if costo:
            return costo
        else:
            return 'NOT FOUND'

    except mysql.connector.Error as Error:
        print(Error)
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()


def enviar_cliente_bd(info):
    conexion = mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    
    cursor = conexion.cursor()
    try:
        comando = f'INSERT INTO clientes(nombre, apellido, taller, pagado) values(%s,%s,%s,%s)'
        cursor.execute(comando, info)
    except mysql.connector.Error as Error:
        print(Error)
        return 'ERROR'
    except ConnectionRefusedError:
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()

####################### CONSULTAR TALLER ###################
def extraer_clientes_bd(id):
    conexion = mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor = conexion.cursor()

    try:
        comando = f'SELECT * FROM clientes WHERE taller = %s'
        cursor.execute(comando, (id,))
        resultado = cursor.fetchall()
        
        if resultado:
            return resultado
        else:
            return 'NO INFO'
    except mysql.connector.Error as error:
        print(error)
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()

####################### MODIFICAR PAGADO ########################
        
def modificar_pagado_db(cliente, pago):
    conexion = mysql.connector.connect(host='localhost',
                                       user = 'root',
                                       passwd = '',
                                       database='esart')
    
    cursor = conexion.cursor()

    try:
        comando = f'SELECT pagado FROM clientes where codigo = %s'
        cursor.execute(comando, (cliente,))
        
        info = cursor.fetchall()
        if info:
            pago_actual = float(info[0][0])
            pago_nuevo = float(pago)
            pagado_nuevo = pago_actual+pago_nuevo
            comando2 = f'UPDATE clientes SET pagado = %s WHERE codigo = %s'
            cursor.execute(comando2, (pagado_nuevo,cliente))
            return True

        else:
            print('NO INFO')
    except mysql.connector.Error as error:
        return('ERROR')
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()


################### ENVIAR GASTO O INGRESO ############
def enviar_gasto_ingreso_db(info):
    conexion = mysql.connector.connect( host='localhost',
                                        user='root',
                                        passwd='',
                                        database='esart')

    cursor = conexion.cursor()
    try:
        comando = f'INSERT INTO gastos (descripcion, tipo, monto, area, zona, dia, mes, anio) values (%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(comando, info)
        return True
    except mysql.connector.Error as error:
        print('ERROR AL ENVIAR COMANDO EN enviar_gasto_ingreso_db')
        print(error)
        return False
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()


###########    EXTRAER CLIENTE RECIEN DADO DE ALTA #####
        
def extraer_Codecliente_recien_agregado(nombre, apellido, taller, pago):
    conexion = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='',
                                       database='esart'                                  
    )


    cursor = conexion.cursor()

    try:
        comando = f"SELECT * FROM clientes WHERE nombre = %s AND apellido = %s AND taller = %s AND pagado = %s"
        cursor.execute(comando, (nombre,apellido,taller,pago,))
        resultado = cursor.fetchall()
        if resultado:
            print(resultado[0][0])
            return resultado[0][0]
        else:
            return "NO INFO"
    except mysql.connector.Error as error:
        print(error)
        return 'ERROR'
