from sendfun import *
from index import *

def comparador(p1,p2):
    x_len = len(p1)
    y_len = len(p2)
    if x_len > y_len:
        palabra_mas_grande = x_len
    elif y_len > x_len:
        palabra_mas_grande = y_len
    elif x_len == y_len:
        palabra_mas_grande = x_len
    else:
        print('CASO EXTRAÑO AL COMPARAR LAS LONGITUDES DE LOS DATOS PROPORCIONADOS A LA FUNCION COMPARADOR')

    contador = 0
    x = p1.lower()
    y = p2.lower()
    try:
        for i, element in enumerate(x):
            if element == y[i]:
                contador+=1
            else:
                pass
        nivel_coincidencia = contador/(palabra_mas_grande/100)
    except IndexError:
        nivel_coincidencia = contador/(palabra_mas_grande/100)
    if nivel_coincidencia>30:#AQUI SE AJUSTA EL NIVEL DE PRESICION DEL BUSCADOR DE COINCIDENCIAS
        return True
    else:
        return False

    
def buscador_de_coincidencias(info, nombre_in, apellido_in):
    coincidencias = []
    for i in range(0,len(info)):
        coincide_nombre = comparador(info[i][1],nombre_in)
        coincide_apellido = comparador(info[i][2],apellido_in)
        if coincide_nombre == True and coincide_apellido == True:
            coincidencias.append(info[i])
        else:
            pass
    return coincidencias

####funcion para evaluar que solo sean numeros#####
def solonumeros(dato):
    if '.' in dato:
        if dato.replace('.','', 1).isdigit():
            return True
    elif dato.isdigit():
            return True
    elif dato == '':
        return False
    return False
        
########FUNCION ENLISTAR FECHA #################
def enlistar_fecha(fecha_curso_lista, op='cal'):    ###FUNCION PARA DARLE FORMATO A LA FECHA
    if op == 'cal':
        if len(fecha_curso_lista[1]) == 1:   #SE LE DA FORMATO DE 2DIGITOS A DIA EN DADO CASO DE TENER 1 DIGITO
               fecha_curso_lista[1] = f'0{fecha_curso_lista[1]}'
        else:
            pass
        if len(fecha_curso_lista[0]) == 1:   #SE LE DA FORMATO DE 2DIGITOS A MES EN DADO CASO DE TENER 1 DIGITO
            fecha_curso_lista[0] = f'0{fecha_curso_lista[0]}'
        else:
            pass
        return [fecha_curso_lista[1], fecha_curso_lista[0], fecha_curso_lista[2]]
    elif op == 'datetime':
        if len(fecha_curso_lista[1]) == 1:   #SE LE DA FORMATO DE 2DIGITOS A DIA EN DADO CASO DE TENER 1 DIGITO
               fecha_curso_lista[1] = f'0{fecha_curso_lista[1]}'
        else:
            pass
        if len(fecha_curso_lista[0]) == 1:   #SE LE DA FORMATO DE 2DIGITOS A MES EN DADO CASO DE TENER 1 DIGITO
            fecha_curso_lista[0] = f'0{fecha_curso_lista[0]}'
        else:
            pass
        fecha_curso_lista[2] = fecha_curso_lista[2][2:]
        return [fecha_curso_lista[1], fecha_curso_lista[0], fecha_curso_lista[2]]

######FUNCION VERIFICAR CAMPOS VACIOS
def verificar_campos_vacios(campos):
    for i in campos:
        if i == '':
            return False
        else:
            pass
    return True

######FUNCION PARA ELIMINAR LABELS, COMBOBOX, ENTRYS ETC ETC ######
def eliminar_elementos_creados(elementos, inicio=0):
    for i in elementos[inicio:]:
        i.destroy()
    nuevos_elementos = elementos[:inicio]
    print(nuevos_elementos)
    return nuevos_elementos
    

#########FUNCION PARA OBTENER UNA LISTA CON CODIGO Y TALLER
def dar_formato_talleres_lista(info):
    lista_formateada=[]
    for i in info:
        taller = f'{i[0]}-{i[1]}-{i[3]}/{i[4]}/{i[5]}'# 25-taller barro-25/03/2025
        lista_formateada.append(taller)
    return(lista_formateada)

#encriptador
def encriptador(psswr):
    encriptado = []
    encriptado_str = []
    for i in psswr:
        code = ord(i)
        x=code-30
        encriptado.append(x)
    for j in encriptado:
        encriptado_str.append(str(j))
    return '-'.join(encriptado_str)

#desencriptador
def desencriptador(psswr):
    psswr_lista = psswr.split('-')
    desencriptado = []
    for i in psswr_lista:
        x = int(i)+30
        desencriptado.append(chr(x))

    passwr = ''.join(desencriptado)
    return passwr