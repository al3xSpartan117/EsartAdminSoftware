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
        comando = "insert into cursos(nombre, costo, dia, mes, anio, horario, disponibilidad) values (%s,%s,%s,%s,%s,%s,%s)"
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
        comando = f'INSERT INTO clientes(nombre, apellido, taller, pagado, celular) values(%s,%s,%s,%s, %s)'
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
def enviar_gasto_ingreso_db(info, op=1):
    conexion = mysql.connector.connect( host='localhost',
                                        user='root',
                                        passwd='',
                                        database='esart')

    cursor = conexion.cursor()
    if op == 1:
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
    elif op == 2:
        try:
            comando = f'INSERT INTO gastos (descripcion, tipo, monto, metodo, area, zona, dia, mes, anio) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
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
    
####### ENVIAR PERSONAL
def enviar_personal_bd(info):
    conexion = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='',
                                       database='esart'
    )

    cursor = conexion.cursor()

    try:
        comando = f'INSERT INTO personal (nombre, apellido, apellido2, privilegios, usuario, psw) VALUES(%s,%s,%s,%s,%s,%s)'
        cursor.execute(comando, info)
        return True
    except mysql.connector.Error as error:
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()

######### EXTRAER USUARIO Y CONTRASENA
def extraer_personal_pverificar(usr):
    conexion = mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor = conexion.cursor()

    try:
        comando = f'SELECT psw, privilegios FROM personal WHERE usuario = %s'
        cursor.execute(comando, (usr,))
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

##########################EXTRAER EMPLEADO####################################
def extraer_personal():
    conexion = mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor = conexion.cursor()

    try:
        comando = f'SELECT codigo, nombre, apellido FROM personal'
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

################ ENVIAR TARJETA
        
def enviar_tarjeta_bd(info):
    conexion = mysql.connector.connect(host='localhost', user='root', passwd='', database='esart')
    cursor = conexion.cursor()

    try:
        comando = f'INSERT INTO tarjetas (titular, digitos, banco, vencimiento) VALUES (%s,%s,%s,%s)'
        cursor.execute(comando, info)
        return True
    except mysql.connector.Error as error:
        print(error)
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()

################# EXTRAER TARJETAS
        
def extraer_tarjetas_bd():
    conexion = mysql.connector.connect(host='localhost', user='root', passwd='', database='esart')
    cursor = conexion.cursor()

    try:
        comando = f'SELECT digitos, banco FROM tarjetas'
        cursor.execute(comando)
        informacion = cursor.fetchall()
        if informacion:
            return informacion
        else:
            return 'NO INFO'
    except mysql.connector.Error as error:
        print(error)
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()

#########EXTRAER INFORMACION GASTOS
def extraer_informacion_gastos_db(info, op=0):
    conexion = mysql.connector.connect(host='localhost', user='root', passwd='', database='esart')
    cursor = conexion.cursor()
    if op == 0:
        try:
            comando = f'SELECT monto FROM gastos WHERE area=%s and zona=%s and tipo=%s'
            cursor.execute(comando, (info))
            informacion = cursor.fetchall()
            print(informacion)
            if informacion:
                total = 0.0
                for i in informacion:
                    total+=float(i[0])
                return total    
            else:
                return 0
        except mysql.connector.Error as error:
            print(error)
            return 'ERROR'
        finally:
            conexion.commit()
            cursor.close()
            conexion.close()

################### EXTRAER DISPONIBILIDAD
            
def extraer_disponibilidad_bd(codigo):   #TAMBIEN SE UTILIZA EN CONSULTAR TALLER
    conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    
    cursor = conexion.cursor()
    try:
        comando = f'SELECT disponibilidad FROM cursos WHERE codigo = %s'
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


########################
def extraer_pagosTotal_clientes(codigo, taller):
    conexion=mysql.connector.connect(host="localhost", 
                              user="root", 
                              passwd="", 
                              database="esart")
    
    cursor = conexion.cursor()
    try:
        comando = f'SELECT monto FROM gastos WHERE descripcion = %s AND area=%s and zona=%s'
        cursor.execute(comando, (codigo,'taller',int(taller)))
        montos = cursor.fetchall()
        if montos:
            montoTotal = 0
            for i in montos:
                montoTotal += i[0]
            return montoTotal
        else:
            return 'NOT FOUND'

    except mysql.connector.Error as Error:
        print(Error)
        return 'ERROR'
    finally:
        conexion.commit()
        cursor.close()
        conexion.close()

#print(extraer_pagos_clientes(17,24))
        
def extraer_cliente_pCelular__bd(cel):
    conexion = mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="esart")
    cursor = conexion.cursor()

    try:
        comando = f'SELECT * FROM clientes WHERE celular = %s'
        cursor.execute(comando, (cel,))
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

def extraer_talleres_rangoFechas(info):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="esart"
    )
    cursor = conexion.cursor()

    # Obtener las fechas de inicio y fin del usuario
    dia_inicio = info[0]
    mes_inicio = info[1]
    anio_inicio = info[2]

    dia_fin = info[3]
    mes_fin = info[4]
    anio_fin = info[5]

    # Construir la consulta SQL
    consulta = ("SELECT * FROM cursos "
            "WHERE STR_TO_DATE(CONCAT(anio, '-', mes, '-', dia), '%Y-%m-%d') "
            "BETWEEN %(inicio)s AND %(fin)s")

# Ejecutar la consulta con los parámetros
    

    try:
        # Ejecutar la consulta SQL con los parámetros de las fechas
        cursor.execute(consulta, {'inicio': f"{anio_inicio}-{mes_inicio}-{dia_inicio}",
                                    'fin': f"{anio_fin}-{mes_fin}-{dia_fin}"})

        # Obtener los resultados
        resultados = cursor.fetchall()

        if resultados:
            return resultados
        else:
            return 'NO INFO'
    except mysql.connector.Error as error:
        print(error)
        return 'ERROR'
    finally:
        # Cerrar cursor y conexión
        conexion.commit()
        cursor.close()
        conexion.close()