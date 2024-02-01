import mysql.connector
from sendfun import *
from fun_operativas import *
from tkinter import *
from tkinter import ttk 
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar
from tkinter import messagebox

psw = '1234'

def ventana_ingresar_gasto_ingreso(): 
    #SUELDOS
    #SERVICIOS
    #COMIDA
    #MOBILIARIO
    def boton_enviar_funcion(op):
        global elementos_creados
        if op == 'extra':
            fecha = elementos_creados[6].get_date()
            fecha_lista = fecha.split('/')
            fecha_formateada = enlistar_fecha(fecha_lista)
            info = (elementos_creados[2].get(), 'i', elementos_creados[4].get(), op, 'extra', fecha_formateada[0], fecha_formateada[1], fecha_formateada[2])
            if verificar_campos_vacios(info) and solonumeros(elementos_creados[4].get()):
                estado_envio = enviar_gasto_ingreso_db(info)
                if estado_envio == True:
                    print('SE HA ENVIADO LA INFORMACION')
                    indicador = ttk.Label(frm, text='ENVIADO', background='GREEN')
                    indicador.grid(column=1, row=5)
                    frm.after(2000,lambda: indicador.grid_remove())
                else:
                    messagebox.showinfo('ERROR', 'Excepcion en boton_enviar_funcion(op)-> estado_envio=enviar_gasto_ingreso_db(info)')
            else:
                messagebox.showinfo('ERROR', 'EXISTE ERROR EN CAMPOS')
        elif op == 'taller':
            fecha = elementos_creados[6].get_date()
            fecha_lista = fecha.split('/')
            fecha_formateada = enlistar_fecha(fecha_lista)
            zona_completa = elementos_creados[14].get()
            zona_completa_lista = zona_completa.split('-')
            info = (elementos_creados[2].get(), 'g', elementos_creados[4].get(), op, zona_completa_lista[0], fecha_formateada[0], fecha_formateada[1], fecha_formateada[2])
            if verificar_campos_vacios(info) and solonumeros(elementos_creados[4].get()):
                estado_envio = enviar_gasto_ingreso_db(info)
                if estado_envio == True:
                    print('SE HA ENVIADO LA INFORMACION')
                    indicador = ttk.Label(frm, text='ENVIADO', background='GREEN')
                    indicador.grid(column=1, row=7)
                    frm.after(2000,lambda: indicador.grid_remove())
                else:
                    messagebox.showinfo('ERROR', 'Excepcion en boton_enviar_funcion(op)-> estado_envio=enviar_gasto_ingreso_db(info)')
            else:
                messagebox.showinfo('ERROR', 'EXISTE ERROR EN CAMPOS')
        
        elif op == 'mtnmto':
            fecha = elementos_creados[6].get_date()
            fecha_lista = fecha.split('/')
            fecha_formateada = enlistar_fecha(fecha_lista)
            info = (elementos_creados[2].get(), 'g', elementos_creados[4].get(), op, 'mtnmto', fecha_formateada[0], fecha_formateada[1], fecha_formateada[2])
            if verificar_campos_vacios(info) and solonumeros(elementos_creados[4].get()):
                estado_envio = enviar_gasto_ingreso_db(info)
                if estado_envio == True:
                    print('SE HA ENVIADO LA INFORMACION')
                    indicador = ttk.Label(frm, text='ENVIADO', background='GREEN')
                    indicador.grid(column=1, row=5)
                    frm.after(2000,lambda: indicador.grid_remove())
                else:
                    messagebox.showinfo('ERROR', 'Excepcion en boton_enviar_funcion(op)-> estado_envio=enviar_gasto_ingreso_db(info)')
            else:
                messagebox.showinfo('ERROR', 'EXISTE ERROR EN CAMPOS')
        elif op == 'servicio':
            fecha = elementos_creados[6].get_date()
            fecha_lista = fecha.split('/')
            fecha_formateada = enlistar_fecha(fecha_lista)
            info = (elementos_creados[2].get(), 'g', elementos_creados[4].get(), op, elementos_creados[8].get().lower(), fecha_formateada[0], fecha_formateada[1], fecha_formateada[2])
            if verificar_campos_vacios(info) and solonumeros(elementos_creados[4].get()):
                estado_envio = enviar_gasto_ingreso_db(info)
                if estado_envio == True:
                    print('SE HA ENVIADO LA INFORMACION')
                    indicador = ttk.Label(frm, text='ENVIADO', background='GREEN')
                    indicador.grid(column=1, row=5)
                    frm.after(2000,lambda: indicador.grid_remove())
                else:
                    messagebox.showinfo('ERROR', 'Excepcion en boton_enviar_funcion(op)-> estado_envio=enviar_gasto_ingreso_db(info)')
            else:
                messagebox.showinfo('ERROR', 'EXISTE ERROR EN CAMPOS')
        elif op == 'alimento':
            fecha = elementos_creados[6].get_date()
            fecha_lista = fecha.split('/')
            fecha_formateada = enlistar_fecha(fecha_lista)
            info = (elementos_creados[2].get(), 'g', elementos_creados[4].get(), op, 'alimento', fecha_formateada[0], fecha_formateada[1], fecha_formateada[2])
            if verificar_campos_vacios(info) and solonumeros(elementos_creados[4].get()):
                estado_envio = enviar_gasto_ingreso_db(info)
                if estado_envio == True:
                    print('SE HA ENVIADO LA INFORMACION')
                    indicador = ttk.Label(frm, text='ENVIADO', background='GREEN')
                    indicador.grid(column=1, row=5)
                    frm.after(2000,lambda: indicador.grid_remove())
                else:
                    messagebox.showinfo('ERROR', 'Excepcion en boton_enviar_funcion(op)-> estado_envio=enviar_gasto_ingreso_db(info)')
            else:
                messagebox.showinfo('ERROR', 'EXISTE ERROR EN CAMPOS')
        elif op == 'mobiliario':
            fecha = elementos_creados[6].get_date()
            fecha_lista = fecha.split('/')
            fecha_formateada = enlistar_fecha(fecha_lista)
            info = (elementos_creados[2].get(), 'g', elementos_creados[4].get(), op, 'mobiliario', fecha_formateada[0], fecha_formateada[1], fecha_formateada[2])
            if verificar_campos_vacios(info) and solonumeros(elementos_creados[4].get()):
                estado_envio = enviar_gasto_ingreso_db(info)
                if estado_envio == True:
                    print('SE HA ENVIADO LA INFORMACION')
                    indicador = ttk.Label(frm, text='ENVIADO', background='GREEN')
                    indicador.grid(column=1, row=5)
                    frm.after(2000,lambda: indicador.grid_remove())
                else:
                    messagebox.showinfo('ERROR', 'Excepcion en boton_enviar_funcion(op)-> estado_envio=enviar_gasto_ingreso_db(info)')
            else:
                messagebox.showinfo('ERROR', 'EXISTE ERROR EN CAMPOS')
        else:
            messagebox.showinfo('ERROR', 'Error en variable op boton_enviar_funcion(op)')
    

    def limpiar_bloquear_combobox(event): #FUNCION PARA QUE EL COMBOBOX DE SELECCIONAR TALLER SE LIMPIE EN CASO DE SELECCIONAR OTRA FECHA
        global elementos_creados
        elementos_creados[14].config(state='disable')
        elementos_creados[14].set('')
    def comando_boton_buscar():#FUNCION DE LA PARTE DE ELEGIR TALLER AL QUE SE LE DARA DE ALTA UN GASTO
        mes = elementos_creados[11].get()
        anio = elementos_creados[12].get()
        mes_en_numero = {'Enero':'01', 
                 'Febrero':'02',
                 'Marzo':'03',
                 'Abril':'04',
                 'Mayo':'05',
                 'Junio':'06',
                 'Julio':'07',
                 'Agosto':'08',
                 'Septiembre':'09',
                 'Octubre':'10',
                 'Noviembre':'11',
                 'Diciembre':'12',}
        resultado = extraer_talleres_bd(mes_en_numero[mes], anio)
        if resultado == 'NOT FOUND':
            messagebox.showinfo('ALERTA', 'NO SE ENCONTRO INFORMACION')
        elif resultado == 'ERROR':
            messagebox.showinfo('ERROR', 'ERROR EN BASE DE DATOS extraer_talleres_bd')
        else:
            talleres_formateados = dar_formato_talleres_lista(resultado)
            elementos_creados[14].config(state='normal', values=talleres_formateados)
            

####SE DESPLIEGAN LAS OPCIONES DEPENDIENDO DE LO ELEGIDO EN EL CBOXSECUNDARIO
            
    
    def desplegar_opciones_alimentos():
        global elementos_creados
        op = 'alimento'
        label_descripcion = ttk.Label(frm, text='DESCRIPCION:')
        label_descripcion.grid(column=0, row=2)
        elementos_creados.append(label_descripcion)#1 elementos creados
        entry_descripcion = ttk.Entry(frm, width=30)
        entry_descripcion.grid(column=1,row=2)
        elementos_creados.append(entry_descripcion)#2 elementos creados
        label_monto = ttk.Label(frm, text='MONTO:')
        label_monto.grid(column=0, row=3)
        elementos_creados.append(label_monto)#3 elementos creados
        entry_monto = ttk.Entry(frm, width=30)
        entry_monto.grid(column=1,row=3)
        elementos_creados.append(entry_monto)#4 elementos creados
        label_fecha = ttk.Label(frm, text='Fecha')
        label_fecha.grid(column=0, row=4)
        elementos_creados.append(label_fecha)#5 elementos creados
        fecha = datetime.now()
        cal = Calendar(frm, selectmode="day", year=fecha.year, month=fecha.month, day=fecha.day)
        cal.grid(column=1, row=4)
        elementos_creados.append(cal)#6 elementos creados
        boton_enviar = ttk.Button(frm, text='ENVIAR', command=lambda x=op: boton_enviar_funcion(op))
        boton_enviar.grid(column=0, row=5)
        elementos_creados.append(boton_enviar)#7 elementos creados

    def desplegar_opciones_mobiliario():
        global elementos_creados
        op = 'mobiliario'
        label_descripcion = ttk.Label(frm, text='DESCRIPCION:')
        label_descripcion.grid(column=0, row=2)
        elementos_creados.append(label_descripcion)#1 elementos creados
        entry_descripcion = ttk.Entry(frm, width=30)
        entry_descripcion.grid(column=1,row=2)
        elementos_creados.append(entry_descripcion)#2 elementos creados
        label_monto = ttk.Label(frm, text='MONTO:')
        label_monto.grid(column=0, row=3)
        elementos_creados.append(label_monto)#3 elementos creados
        entry_monto = ttk.Entry(frm, width=30)
        entry_monto.grid(column=1,row=3)
        elementos_creados.append(entry_monto)#4 elementos creados
        label_fecha = ttk.Label(frm, text='Fecha')
        label_fecha.grid(column=0, row=4)
        elementos_creados.append(label_fecha)#5 elementos creados
        fecha = datetime.now()
        cal = Calendar(frm, selectmode="day", year=fecha.year, month=fecha.month, day=fecha.day)
        cal.grid(column=1, row=4)
        elementos_creados.append(cal)#6 elementos creados
        boton_enviar = ttk.Button(frm, text='ENVIAR', command=lambda x=op: boton_enviar_funcion(op))
        boton_enviar.grid(column=0, row=5)
        elementos_creados.append(boton_enviar)#7 elementos creados

    def desplegar_opciones_taller():
        global elementos_creados_taller
        global elementos_creados
        op = 'taller'
        label_descripcion = ttk.Label(frm, text='DESCRIPCION:')
        label_descripcion.grid(column=0, row=2)
        elementos_creados.append(label_descripcion)#1 elementos creados
        entry_descripcion = ttk.Entry(frm, width=30)
        entry_descripcion.grid(column=1,row=2)
        elementos_creados.append(entry_descripcion)#2 elementos creados
        label_monto = ttk.Label(frm, text='MONTO:')
        label_monto.grid(column=0, row=3)
        elementos_creados.append(label_monto)#3 elementos creados
        entry_monto = ttk.Entry(frm, width=30)
        entry_monto.grid(column=1,row=3)
        elementos_creados.append(entry_monto)#4 elementos creados
        label_fecha = ttk.Label(frm, text='Fecha')
        label_fecha.grid(column=0, row=4)
        elementos_creados.append(label_fecha)#5 elementos creados
        fecha = datetime.now()
        cal = Calendar(frm, selectmode="day", year=fecha.year, month=fecha.month, day=fecha.day)
        cal.grid(column=1, row=4)
        elementos_creados.append(cal)#6 elementos creados
        ##################### AQUI EMPIEZA LA PARTE DE BUSCAR EL TALLER AL QUE SE LE VA A DAR DE ALTA EL GASTO
        label_mes = ttk.Label(frm, text='MES')
        label_mes.grid(column=1, row=5)
        elementos_creados.append(label_mes)#7
        label_anio = ttk.Label(frm, text='AÑO')
        label_anio.grid(column=2, row=5)
        elementos_creados.append(label_anio)#8 
        label_selectaller = ttk.Label(frm, text='SELECCIONAR TALLER:')
        label_selectaller.grid(column=4, row=5)
        elementos_creados.append(label_selectaller)#9
        label_taller = ttk.Label(frm, text='TALLER:')
        label_taller.grid(column=0,row=6)
        elementos_creados.append(label_taller)#10
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        anios = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
        combobox_mes = ttk.Combobox(frm, values=meses, width=40)
        combobox_mes.grid(column=1, row=6)
        combobox_mes.bind('<<ComboboxSelected>>', limpiar_bloquear_combobox)
        elementos_creados.append(combobox_mes)#11
        combobox_anio = ttk.Combobox(frm, values=anios)
        combobox_anio.grid(column=2, row=6)
        combobox_anio.bind('<<ComboboxSelected>>', limpiar_bloquear_combobox)
        elementos_creados.append(combobox_anio)#12
        boton_buscar_taller = ttk.Button(frm, text='BUSCAR', command=comando_boton_buscar)
        boton_buscar_taller.grid(column=3, row=6)
        elementos_creados.append(boton_buscar_taller)#13
        combobox_selecTaller = ttk.Combobox(frm, state='disable', width=50)
        combobox_selecTaller.grid(column=4, row=6)
        elementos_creados.append(combobox_selecTaller)#14
        boton_enviar = ttk.Button(frm, text='ENVIAR', command=lambda x=op: boton_enviar_funcion(op))
        boton_enviar.grid(column=0, row=10)
        elementos_creados.append(boton_enviar)#15
        
    def desplegar_opciones_servicios():
        global elementos_creados
        op = 'servicio'
        label_descripcion = ttk.Label(frm, text='DESCRIPCION:')
        label_descripcion.grid(column=0, row=2)
        elementos_creados.append(label_descripcion)#1 elementos creados
        entry_descripcion = ttk.Entry(frm, width=30)
        entry_descripcion.grid(column=1,row=2)
        elementos_creados.append(entry_descripcion)#2 elementos creados
        label_monto = ttk.Label(frm, text='MONTO:')
        label_monto.grid(column=0, row=3)
        elementos_creados.append(label_monto)#3 elementos creados
        entry_monto = ttk.Entry(frm, width=30)
        entry_monto.grid(column=1,row=3)
        elementos_creados.append(entry_monto)#4 elementos creados
        label_fecha = ttk.Label(frm, text='Fecha')
        label_fecha.grid(column=0, row=4)
        elementos_creados.append(label_fecha)#5 elementos creados
        fecha = datetime.now()
        cal = Calendar(frm, selectmode="day", year=fecha.year, month=fecha.month, day=fecha.day)
        cal.grid(column=1, row=4)
        elementos_creados.append(cal)#6 elementos creados
        boton_enviar = ttk.Button(frm, text='ENVIAR', command=lambda x=op: boton_enviar_funcion(op))
        boton_enviar.grid(column=0, row=5)
        elementos_creados.append(boton_enviar)#7 elementos creados
        combobox_tipo_servicio = ttk.Combobox(frm, values=['LUZ', 'AGUA', 'INTERNET'])
        combobox_tipo_servicio.grid(column=2, row=3)
        elementos_creados.append(combobox_tipo_servicio)#8 elementos creados 
        label_tipo_servicio = ttk.Label(frm, text='TIPO DE SERVICIO:')
        label_tipo_servicio.grid(column=2, row=2)
        elementos_creados.append(label_tipo_servicio)#9 elementos creados

    def desplegar_opciones_mtnmto():
        global elementos_creados
        op = 'mtnmto'
        label_descripcion = ttk.Label(frm, text='DESCRIPCION:')
        label_descripcion.grid(column=0, row=2)
        elementos_creados.append(label_descripcion)#1 elementos creados
        entry_descripcion = ttk.Entry(frm, width=30)
        entry_descripcion.grid(column=1,row=2)
        elementos_creados.append(entry_descripcion)#2 elementos creados
        label_monto = ttk.Label(frm, text='MONTO:')
        label_monto.grid(column=0, row=3)
        elementos_creados.append(label_monto)#3 elementos creados
        entry_monto = ttk.Entry(frm, width=30)
        entry_monto.grid(column=1,row=3)
        elementos_creados.append(entry_monto)#4 elementos creados
        label_fecha = ttk.Label(frm, text='Fecha')
        label_fecha.grid(column=0, row=4)
        elementos_creados.append(label_fecha)#5 elementos creados
        fecha = datetime.now()
        cal = Calendar(frm, selectmode="day", year=fecha.year, month=fecha.month, day=fecha.day)
        cal.grid(column=1, row=4)
        elementos_creados.append(cal)#6 elementos creados
        boton_enviar = ttk.Button(frm, text='ENVIAR', command=lambda x=op: boton_enviar_funcion(op))
        boton_enviar.grid(column=0, row=5)
        elementos_creados.append(boton_enviar)#7 elementos creados


    def desplegar_opciones_extra():
        global elementos_creados
        op = 'extra'
        label_descripcion = ttk.Label(frm, text='DESCRIPCION:')
        label_descripcion.grid(column=0, row=2)
        elementos_creados.append(label_descripcion)#1 elementos creados
        entry_descripcion = ttk.Entry(frm, width=30)
        entry_descripcion.grid(column=1,row=2)
        elementos_creados.append(entry_descripcion)#2 elementos creados
        label_monto = ttk.Label(frm, text='MONTO:')
        label_monto.grid(column=0, row=3)
        elementos_creados.append(label_monto)#3 elementos creados
        entry_monto = ttk.Entry(frm, width=30)
        entry_monto.grid(column=1,row=3)
        elementos_creados.append(entry_monto)#4 elementos creados
        label_fecha = ttk.Label(frm, text='Fecha')
        label_fecha.grid(column=0, row=4)
        elementos_creados.append(label_fecha)#5 elementos creados
        fecha = datetime.now()
        cal = Calendar(frm, selectmode="day", year=fecha.year, month=fecha.month, day=fecha.day)
        cal.grid(column=1, row=4)
        elementos_creados.append(cal)#6 elementos creados
        boton_enviar = ttk.Button(frm, text='ENVIAR', command=lambda x=op: boton_enviar_funcion(op))
        boton_enviar.grid(column=0, row=5)
        elementos_creados.append(boton_enviar)#7 elementos creados

    ###########DEPENDIENDO DE LA OPCION SELECIONADA EN EL EN EL CBOX SECUNDARIO SE DECIDE QUE FUNCION SE EJECUTA
    def opcion_seleccionada_cboxsecundario(event):
        global elementos_creados
        elementos_creados = eliminar_elementos_creados(elementos_creados, 1)
        print('opcion_seleccionada_cboxsecundario elementos creados:')
        print(elementos_creados)
        op = elementos_creados[0].get()
        print(op)
        if op == 'TALLER':
            desplegar_opciones_taller()
        elif op == 'EXTRA':
            desplegar_opciones_extra()
        elif op == 'MTNMTO':
            desplegar_opciones_mtnmto()
        elif op == 'SERVICIO':
            desplegar_opciones_servicios()
        elif op == 'ALIMENTO':
            desplegar_opciones_alimentos()
        elif op == "MOBILIARIO":
            desplegar_opciones_mobiliario()
        else:
            print('ERROR en variable op opcion_seleccionada_gastos')

    ###################DEPENDIENDO DE LA SELECCION GENERAL SE DESPLIEGA UN COMBOBOX SECUNDARIO DE DICHA OPCION
    def desplegar_combobox_ingreso():
        global elementos_creados
        combobox_op_ingreso = ttk.Combobox(frm, values='EXTRA')
        combobox_op_ingreso.grid(column=2 , row=1 )
        combobox_op_ingreso.bind('<<ComboboxSelected>>', opcion_seleccionada_cboxsecundario)
        elementos_creados.append(combobox_op_ingreso)#0 elementos creados

    def desplegar_combobox_gasto():
        global elementos_creados
        combobox_op_gasto = ttk.Combobox(frm, values=['TALLER', 'MTNMTO', 'SERVICIO', 'ALIMENTO', 'MOBILIARIO'])
        combobox_op_gasto.grid(column=2 , row=1 )
        combobox_op_gasto.bind('<<ComboboxSelected>>', opcion_seleccionada_cboxsecundario)
        elementos_creados.append(combobox_op_gasto)#0 elementos creados

    
    ########################SELECCION GENERAL ENTRE GASTO E INGRESO
    def opcion_seleccionada_combobox(event):
        global elementos_creados
        eliminar_elementos_creados(elementos_creados)
        elementos_creados = [] ####REINICIAMOS LA VARIABLE PARA QUE NO EXISTA CONFLICTOS DE REFERENCIA
        op = gastoIngreso_combobox.get()
        if op == 'INGRESO':
            desplegar_combobox_ingreso()
        elif op == 'GASTO':
            desplegar_combobox_gasto()
        else:
            print('CASO EXTRAÑO EN opcion_seleccionada_combobox()')
        
    global elementos_creados
    global elementos_creados_taller
    elementos_creados_taller = []
    elementos_creados = []
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.geometry('1200x600')
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text='ALTA GASTO/INGRESO:').grid(column=0,row=0)
    ttk.Label(frm, text='TIPO:').grid(column=0, row=1)
    gastoIngreso_combobox = ttk.Combobox(frm, values=['GASTO', 'INGRESO'])
    gastoIngreso_combobox.grid(column=1,row=1)
    gastoIngreso_combobox.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox)

    
########################################### VENTANA PAGO CLIENTE ################################
def ventana_pago_cliente():
    def buscar_curso_boton():
        mostrar_cursos_combobox.set('')
        mes_seleccionado = mes_combobox.get()
        mes_en_numero = {'Enero':'01', 
                         'Febrero':'02',
                         'Marzo':'03',
                         'Abril':'04',
                         'Mayo':'05',
                         'Junio':'06',
                         'Julio':'07',
                         'Agosto':'08',
                         'Septiembre':'09',
                         'Octubre':'10',
                         'Noviembre':'11',
                         'Diciembre':'12',}
        anio_seleccionado = anio_combobox.get()
        informacion = extraer_talleres_bd(mes_en_numero[mes_seleccionado], anio_seleccionado)
        if informacion == "ERROR":
            indicador = ttk.Label(frm, text='DATABASE ERROR', background='red')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
        elif informacion == 'NOT FOUND':
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
            mostrar_cursos_combobox.set('')
            mostrar_cursos_combobox.config(state='disable', width=50)
        else:
            indicador = ttk.Label(frm, text='COINCIDENCIA', background='green')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
            info_lista = []
            for i in informacion:
                formato_codigo_curso = f'{i[0]}-{i[1]}'
                info_lista.append(formato_codigo_curso)
            mostrar_cursos_combobox.config(state='readonly', values=info_lista, width=50)

    def opcion_seleccionada_combobox(event): #FUNCION QUE SE EJECUTA CUANDO EL USUARIO SELECCIONA UNA OPCION DEL COMBOBOX
        taller = mostrar_cursos_combobox.get()
        taller_lista = taller.split('-')
        resultado_consulta = extraer_clientes_bd(taller_lista[0])
        if resultado_consulta == 'ERROR':
            indicador = ttk.Label(frm, text='DATABASE ERROR', background='red')
            indicador.grid(column=4, row=0)
            frm.after(3000, lambda: indicador.grid_remove())
        elif resultado_consulta == 'NO INFO':
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=4, row=0)
            frm.after(3000, lambda: indicador.grid_remove())
        else: 
            indicador = ttk.Label(frm, text='DESPLEGANDO', background='green')
            indicador.grid(column=4, row=0)
            frm.after(3000, lambda: indicador.grid_remove())
            costo = extraer_costo_bd(taller_lista[0])
            desplegar_informacion(resultado_consulta, costo)
            boton_buscar_pCodigo.config(state='disable')
    
    def limpiar_informacion():
        for label in labels_creados:
            label.destroy()     
        for boton in botones_creados:
            boton.destroy()
        for entry in entrys_creados:
            entry.destroy()

        
        mes_combobox.config(state='normal')
        anio_combobox.config(state='normal')
        mostrar_cursos_combobox.config(state='normal')
        boton_buscar_pCodigo.config(state='normal')
        boton_buscar.config(state='normal')
    
    def comando_boton_pagar_bucle(i, cliente, taller):
        global entrys_creados
        info = entrys_creados[i].get()
        x = modificar_pagado_db(cliente, info)
        if x == True:
            print('SE HA PODIDO MODIFICAR PAGADO')
            fecha = datetime.now()
            fecha_lista = [str(fecha.month), str(fecha.day), str(fecha.year)]
            fecha_organizada = enlistar_fecha(fecha_lista, 'datetime')
            informacion_ingreso = [cliente, 'i',  info, 'taller', taller, fecha_organizada[0], fecha_organizada[1], fecha_organizada[2]]
            enviar_gasto_ingreso_db(informacion_ingreso)
        


            

    def desplegar_informacion(info, costo):
            global labels_creados
            global entrys_creados
            global botones_creados
            entrys_creados = []
            labels_creados =[]
            botones_creados = []
            total_taller = 0.0
            total_pagado = 0.0
            total_faltante = 0.0
            for i in range(0, len(info)):
                indicador_codigo = ttk.Label(frm, text=info[i][0],border=100)
                indicador_codigo.grid(column= 0, row= i+5)
                labels_creados.append(indicador_codigo)
                indicador_nombre = ttk.Label(frm, text=info[i][1])
                indicador_nombre.grid(column= 1, row= i+5)
                labels_creados.append(indicador_nombre)
                indicador_apellido = ttk.Label(frm, text=info[i][2])
                indicador_apellido.grid(column= 2, row= i+5)
                labels_creados.append(indicador_apellido)
                indicador_taller = ttk.Label(frm, text=info[i][3])
                indicador_taller.grid(column= 3, row= i+5)
                labels_creados.append(indicador_taller)
                indicador_pagado = ttk.Label(frm, text=info[i][4])
                indicador_pagado.grid(column= 4, row= i+5)
                labels_creados.append(indicador_pagado)
                indicador_costo = ttk.Label(frm, text=costo)
                indicador_costo.grid(column= 5, row= i+5)
                labels_creados.append(indicador_costo)
                entry_pago = ttk.Entry(frm)
                entry_pago.grid(column= 7, row= i+5)
                entrys_creados.append(entry_pago)
                boton_pagar = ttk.Button(frm, text='PAGAR', command=lambda indice=i, cliente=info[i][0], taller=info[i][3]: comando_boton_pagar_bucle(indice, cliente, taller))
                boton_pagar.grid(column=8, row=i+5)
                botones_creados.append(boton_pagar)
                faltante = float(costo[0][0])-float(info[i][4])
                conversion1 = float(costo[0][0])
                conversion2 = float(info[i][4])
                total_taller += conversion1
                total_pagado += conversion2
                ultimo_label = i+5
                if faltante <= 0:
                    indicador_faltante = ttk.Label(frm, text='PAGADO', background='green')
                    indicador_faltante.grid(column= 6, row= i+5)
                    labels_creados.append(indicador_faltante)
                else:
                    indicador_faltante = ttk.Label(frm, text=faltante)
                    indicador_faltante.grid(column= 6, row= i+5)
                    labels_creados.append(indicador_faltante)
                    total_faltante += faltante
            indicador_total_taller = ttk.Label(frm, text=total_taller, background='#add8e6')
            indicador_total_taller.grid(column= 5, row= ultimo_label+1)
            labels_creados.append(indicador_total_taller)
            indicador_total_pagado = ttk.Label(frm, text=total_pagado, background='#add8e6')
            indicador_total_pagado.grid(column= 4, row= ultimo_label+1)
            labels_creados.append(indicador_total_pagado)
            indicador_total_faltante = ttk.Label(frm, text=total_faltante, background='#add8e6')
            indicador_total_faltante.grid(column= 6, row= ultimo_label+1)
            labels_creados.append(indicador_total_faltante)
            label_total = ttk.Label(frm, text='TOTAL', background='#add8e6')
            label_total.grid(column= 3, row= ultimo_label+1)
            labels_creados.append(label_total)
            boton_limpiar = ttk.Button(frm, text='LIMPIAR', command=limpiar_informacion)
            boton_limpiar.grid(column=5, row=2)
            labels_creados.append(boton_limpiar)
            mes_combobox.config(state='disable')
            anio_combobox.config(state='disable')
            mostrar_cursos_combobox.config(state='disable')
            boton_buscar_pCodigo.config(state='disable')
    
    def comando_buscar_tallerPCodigo():
        codigo = entry_codigo.get()
        info = consultar_info_bd(codigo)
        if info == 'ERROR':
            indicador = ttk.Label(frm, text='DB ERROR', background='red')
            indicador.grid(column=3, row=3)
            frm.after(3000, lambda: indicador.grid_remove())
        elif info == False:
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=3, row=3)
            frm.after(3000, lambda: indicador.grid_remove())
        else:
            costo = extraer_costo_bd(codigo)
            clientes = extraer_clientes_bd(codigo)
            if clientes == 'NO INFO':
                indicador = ttk.Label(frm, text='NO INFO', background='red')
                indicador.grid(column=3, row=3)
                frm.after(3000, lambda: indicador.grid_remove())
            elif clientes == 'ERROR':
                indicador = ttk.Label(frm, text='DB ERROR', background='red')
                indicador.grid(column=3, row=3)
                frm.after(3000, lambda: indicador.grid_remove())
            else:
                desplegar_informacion(clientes, costo)
                boton_buscar.config(state='disable')

            
    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text="REALIZAR PAGO:").grid(column=0, row=0)
    # Menú desplegable con los meses y anios
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    anios = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    mes_combobox = ttk.Combobox(frm, values=meses, state="readonly")
    mes_combobox.grid(column=1, row=2)
    anio_combobox = ttk.Combobox(frm, values=anios, state='readonly')
    anio_combobox.grid(column=2, row=2)
    ttk.Label(frm, text='BUSCAR CURSO POR FECHA:').grid(column=0, row=2 )
    ttk.Label(frm, text='MES').grid(column=1, row=1)
    ttk.Label(frm, text='AÑO').grid(column=2, row=1)
    ttk.Label(frm, text='SELECCIONAR TALLER:').grid(column=4, row=1)
    boton_buscar = ttk.Button(frm, text="Buscar", command=buscar_curso_boton)
    boton_buscar.grid(column=3, row=2)
    mostrar_cursos_combobox = ttk.Combobox(frm, state="disable", width=50)
    mostrar_cursos_combobox.grid(column=4, row=2)
    mostrar_cursos_combobox.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox)
    #BUSCAR POR CODIGO
    ttk.Label(frm, text='BUSCAR POR CODIGO:').grid(column=0, row=3)
    entry_codigo = ttk.Entry(frm)
    entry_codigo.grid(column=1, row=3)
    boton_buscar_pCodigo = ttk.Button(frm, text='BUSCAR', command=comando_buscar_tallerPCodigo)
    boton_buscar_pCodigo.grid(column=2, row=3)
    #NOMBRE CASILLAS
    ttk.Label(frm, text='CODIGO:').grid(column=0, row=4)
    ttk.Label(frm, text='NOMBRE:').grid(column=1, row=4)
    ttk.Label(frm, text='APELLIDO:').grid(column=2, row=4)
    ttk.Label(frm, text='TALLER:').grid(column=3, row=4)
    ttk.Label(frm, text='PAGADO:').grid(column=4, row=4)
    ttk.Label(frm, text='COSTO:').grid(column=5, row=4)
    ttk.Label(frm, text='FALTANTE:').grid(column=6, row=4)
    ttk.Label(frm, text='PAGO:').grid(column=7, row=4)



############################################### BUSCAR CLIENTE      ##############################################
def ventana_buscar_cliente():
    def comando_boton_buscar_pcodigo():
        global labels_creados
        labels_creados = []
        codigo = entry_codigo.get()
        info = extraer_cliente_pcodigo__bd(codigo)
        if info == 'ERROR':
            indicadorError = ttk.Label(frm, text='ERROR', background='red')
            indicadorError.grid(column=3, row=1)
            frm.after(3000, lambda: indicadorError.grid_remove())
        elif info == 'NO INFO':
            indicadorNoInfo = ttk.Label(frm, text='NO INFO', background='red')
            indicadorNoInfo.grid(column=3, row=1)
            frm.after(3000, lambda: indicadorNoInfo.grid_remove())
        else:
             for i in range(len(info)):
                indicador_codigo = ttk.Label(frm, text=info[i][0])
                indicador_codigo.grid(column=0, row=i+5)
                labels_creados.append(indicador_codigo)
                indicador_nombre = ttk.Label(frm, text=info[i][1])
                indicador_nombre.grid(column=1, row=i+5)
                labels_creados.append(indicador_nombre)
                indicador_apellido = ttk.Label(frm, text=info[i][2])
                indicador_apellido.grid(column=2, row=i+5)
                labels_creados.append(indicador_apellido)
                indicador_taller = ttk.Label(frm, text=info[i][3])
                indicador_taller.grid(column=3, row=i+5)
                labels_creados.append(indicador_taller)
                indicador_pagado = ttk.Label(frm, text=info[i][4])
                indicador_pagado.grid(column=4, row=i+5)
                labels_creados.append(indicador_pagado)
                costo = extraer_costo_bd(info[i][3])
                if costo == 'NOT FOUND':
                    indicador_costo = ttk.Label(frm, text='NO INFO', background='red')
                    indicador_costo.grid(column=5, row=i+5)
                    labels_creados.append(indicador_costo)
                elif costo == 'ERROR':
                    indicador_costo = ttk.Label(frm, text='DB ERROR', background='red')
                    indicador_costo.grid(column=5, row=i+5)
                    labels_creados.append(indicador_costo)
                else:
                    indicador_costo = ttk.Label(frm, text=costo[0][0])
                    indicador_costo.grid(column=5, row=i+5)
                    labels_creados.append(indicador_costo)
                    costo_float = float(costo[0][0])
                    pagado_float = float(info[i][4])
                    faltante = costo_float-pagado_float
                    indicador_faltante = ttk.Label(frm, text=faltante)
                    indicador_faltante.grid(column=6, row=i+5)
                    labels_creados.append(indicador_costo)





    
    def comando_boton_buscar_pNombre():
        global labels_creados
        try:
            for label in labels_creados:
                label.destroy()
        except NameError:
            pass
        labels_creados = []
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        info = extraer_nombres_bd()
        if info == 'ERROR':
            indicadorError = ttk.Label(frm, text='ERROR', background='red')
            indicadorError.grid(column=3, row=3)
            frm.after(3000, lambda: indicadorError.grid_remove())
        elif info == 'NO INFO':
            indicadorNoInfo = ttk.Label(frm, text='NO INFO', background='red')
            indicadorNoInfo.grid(column=3, row=3)
            frm.after(3000, lambda: indicadorNoInfo.grid_remove())
        else:
            coincidencias = buscador_de_coincidencias(info, nombre, apellido)
            if coincidencias == []:
                print('SIN COINCIDENCIAS')
            else:
                print(coincidencias)
                for i in range(len(coincidencias)):
                    print(f'CICLO {i}')
                    indicador_codigo = ttk.Label(frm, text=coincidencias[i][0])
                    indicador_codigo.grid(column=0, row=i+5)
                    labels_creados.append(indicador_codigo)
                    indicador_nombre = ttk.Label(frm, text=coincidencias[i][1])
                    indicador_nombre.grid(column=1, row=i+5)
                    labels_creados.append(indicador_nombre)
                    indicador_apellido = ttk.Label(frm, text=coincidencias[i][2])
                    indicador_apellido.grid(column=2, row=i+5)
                    labels_creados.append(indicador_apellido)
                    indicador_taller = ttk.Label(frm, text=coincidencias[i][3])
                    indicador_taller.grid(column=3, row=i+5)
                    labels_creados.append(indicador_taller)
                    indicador_pagado = ttk.Label(frm, text=coincidencias[i][4])
                    indicador_pagado.grid(column=4, row=i+5)
                    labels_creados.append(indicador_pagado)
        



    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text="BUSCAR CLIENTE").grid(column=0, row=0)
    ttk.Label(frm, text="POR CODIGO:").grid(column=0, row=1)
    entry_codigo = ttk.Entry(frm)
    entry_codigo.grid(column=1, row=1)
    boton_buscar_codigo = ttk.Button(frm, text='BUSCAR', command=comando_boton_buscar_pcodigo)
    boton_buscar_codigo.grid(column=2, row=1)
    ttk.Label(frm, text="POR NOMBRE:").grid(column=0, row=3)
    ttk.Label(frm, text="NOMBRE:").grid(column=1, row=2)
    ttk.Label(frm, text="APELLIDO:").grid(column=2, row=2)
    entry_nombre = ttk.Entry(frm)
    entry_nombre.grid(column=1, row=3)
    entry_apellido = ttk.Entry(frm)
    entry_apellido.grid(column=2, row=3)
    bonton_buscar_NombreApellido = ttk.Button(frm, text='BUSCAR', command=comando_boton_buscar_pNombre)
    bonton_buscar_NombreApellido.grid(column=3, row=3)
    ####INDICADORES DE INFORMACION DE CLIENTE
    ttk.Label(frm, text='CODIGO').grid(column=0,row=4)
    ttk.Label(frm, text='NOMBRE').grid(column=1,row=4)
    ttk.Label(frm, text='APELLIDO').grid(column=2,row=4)
    ttk.Label(frm, text='TALLER').grid(column=3,row=4)
    ttk.Label(frm, text='PAGADO').grid(column=4,row=4)
    ttk.Label(frm, text='COSTO').grid(column=5,row=4)
    ttk.Label(frm, text='FALTANTE').grid(column=6,row=4)




############################################### CONSULTAR TALLER    ###############################################
def ventana_consultar_taller():
    def buscar_curso_boton():
        mostrar_cursos_combobox.set('')
        mes_seleccionado = mes_combobox.get()
        mes_en_numero = {'Enero':'01', 
                         'Febrero':'02',
                         'Marzo':'03',
                         'Abril':'04',
                         'Mayo':'05',
                         'Junio':'06',
                         'Julio':'07',
                         'Agosto':'08',
                         'Septiembre':'09',
                         'Octubre':'10',
                         'Noviembre':'11',
                         'Diciembre':'12',}
        anio_seleccionado = anio_combobox.get()
        informacion = extraer_talleres_bd(mes_en_numero[mes_seleccionado], anio_seleccionado)
        if informacion == "ERROR":
            indicador = ttk.Label(frm, text='DATABASE ERROR', background='red')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
        elif informacion == 'NOT FOUND':
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
            mostrar_cursos_combobox.set('')
            mostrar_cursos_combobox.config(state='disable', width=50)
        else:
            indicador = ttk.Label(frm, text='COINCIDENCIA', background='green')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
            info_lista = []
            for i in informacion:
                formato_codigo_curso = f'{i[0]}-{i[1]}'
                info_lista.append(formato_codigo_curso)
            mostrar_cursos_combobox.config(state='readonly', values=info_lista, width=50)

    def opcion_seleccionada_combobox(event): #FUNCION QUE SE EJECUTA CUANDO EL USUARIO SELECCIONA UNA OPCION DEL COMBOBOX
        taller = mostrar_cursos_combobox.get()
        taller_lista = taller.split('-')
        resultado_consulta = extraer_clientes_bd(taller_lista[0])
        if resultado_consulta == 'ERROR':
            indicador = ttk.Label(frm, text='DATABASE ERROR', background='red')
            indicador.grid(column=4, row=0)
            frm.after(3000, lambda: indicador.grid_remove())
        elif resultado_consulta == 'NO INFO':
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=4, row=0)
            frm.after(3000, lambda: indicador.grid_remove())
        else: 
            indicador = ttk.Label(frm, text='DESPLEGANDO', background='green')
            indicador.grid(column=4, row=0)
            frm.after(3000, lambda: indicador.grid_remove())
            costo = extraer_costo_bd(taller_lista[0])
            desplegar_informacion(resultado_consulta, costo)
            boton_buscar_pCodigo.config(state='disable')
    
    def limpiar_informacion():
        for label in labels_creados:
            label.destroy()
        mes_combobox.config(state='normal')
        anio_combobox.config(state='normal')
        mostrar_cursos_combobox.config(state='normal')
        boton_buscar_pCodigo.config(state='normal')
        boton_buscar.config(state='normal')
            

    def desplegar_informacion(info, costo):
            global labels_creados
            labels_creados =[]
            total_taller = 0.0
            total_pagado = 0.0
            total_faltante = 0.0
            for i in range(0, len(info)):
                indicador_codigo = ttk.Label(frm, text=info[i][0],border=100)
                indicador_codigo.grid(column= 0, row= i+5)
                labels_creados.append(indicador_codigo)
                indicador_nombre = ttk.Label(frm, text=info[i][1])
                indicador_nombre.grid(column= 1, row= i+5)
                labels_creados.append(indicador_nombre)
                indicador_apellido = ttk.Label(frm, text=info[i][2])
                indicador_apellido.grid(column= 2, row= i+5)
                labels_creados.append(indicador_apellido)
                indicador_taller = ttk.Label(frm, text=info[i][3])
                indicador_taller.grid(column= 3, row= i+5)
                labels_creados.append(indicador_taller)
                indicador_pagado = ttk.Label(frm, text=info[i][4])
                indicador_pagado.grid(column= 4, row= i+5)
                labels_creados.append(indicador_pagado)
                indicador_costo = ttk.Label(frm, text=costo)
                indicador_costo.grid(column= 5, row= i+5)
                labels_creados.append(indicador_costo)
                faltante = float(costo[0][0])-float(info[i][4])
                conversion1 = float(costo[0][0])
                conversion2 = float(info[i][4])
                total_taller += conversion1
                total_pagado += conversion2
                ultimo_label = i+5
                if faltante <= 0:
                    indicador_faltante = ttk.Label(frm, text='PAGADO', background='green')
                    indicador_faltante.grid(column= 6, row= i+5)
                    labels_creados.append(indicador_faltante)
                else:
                    indicador_faltante = ttk.Label(frm, text=faltante)
                    indicador_faltante.grid(column= 6, row= i+5)
                    labels_creados.append(indicador_faltante)
                    total_faltante += faltante
            indicador_total_taller = ttk.Label(frm, text=total_taller, background='#add8e6')
            indicador_total_taller.grid(column= 5, row= ultimo_label+1)
            labels_creados.append(indicador_total_taller)
            indicador_total_pagado = ttk.Label(frm, text=total_pagado, background='#add8e6')
            indicador_total_pagado.grid(column= 4, row= ultimo_label+1)
            labels_creados.append(indicador_total_pagado)
            indicador_total_faltante = ttk.Label(frm, text=total_faltante, background='#add8e6')
            indicador_total_faltante.grid(column= 6, row= ultimo_label+1)
            labels_creados.append(indicador_total_faltante)
            label_total = ttk.Label(frm, text='TOTAL', background='#add8e6')
            label_total.grid(column= 3, row= ultimo_label+1)
            labels_creados.append(label_total)
            boton_limpiar = ttk.Button(frm, text='LIMPIAR', command=limpiar_informacion)
            boton_limpiar.grid(column=5, row=2)
            labels_creados.append(boton_limpiar)
            mes_combobox.config(state='disable')
            anio_combobox.config(state='disable')
            mostrar_cursos_combobox.config(state='disable')
            boton_buscar_pCodigo.config(state='disable')
    
    def comando_buscar_tallerPCodigo():
        codigo = entry_codigo.get()
        info = consultar_info_bd(codigo)
        if info == 'ERROR':
            indicador = ttk.Label(frm, text='DB ERROR', background='red')
            indicador.grid(column=3, row=3)
            frm.after(3000, lambda: indicador.grid_remove())
        elif info == False:
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=3, row=3)
            frm.after(3000, lambda: indicador.grid_remove())
        else:
            costo = extraer_costo_bd(codigo)
            clientes = extraer_clientes_bd(codigo)
            if clientes == 'NO INFO':
                indicador = ttk.Label(frm, text='NO INFO', background='red')
                indicador.grid(column=3, row=3)
                frm.after(3000, lambda: indicador.grid_remove())
            elif clientes == 'ERROR':
                indicador = ttk.Label(frm, text='DB ERROR', background='red')
                indicador.grid(column=3, row=3)
                frm.after(3000, lambda: indicador.grid_remove())
            else:
                desplegar_informacion(clientes, costo)
                boton_buscar.config(state='disable')

            
                
            
              

            

    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text="CONSULTAR TALLER:").grid(column=0, row=0)
    # Menú desplegable con los meses y anios
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    anios = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    mes_combobox = ttk.Combobox(frm, values=meses, state="readonly")
    mes_combobox.grid(column=1, row=2)
    anio_combobox = ttk.Combobox(frm, values=anios, state='readonly')
    anio_combobox.grid(column=2, row=2)
    ttk.Label(frm, text='BUSCAR CURSO POR FECHA:').grid(column=0, row=2 )
    ttk.Label(frm, text='MES').grid(column=1, row=1)
    ttk.Label(frm, text='AÑO').grid(column=2, row=1)
    ttk.Label(frm, text='SELECCIONAR TALLER:').grid(column=4, row=1)
    boton_buscar = ttk.Button(frm, text="Buscar", command=buscar_curso_boton)
    boton_buscar.grid(column=3, row=2)
    mostrar_cursos_combobox = ttk.Combobox(frm, state="disable", width=50)
    mostrar_cursos_combobox.grid(column=4, row=2)
    mostrar_cursos_combobox.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox)
    #BUSCAR POR CODIGO
    ttk.Label(frm, text='BUSCAR POR CODIGO:').grid(column=0, row=3)
    entry_codigo = ttk.Entry(frm)
    entry_codigo.grid(column=1, row=3)
    boton_buscar_pCodigo = ttk.Button(frm, text='BUSCAR', command=comando_buscar_tallerPCodigo)
    boton_buscar_pCodigo.grid(column=2, row=3)
    #NOMBRE CASILLAS
    ttk.Label(frm, text='CODIGO:').grid(column=0, row=4)
    ttk.Label(frm, text='NOMBRE:').grid(column=1, row=4)
    ttk.Label(frm, text='APELLIDO:').grid(column=2, row=4)
    ttk.Label(frm, text='TALLER:').grid(column=3, row=4)
    ttk.Label(frm, text='PAGADO:').grid(column=4, row=4)
    ttk.Label(frm, text='COSTO:').grid(column=5, row=4)
    ttk.Label(frm, text='FALTANTE:').grid(column=6, row=4)


###############################################    INSCRIBIR CLIENTE       #####################################
def ventana_inscribir_cliente():

    def enviar_cliente_boton():
        nombre = nombre_cliente_entry.get()
        apellido = apellido_cliente_entry.get()
        taller = mostrar_cursos_combobox.get()
        taller_lista = taller.split('-')
        pago = pago_cliente_entry.get()
        informacion = (nombre, apellido, taller_lista[0], pago)
        resultado_envio = enviar_cliente_bd(informacion)
        if resultado_envio == 'ERROR':
            indicador = ttk.Label(frm, text='ERROR AL ENVIAR', background='red')
            indicador.grid(column=1, row=7)
            frm.after(3000, lambda: indicador.grid_remove())
        else:
            indicador = ttk.Label(frm, text='ENVIADO', background='green')
            indicador.grid(column=1, row=7)
            frm.after(3000, lambda: indicador.grid_remove())



        
    def buscar_curso_boton():
        mes_seleccionado = mes_combobox.get()
        mes_en_numero = {'Enero':'01', 
                         'Febrero':'02',
                         'Marzo':'03',
                         'Abril':'04',
                         'Mayo':'05',
                         'Junio':'06',
                         'Julio':'07',
                         'Agosto':'08',
                         'Septiembre':'09',
                         'Octubre':'10',
                         'Noviembre':'11',
                         'Diciembre':'12',}
        anio_seleccionado = anio_combobox.get()
        informacion = extraer_talleres_bd(mes_en_numero[mes_seleccionado], anio_seleccionado)
        if informacion == "ERROR":
            indicador = ttk.Label(frm, text='DATABASE ERROR', background='red')
            indicador.grid(column=3, row=3)
            frm.after(3000, lambda: indicador.grid_remove())
        elif informacion == 'NOT FOUND':
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=3, row=3)
            frm.after(3000, lambda: indicador.grid_remove())
            mostrar_cursos_combobox.set('')
            mostrar_cursos_combobox.config(state='disable', width=50)
            label_mostrar_costo.config(text='')
        else:
            indicador = ttk.Label(frm, text='COINCIDENCIA', background='green')
            indicador.grid(column=3, row=3)
            frm.after(3000, lambda: indicador.grid_remove())
            info_lista = []
            for i in informacion:
                formato_codigo_curso = f'{i[0]}-{i[1]}'
                info_lista.append(formato_codigo_curso)
            mostrar_cursos_combobox.config(state='readonly', values=info_lista, width=50)

    def opcion_seleccionada_combobox(event):    #ESTA FUNCION SE EJECUTA CUANDO EL USUARIO SELECCIONA UNA OPCION DEL COMBOBOX
        opcion_seleccionada = mostrar_cursos_combobox.get()
        opcion_seleccionada_lista = opcion_seleccionada.split('-')
        costo = extraer_costo_bd(opcion_seleccionada_lista[0])
        if costo == 'NOT FOUND':
            print('NO SE ENCONTRO INFO')
        elif costo == 'ERROR':
            print('HUBO ERROR')
        else:
            label_mostrar_costo.config(text=costo[0][0])


    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text="INSCRIBIR CLIENTE:").grid(column=0, row=0)
    ttk.Label(frm, text='NOMBRE:').grid(column=0, row=1)
    nombre_cliente_entry = ttk.Entry(frm)
    nombre_cliente_entry.grid(column=1, row=1)
    ttk.Label(frm, text='APELLIDO:').grid(column=0, row=2)
    apellido_cliente_entry = ttk.Entry(frm)
    apellido_cliente_entry.grid(column=1, row=2)
    ttk.Label(frm, text='BUSCAR CURSO POR FECHA:').grid(column=0, row=4 )
    ttk.Label(frm, text='MES').grid(column=1, row=3)
    ttk.Label(frm, text='AÑO').grid(column=2, row=3)
    ttk.Label(frm, text='SELECCIONAR TALLER:').grid(column=4, row=3)
    # Menú desplegable con los meses y anios
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    anios = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    mes_combobox = ttk.Combobox(frm, values=meses, state="readonly")
    mes_combobox.grid(column=1, row=4)
    anio_combobox = ttk.Combobox(frm, values=anios, state='readonly')
    anio_combobox.grid(column=2, row=4)
    #Boton para buscar taller
    boton_buscar = ttk.Button(frm, text="Buscar", command=buscar_curso_boton)
    boton_buscar.grid(column=3, row=4)
    mostrar_cursos_combobox = ttk.Combobox(frm, state="disable", width=50)
    mostrar_cursos_combobox.grid(column=4, row=4)
    mostrar_cursos_combobox.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox)
    ttk.Label(frm, text='PAGO:').grid(column=0, row=5)
    pago_cliente_entry = ttk.Entry(frm)
    pago_cliente_entry.grid(column=0, row=6)
    ttk.Label(frm, text='COSTO TALLER:').grid(column=1, row=5)
    label_mostrar_costo = ttk.Label(frm, text='COSTO')
    label_mostrar_costo.grid(column=1, row=6)
    # Botón para enviar informacion
    boton_enviar = ttk.Button(frm, text="ENVIAR", command=enviar_cliente_boton)
    boton_enviar.grid(column=0, row=7)
    
    
    



    #NOMBRE APELLIDO CURSO FECHA CURSO COSTO DE CURSO
    #PAGO   EL CODIGO DE CLIENTE ES

###############################################     DAR DE BAJA TALLER      ########################################


def ventana_baja_taller():
    def comparar_psw():
        global psw
        psw_introducida = intro_psw.get()
        if psw == psw_introducida:
            
            entry_codigo_curso.config(state = 'normal')
            button_psw_aceptar2.config(state = 'normal')
            button_psw_aceptar3.config(state = 'normal')
        else:
            print('Contraseña incorrecta')
    
    def mostrar_curso_a_eliminar():
        id = entry_codigo_curso.get()
        datos_del_curso = consultar_info_bd(id)
        print(datos_del_curso)
        if datos_del_curso == None:
            label_mostrar_curso.config(text="No se encontro informacion")
        elif datos_del_curso == False:
            pass
        else:
            curso_a_mostrar = f'CURSO: {datos_del_curso[1]}\n COSTO: {datos_del_curso[2]}\n DIA: {datos_del_curso[3]}\n MES: {datos_del_curso[4]}\n AÑO: {datos_del_curso[5]}\n HORARIO: {datos_del_curso[6]}\n DISPONIBILIDAD: {datos_del_curso[7]}\n\nIMPORTANTE!!\nAL PRESIONAR ACEPTAR\n ELIMINARAS DE MANERA\n PERMANENTE EL TALLER\n ESPECIFICADO Y TODOS\n LOS CLIENTES INSCRITOS'
            label_mostrar_curso.config(text=curso_a_mostrar, background='yellow')
    
    def confirmar_eliminar():
        id = entry_codigo_curso.get()
        if eliminar_curso_db(int(id)) == True:
            label_mostrar_curso.config(text='ELIMINADO', background='green')
            entry_codigo_curso.delete(0, 'end')
            entry_codigo_curso.config(state='disabled')
            button_psw_aceptar2.config(state='disabled')
            button_psw_aceptar3.config(state='disabled')
            intro_psw.delete(0, 'end')
            eliminar_clientes_curso_bd(id)


        else:
            label_mostrar_curso.config(text='No se ha podido eliminar', background='red')
            entry_codigo_curso.delete(0, 'end')
            entry_codigo_curso.config(state='disabled')
            button_psw_aceptar2.config(state='disabled')
            button_psw_aceptar3.config(state='disabled')
            intro_psw.delete(0, 'end')





    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text="ELIMINAR CURSO\nPASSWORD:").grid(column=0, row=0)
    intro_psw = ttk.Entry(frm)
    intro_psw.grid(column=0, row=1)
    button_psw_aceptar = ttk.Button(frm, text='ACEPTAR', command=comparar_psw).grid(column=0, row=2)
    ttk.Label(frm, text='CODIGO DE CURSO:').grid(column=0, row=3)
    entry_codigo_curso = ttk.Entry(frm, state='disabled')
    entry_codigo_curso.grid(column=0, row=4)
    button_psw_aceptar2 = ttk.Button(frm, text='ACEPTAR', command=mostrar_curso_a_eliminar, state='disabled')
    button_psw_aceptar2.grid(column=0, row=5)
    ttk.Label(frm, text="SE ELIMINARA:", background='red').grid(column=0, row=6)
    label_mostrar_curso = ttk.Label(frm, text="SIN INFORMACION")
    label_mostrar_curso.grid(column=0, row=7)
    button_psw_aceptar3 = ttk.Button(frm, text='ACEPTAR', command=confirmar_eliminar, state='disabled')
    button_psw_aceptar3.grid(column=0, row=8)
    ttk.Button(frm, text="CERRAR", command=ventana_secundaria.destroy).grid(column=0, row=9)


########################################## DAR DE ALTA CURSO #####################################################
def ventana_alta_taller():
    def enviar_curso_a_bd():
        nombre_curso = entry_nombre.get()
        costo = entry_costo.get()
        fecha_curso = cal.get_date()
        fecha_curso_lista = fecha_curso.split('/')
        if len(fecha_curso_lista[1]) == 1:   #SE LE DA FORMATO DE 2DIGITOS A DIA EN DADO CASO DE TENER 1 DIGITO
            fecha_curso_lista[1] = f'0{fecha_curso_lista[1]}'
        else:
            pass
        if len(fecha_curso_lista[0]) == 1:   #SE LE DA FORMATO DE 2DIGITOS A MES EN DADO CASO DE TENER 1 DIGITO
            fecha_curso_lista[0] = f'0{fecha_curso_lista[0]}'
        else:
            pass
        horario = entry_horario.get()
        disponibilidad = entry_disponibilidad.get()
        gastos_materiales = entry_gasto_materiales.get()
        info = (nombre_curso, costo, fecha_curso_lista[1],fecha_curso_lista[0],fecha_curso_lista[2], horario, disponibilidad, gastos_materiales)
        if envio_bd_curso(info) == None:
            indicador = ttk.Label(frm, text="EXITO", background='green')
            indicador.grid(column=2, row=7)
            frm.after(3000, lambda: indicador.grid_remove())
        else:
            ttk.Label(frm, text="FALLO", background='red').grid(column=2, row=7)
            



    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text="DAR DE ALTA CURSO").grid(column=1, row=0)
    ttk.Label(frm, text="NOMBRE CURSO").grid(column=1, row=1)
    entry_nombre = ttk.Entry(frm)
    entry_nombre.grid(column=2 , row=1)
    ttk.Label(frm, text="COSTO").grid(column=1, row=2)
    entry_costo = ttk.Entry(frm)
    entry_costo.grid(column=2 , row=2)
    ttk.Label(frm, text="FECHA DEL CURSO").grid(column=1, row=3)
    entry_fecha = ttk.Entry(frm)
    cal = Calendar(frm, selectmode="day", year=2024, month=1, day=1)
    cal.grid(column=2, row=3)
    ttk.Label(frm, text="HORARIO").grid(column=1, row=4)
    entry_horario = ttk.Entry(frm)
    entry_horario.grid(column=2 , row=4)
    ttk.Label(frm, text="DISPONIBILIDAD").grid(column=1, row=5)
    entry_disponibilidad = ttk.Entry(frm)
    entry_disponibilidad.grid(column=2 , row=5)
    ttk.Label(frm, text="COSTO DE MATERIALES").grid(column=1, row=6)
    entry_gasto_materiales = ttk.Entry(frm, state='disable')
    entry_gasto_materiales.grid(column=2 , row=6)
    ttk.Button(frm, text="GUARDAR", command=enviar_curso_a_bd).grid(column=1, row=7)
    ttk.Button(frm, text="CERRAR", command=ventana_secundaria.destroy).grid(column=1, row=8)

    
######################################### MAIN ############################################################
def main():
    root = Tk()
    frm = ttk.Frame(root, padding=50)
    frm.grid()
    ttk.Label(frm, text="ESART SISTEMA ADMINISTRATIVO").grid(column=1, row=0)
    ttk.Button(frm, text="DAR DE ALTA TALLER", command=ventana_alta_taller).grid(column=1, row=1)
    ttk.Button(frm, text="DAR DE BAJA TALLER", command=ventana_baja_taller).grid(column=1, row=2)
    ttk.Button(frm, text="CONSULTAR TALLER", command=ventana_consultar_taller).grid(column=1, row=3)
    ttk.Button(frm, text="INSCRIBIR CLIENTE", command=ventana_inscribir_cliente).grid(column=2, row=1)
    ttk.Button(frm, text="BUSCAR CLIENTE", command=ventana_buscar_cliente).grid(column=2, row=2)
    ttk.Button(frm, text="PAGO CLIENTE", command=ventana_pago_cliente).grid(column=2, row=3)
    ttk.Button(frm, text="ALTA GASTO/INGRESO", command=ventana_ingresar_gasto_ingreso).grid(column=3, row=1)
    ttk.Button(frm, text="CERRAR", command=root.destroy).grid(column=1, row=6)
    #HOLA
    root.mainloop()


if __name__ == '__main__':
    main()