
import sendfun

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

############ verificador numero de telefono correcto
def verificadorCel(n):
    if len(n) == 10:
        if solonumeros(n):
            return True
        else:
            return False
    else:
        return False

########### DAR FORMATO A TARJETAS
def formato_a_tarjetas(info):
    info_lista = []
    for i in info:
        lista = list(i)
        x = '-'.join(lista)
        info_lista.append(x)
    return info_lista

########### FUNCION INFORMACION PARA RENDIMIENTO DE TALLER
#VARIEBLE QUE GUARDE TODOS LOS GASTOS DEL TALLER
def informacion_rendimiento(taller):
    from sendfun import extraer_disponibilidad_bd
    from sendfun import extraer_informacion_gastos_db
    monto_total_gastos = extraer_informacion_gastos_db(['taller',taller,'g'])
    monto_total_ingresos = extraer_informacion_gastos_db(['taller',taller,'i'])
    disponibilidad = extraer_disponibilidad_bd(taller)
    print(f'INGRESO ES:{monto_total_ingresos} y el gasto es {monto_total_gastos}')
    try:
        ganancia = monto_total_ingresos-monto_total_gastos
    except TypeError:
        pass
    rendimiento = calcular_porcentaje_rendimiento_taller(monto_total_ingresos, monto_total_gastos)
    return [monto_total_gastos, monto_total_ingresos, ganancia, rendimiento, disponibilidad[0][0]]

def informacion_rendimiento_talleres(info):#Funcion que recibe lista de tuplas con talleres y obtiene el rendimiento de cada taller y lo agrega a la lista rendimientos[]
    rendimientos = []
    for i in info:
        x = informacion_rendimiento(i[0])
        rendimientos.append(x)
    return rendimientos

################ CALCULAR PORCENTAJES DE RENDIMIENTO DE TALLER
def calcular_porcentaje_rendimiento_taller(ingresos, gastos):
    try:
        unoporciento = ingresos/100
        porcentaje_gastos = gastos/unoporciento
        rendimiento_real = 100-porcentaje_gastos
    except ZeroDivisionError:
        return 'NO INFO' #LOS 0s vienen de que no se encontraron gastos ni ingresos en la tabla gastos
    return round(rendimiento_real, 2)

################ DAR FORMATO A LISTA DE TUPLA DE CLIENTES PARA TRANSFERIR EXCEDENTES
def formato_a_clientes(info):
    clientes = []
    for i in info:
        i = list(i)
        c = f'{i[0]}-{i[1]} {i[2]}-{i[3]}'
        clientes.append(c)
    return clientes
################ Calcular el excedente de un cliente
def calcular_excedente(cliente, taller):
    from sendfun import extraer_costo_bd
    from sendfun import extraer_pagosTotal_clientes
    costo = extraer_costo_bd(taller)
    pagado = extraer_pagosTotal_clientes(cliente, taller)
    excedente = float(costo[0][0])-float(pagado)
    return excedente

############### CALCULOS SOBRE RENDIMIENTO DE TALLERES

def calculo_rendimientos_talleres(info):#RECIBIMOS LA LISTA DE TUPLAS QUE RETORNA informacion_rendimientos_talleres()
    #[monto_total_gastos, monto_total_ingresos, ganancia, rendimiento, disponibilidad[0][0]] informacion por tupla
    gastos_total = 0
    ingreso_total = 0
    ganancia_total = 0
    rendimiento_total = 0
    contador_talleres=0
    for i in info: 
        gasto = i[0]
        ingreso = i[1]
        ganancia = i[2]
        rendimiento = i[3]
        gastos_total+=gasto
        ingreso_total+=ingreso
        ganancia_total+=ganancia
        if rendimiento == 'NO INFO':
            contador_talleres-=1
            pass
        else:
            rendimiento_total+=rendimiento
        contador_talleres+=1
    rendimiento_promedio = rendimiento_total/contador_talleres
    return [gastos_total, ingreso_total, ganancia_total, round(rendimiento_promedio, 2)]

###############FUNCION PARA DAR FORMATO A DATOS Y MOSTRARLOS EN EXCEL

def formato_excel_tablas(info, op):
    if op == 'clientes':
        clientes = []
        for i in info:
            dic = {'Codigo':i[0], 'Nombre':i[1], 'Apellido':i[2], 'Taller':i[3], 'Pagado':i[4], 'celular':i[5]}
            clientes.append(dic)
        return clientes
    elif op == 'gastos':
        gastos = []
        for i in info:
            fecha = f'{i[7]}-{i[8]}-{i[9]}'
            dic = {'ID':i[0], 'Descripcion':i[1], 'Tipo':i[2], 'Monto':i[3], 'Metodo':i[4], 'Area':i[5], 'Zona':i[6], 'Fecha':fecha}
            gastos.append(dic)
        return gastos
    elif op == 'cursos':
        gastos = []
        for i in info:
            dic = {'Codigo':i[0], 'Nombre':i[1], 'Apellido':i[2], 'Taller':i[3], 'Pagado':i[4], 'celular':i[5]}
            gastos.append(dic)
        return gastos


def calcular_rendimiento_general(info):
    monto_total_gasto = 0
    monto_total_ingreso = 0
    ganancia_total = 0
    for i in info:
        if i[2] == 'i':
            monto_total_ingreso += i[3]
        elif i[2] == 'g':
            monto_total_gasto += i[3]
        else:
            pass
    ganancia_total=monto_total_ingreso-monto_total_gasto

    if monto_total_ingreso==0:
        return [monto_total_ingreso, monto_total_gasto, ganancia_total, 'CRITICO']
    elif monto_total_gasto==0:
        return [monto_total_ingreso, monto_total_gasto, ganancia_total, 100]
    elif monto_total_gasto == 0 and monto_total_ingreso == 0:
        return ['NO INFO', 'NO INFO', 'N/A', 'N/A']
    else:
        rendimiento = 100-(monto_total_gasto/(monto_total_ingreso/100))
        

    return [monto_total_ingreso, monto_total_gasto, ganancia_total, round(rendimiento, 2)]
    