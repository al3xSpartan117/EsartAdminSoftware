import mysql.connector
from sendfun import *
from fun_operativas import *
from tkinter import *
from tkinter import ttk 
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar
from tkinter import messagebox
import funExcel


global password

def ventana_ingresar_gasto_ingreso(): 

    def boton_enviar_funcion(op):
        global elementos_creados
        if op == 'extra':
            fecha = elementos_creados[6].get_date()
            fecha_lista = fecha.split('/')
            fecha_formateada = enlistar_fecha(fecha_lista)
            metodoPago = elementos_creados[8].get()
            info = (elementos_creados[2].get(), 'i', elementos_creados[4].get(), metodoPago, op, 'extra', fecha_formateada[0], fecha_formateada[1], fecha_formateada[2])
            if verificar_campos_vacios(info) and solonumeros(elementos_creados[4].get()):
                estado_envio = enviar_gasto_ingreso_db(info, op=2)
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
        elif op == 'sueldos':
            fecha = elementos_creados[6].get_date()
            fecha_lista = fecha.split('/')
            fecha_formateada = enlistar_fecha(fecha_lista)
            empleado = elementos_creados[2].get().split('-')
            #empleado_lista = empleado.split('-')
            print(empleado)
            info = (empleado[0], 'g', elementos_creados[4].get(), op, 'sueldos', fecha_formateada[0], fecha_formateada[1], fecha_formateada[2])
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

    def desplegar_opciones_sueldos():
        global elementos_creados
        op = 'sueldos'
        label_descripcion = ttk.Label(frm, text='EMPLEADO:')
        label_descripcion.grid(column=0, row=2)
        elementos_creados.append(label_descripcion)#1 elementos creados

        ######################### AQUI SE EXTRAE A LOS EMPLEADOS PARA PODER AGREGARLOS AL COMBOBOX COMO OPCIONES
        personal = extraer_personal()
        personal_lista = []
        for i in personal:
           minilista = []
           for j in i:
               x=str(j)
               minilista.append(x)
           personal_lista.append('-'.join(minilista))
        #########################
        empleados_combobox = ttk.Combobox(frm, values=personal_lista)
        empleados_combobox.grid(column=1, row=2)
        elementos_creados.append(empleados_combobox)#2 elementos creados

        # entry_descripcion = ttk.Entry(frm, width=30)
        # entry_descripcion.grid(column=1,row=2)
        # elementos_creados.append(entry_descripcion)#2 elementos creados


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
        ######################## metodo de pago
        metodos = extraer_tarjetas_bd()
        metodos_lista = ['EFECTIVO'] + formato_a_tarjetas(metodos)
        combobox_metodo = ttk.Combobox(frm, values=metodos_lista)
        combobox_metodo.grid(column=2, row=3)
        elementos_creados.append(combobox_metodo)

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
        elif op == "SUELDOS":
            desplegar_opciones_sueldos()
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
        combobox_op_gasto = ttk.Combobox(frm, values=['TALLER', 'MTNMTO', 'SERVICIO', 'ALIMENTO', 'MOBILIARIO', 'SUELDOS'])
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
            mostrar_cursos_combobox.config(state='disable', width=20)
        else:
            indicador = ttk.Label(frm, text='COINCIDENCIA', background='green')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
            info_lista = []
            for i in informacion:
                formato_codigo_curso = f'{i[0]}-{i[1]}'
                info_lista.append(formato_codigo_curso)
            mostrar_cursos_combobox.config(state='readonly', values=info_lista, width=20)

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
    
    def comando_actualizar_info():
        limpiar_informacion()
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
        global combobox_creados
        info = entrys_creados[i].get()
        metodo = combobox_creados[i].get()
        metodo_lista = [metodo]
        if verificar_campos_vacios(info) and verificar_campos_vacios(metodo_lista):
            x = modificar_pagado_db(cliente, info)
            if x == True:
                fecha = datetime.now()
                fecha_lista = [str(fecha.month), str(fecha.day), str(fecha.year)]
                fecha_organizada = enlistar_fecha(fecha_lista, 'datetime')
                informacion_ingreso = [cliente, 'i', info, metodo, 'taller', taller, fecha_organizada[0], fecha_organizada[1], fecha_organizada[2]]
                enviar_gasto_ingreso_db(informacion_ingreso, op=2)
                indicador = ttk.Label(frm, text='EXITO', background='green')
                indicador.grid(column=9, row=4)
                frm.after(2000, lambda: indicador.grid_remove())
                comando_actualizar_info()
            elif x == 'NO INFO':
                indicador = ttk.Label(frm, text='NO INFO', background='red')
                indicador.grid(column=8, row=4)
                frm.after(1000, lambda: indicador.grid_remove())
        else:
            messagebox.showinfo('ERROR', 'EXISTE ERROR DE CAMPOS')

    def desplegar_informacion(info, costo):
            global labels_creados
            global entrys_creados
            global botones_creados
            global combobox_creados
            combobox_creados = []
            entrys_creados = []
            labels_creados =[]
            botones_creados = []
            total_taller = 0.0
            total_pagado = 0.0
            total_faltante = 0.0
            tarjetas = extraer_tarjetas_bd()
            if tarjetas == 'NO INFO':
                messagebox.showerror('ERROR', 'NO SE ENCONTRO INFORMACION DE TARJETAS')
            elif tarjetas == 'ERROR':
                messagebox.showerror('ERROR', 'ERROR EN BASE DE DATOS')
            else:
                metodos_pago = ['Efectivo']
                metodos_pago = metodos_pago + formato_a_tarjetas(tarjetas)
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
                indicador_pagado = ttk.Label(frm, text=extraer_pagosTotal_clientes(info[i][0], info[i][3]))
                indicador_pagado.grid(column= 4, row= i+5)
                labels_creados.append(indicador_pagado)
                indicador_costo = ttk.Label(frm, text=costo)
                indicador_costo.grid(column= 5, row= i+5)
                labels_creados.append(indicador_costo)
                entry_pago = ttk.Entry(frm, width=5)
                entry_pago.grid(column= 7, row= i+5)
                entrys_creados.append(entry_pago)
                boton_pagar = ttk.Button(frm, text='PAGAR', command=lambda indice=i, cliente=info[i][0], taller=info[i][3]: comando_boton_pagar_bucle(indice, cliente, taller))
                boton_pagar.grid(column=9, row=i+5)
                botones_creados.append(boton_pagar)
                faltante = float(costo[0][0])-float(extraer_pagosTotal_clientes(info[i][0], info[i][3]))
                conversion1 = float(costo[0][0])
                conversion2 = float(extraer_pagosTotal_clientes(info[i][0], info[i][3]))
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
                combobox_tipoPago = ttk.Combobox(frm, values=metodos_pago, width=10)#AQUI SE TIENEN QUE DESPLEGAR LAS TARJETAS DISPONIBLES
                combobox_tipoPago.grid(column=8, row=i+5)
                combobox_creados.append(combobox_tipoPago)
                indicador_nombre2 = ttk.Label(frm, text=info[i][1])
                indicador_nombre2.grid(column=10, row=i+5)
                labels_creados.append(indicador_nombre2)
                #########################################
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
            boton_actualizar = ttk.Button(frm, text='ACTUALIZAR', command=comando_actualizar_info)
            boton_actualizar.grid(column=6,row=2)
            botones_creados.append(boton_actualizar)
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
    # Menú desplegable con los meses y anios
    label_pagocliente = ttk.Label(frm, text='PAGO CLIENTE:')
    label_pagocliente.grid(column=0, row=0)
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    anios = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    mes_combobox = ttk.Combobox(frm, values=meses, state="readonly", width=10)
    mes_combobox.grid(column=1, row=2)
    anio_combobox = ttk.Combobox(frm, values=anios, state='readonly', width=10)
    anio_combobox.grid(column=2, row=2)
    ttk.Label(frm, text='BUSCAR CURSO POR FECHA:').grid(column=0, row=2 )
    ttk.Label(frm, text='MES').grid(column=1, row=1)
    ttk.Label(frm, text='AÑO').grid(column=2, row=1)
    ttk.Label(frm, text='SELECCIONAR TALLER:').grid(column=4, row=1)
    boton_buscar = ttk.Button(frm, text="Buscar", command=buscar_curso_boton)
    boton_buscar.grid(column=3, row=2)
    mostrar_cursos_combobox = ttk.Combobox(frm, state="disable", width=20)
    mostrar_cursos_combobox.grid(column=4, row=2)
    mostrar_cursos_combobox.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox)
    #BUSCAR POR CODIGO
    ttk.Label(frm, text='BUSCAR POR CODIGO:').grid(column=0, row=3)
    entry_codigo = ttk.Entry(frm, width=10)
    entry_codigo.grid(column=1, row=3)
    boton_buscar_pCodigo = ttk.Button(frm, text='BUSCAR', command=comando_buscar_tallerPCodigo)
    boton_buscar_pCodigo.grid(column=2, row=3)
    #NOMBRE CASILLAS
    ttk.Label(frm, text='CODIGO').grid(column=0, row=4)
    ttk.Label(frm, text='NOMBRE').grid(column=1, row=4)
    ttk.Label(frm, text='APELLIDO').grid(column=2, row=4)
    ttk.Label(frm, text='TALLER').grid(column=3, row=4)
    ttk.Label(frm, text='PAGADO').grid(column=4, row=4)
    ttk.Label(frm, text='COSTO').grid(column=5, row=4)
    ttk.Label(frm, text='FALTANTE').grid(column=6, row=4)
    ttk.Label(frm, text='PAGO').grid(column=7, row=4)
    ttk.Label(frm, text='TIPO DE PAGO').grid(column=8, row=4)

############################################### BUSCAR CLIENTE      ##############################################
def ventana_buscar_cliente():
    def comando_boton_buscar_pcodigo():
        global labels_creados
        labels_creados = []
        codigo = entry_codigo.get()
        info = extraer_cliente_pcodigo__bd(codigo)
        if info == 'ERROR':
            indicadorError = ttk.Label(frm, text='ERROR', background='red')
            indicadorError.grid(column=1, row=0)
            frm.after(3000, lambda: indicadorError.grid_remove())
        elif info == 'NO INFO':
            indicadorNoInfo = ttk.Label(frm, text='NO INFO', background='red')
            indicadorNoInfo.grid(column=1, row=0)
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
                    indicador_celular = ttk.Label(frm, text=info[i][5])
                    indicador_celular.grid(column=7, row=i+5)

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
            indicadorError.grid(column=1, row=0)
            frm.after(3000, lambda: indicadorError.grid_remove())
        elif info == 'NO INFO':
            indicadorNoInfo = ttk.Label(frm, text='NO INFO', background='red')
            indicadorNoInfo.grid(column=1, row=0)
            frm.after(3000, lambda: indicadorNoInfo.grid_remove())
        else:
            coincidencias = buscador_de_coincidencias(info, nombre, apellido)
            if coincidencias == []:
                indicadorError = ttk.Label(frm, text='NO INFO', background='red')
                indicadorError.grid(column=1, row=0)
                frm.after(3000, lambda: indicadorError.grid_remove())
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
                    costo = extraer_costo_bd(coincidencias[i][3])
                    print(f'COSTO={costo} coincidencias: {coincidencias[i][3]}')
                    if costo == 'NOT FOUND':
                        indicador_costo = ttk.Label(frm, text='NO INFO', background='red')
                        indicador_costo.grid(column=5, row=i+5)
                        labels_creados.append(indicador_costo)
                    elif costo == 'ERROR':
                        indicador_costo = ttk.Label(frm, text='DB ERROR', background='red')
                        indicador_costo.grid(column=5, row=i+5)
                        labels_creados.append(indicador_costo)
                    else:
                        print('SI ESTA ENTRANDO AL BLOQUE EN REVISION')
                        indicador_costo = ttk.Label(frm, text=costo[0][0])
                        indicador_costo.grid(column=5, row=i+5)
                        labels_creados.append(indicador_costo)
                        costo_float = float(costo[0][0])
                        pagado_float = float(info[i][4])
                        faltante = costo_float-pagado_float
                        indicador_faltante = ttk.Label(frm, text=faltante)
                        indicador_faltante.grid(column=6, row=i+5)
                        labels_creados.append(indicador_costo)

    def comando_boton_buscar_pCelular():
        global labels_creados
        labels_creados = []
        numero = entry_numero.get()
        info = extraer_cliente_pCelular__bd(numero)
        if info == 'ERROR':
            indicadorError = ttk.Label(frm, text='ERROR', background='red')
            indicadorError.grid(column=1, row=0)
            frm.after(3000, lambda: indicadorError.grid_remove())
        elif info == 'NO INFO':
            indicadorNoInfo = ttk.Label(frm, text='NO INFO', background='red')
            indicadorNoInfo.grid(column=1, row=0)
            frm.after(3000, lambda: indicadorNoInfo.grid_remove())
        else:
             for i in range(len(info)):
                indicador_codigo = ttk.Label(frm, text=info[i][0])
                indicador_codigo.grid(column=0, row=i+6)
                labels_creados.append(indicador_codigo)
                indicador_nombre = ttk.Label(frm, text=info[i][1])
                indicador_nombre.grid(column=1, row=i+6)
                labels_creados.append(indicador_nombre)
                indicador_apellido = ttk.Label(frm, text=info[i][2])
                indicador_apellido.grid(column=2, row=i+6)
                labels_creados.append(indicador_apellido)
                indicador_taller = ttk.Label(frm, text=info[i][3])
                indicador_taller.grid(column=3, row=i+6)
                labels_creados.append(indicador_taller)
                indicador_pagado = ttk.Label(frm, text=info[i][4])
                indicador_pagado.grid(column=4, row=i+6)
                labels_creados.append(indicador_pagado)
                costo = extraer_costo_bd(info[i][3])
                if costo == 'NOT FOUND':
                    indicador_costo = ttk.Label(frm, text='NO INFO', background='red')
                    indicador_costo.grid(column=5, row=i+6)
                    labels_creados.append(indicador_costo)
                elif costo == 'ERROR':
                    indicador_costo = ttk.Label(frm, text='DB ERROR', background='red')
                    indicador_costo.grid(column=5, row=i+6)
                    labels_creados.append(indicador_costo)
                else:
                    indicador_costo = ttk.Label(frm, text=costo[0][0])
                    indicador_costo.grid(column=5, row=i+6)
                    labels_creados.append(indicador_costo)
                    costo_float = float(costo[0][0])
                    pagado_float = float(extraer_pagosTotal_clientes(info[i][0],info[i][3]))
                    faltante = costo_float-pagado_float
                    indicador_faltante = ttk.Label(frm, text=faltante)
                    indicador_faltante.grid(column=6, row=i+6)
                    labels_creados.append(indicador_costo)
                    indicador_celular = ttk.Label(frm, text=info[i][5])
                    indicador_celular.grid(column=7, row=i+6)


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
    ttk.Label(frm, text="POR CELULAR:").grid(column=0, row=4)
    entry_numero = ttk.Entry(frm)
    entry_numero.grid(column=1, row=4)
    boton_buscar_numero = ttk.Button(frm, text='BUSCAR', command=comando_boton_buscar_pCelular)
    boton_buscar_numero.grid(column=2, row=4)
    ####INDICADORES DE INFORMACION DE CLIENTE
    ttk.Label(frm, text='CODIGO').grid(column=0,row=5)
    ttk.Label(frm, text='NOMBRE').grid(column=1,row=5)
    ttk.Label(frm, text='APELLIDO').grid(column=2,row=5)
    ttk.Label(frm, text='TALLER').grid(column=3,row=5)
    ttk.Label(frm, text='PAGADO').grid(column=4,row=5)
    ttk.Label(frm, text='COSTO').grid(column=5,row=5)
    ttk.Label(frm, text='FALTANTE').grid(column=6,row=5)
    ttk.Label(frm, text='TELEFONO').grid(column=7,row=5)

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
        for label in labels_creados1:
            label.destroy()
        mes_combobox.config(state='normal')
        anio_combobox.config(state='normal')
        mostrar_cursos_combobox.config(state='normal')
        boton_buscar_pCodigo.config(state='normal')
        boton_buscar.config(state='normal')
            
    def comando_actualizar_info(): 

        limpiar_informacion()
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
   
    def desplegar_informacion(info, costo):
            global labels_creados1
            labels_creados1 =[]
            total_taller = 0.0
            total_pagado = 0.0
            total_faltante = 0.0
            cantidad_clientes = 0
            for i in range(0, len(info)):
                indicador_codigo = ttk.Label(frm, text=info[i][0],border=100)
                indicador_codigo.grid(column= 0, row= i+5)
                if ((i+5)%2)==0: indicador_codigo.configure(relief='groove')
                labels_creados1.append(indicador_codigo)
                indicador_nombre = ttk.Label(frm, text=info[i][1])
                indicador_nombre.grid(column= 1, row= i+5)
                if ((i+5)%2)==0: indicador_nombre.configure(relief='groove')
                labels_creados1.append(indicador_nombre)
                indicador_apellido = ttk.Label(frm, text=info[i][2])
                indicador_apellido.grid(column= 2, row= i+5)
                if ((i+5)%2)==0: indicador_apellido.configure(relief='groove')
                labels_creados1.append(indicador_apellido)
                indicador_taller = ttk.Label(frm, text=info[i][3])
                indicador_taller.grid(column= 3, row= i+5)
                if ((i+5)%2)==0: indicador_taller.configure(relief='groove')
                labels_creados1.append(indicador_taller)
                indicador_pagado = ttk.Label(frm, text=extraer_pagosTotal_clientes(info[i][0],info[i][3]))
                indicador_pagado.grid(column= 4, row= i+5)
                if ((i+5)%2)==0: indicador_pagado.configure(relief='groove')
                labels_creados1.append(indicador_pagado)
                indicador_costo = ttk.Label(frm, text=costo)
                indicador_costo.grid(column= 5, row= i+5)
                if ((i+5)%2)==0: indicador_costo.configure(relief='groove')
                labels_creados1.append(indicador_costo)
                try:
                    faltante = float(costo[0][0])-float(extraer_pagosTotal_clientes(info[i][0],info[i][3]))
                except ValueError:
                    faltante = 0
                conversion1 = float(costo[0][0])
                conversion2 = float(extraer_pagosTotal_clientes(info[i][0],info[i][3]))
                total_taller += conversion1
                total_pagado += conversion2
                ultimo_label = i+5
                if faltante <= 0:
                    indicador_faltante = ttk.Label(frm, text='PAGADO', background='green')
                    indicador_faltante.grid(column= 6, row= i+5)
                    if ((i+5)%2)==0: indicador_faltante.configure(relief='groove')
                    labels_creados1.append(indicador_faltante)
                else:
                    indicador_faltante = ttk.Label(frm, text=faltante)
                    indicador_faltante.grid(column= 6, row= i+5)
                    if ((i+5)%2)==0: indicador_faltante.configure(relief='groove')
                    labels_creados1.append(indicador_faltante)
                    total_faltante += faltante
                indicador_nombre2 = ttk.Label(frm, text=info[i][1])
                indicador_nombre2.grid(column=7, row=i+5)
                if ((i+5)%2)==0: indicador_nombre2.configure(relief='groove')
                labels_creados1.append(indicador_nombre2)
                indicador_telefono = ttk.Label(frm, text=info[i][5])
                indicador_telefono.grid(column=8, row=i+5)
                if ((i+5)%2)==0: indicador_telefono.configure(relief='groove')
                labels_creados1.append(indicador_telefono)
                cantidad_clientes += 1
            indicador_total_taller = ttk.Label(frm, text=total_taller, background='#add8e6')
            indicador_total_taller.grid(column= 5, row= ultimo_label+1)
            labels_creados1.append(indicador_total_taller)
            indicador_total_pagado = ttk.Label(frm, text=total_pagado, background='#add8e6')
            indicador_total_pagado.grid(column= 4, row= ultimo_label+1)
            labels_creados1.append(indicador_total_pagado)
            indicador_total_faltante = ttk.Label(frm, text=total_faltante, background='#add8e6')
            indicador_total_faltante.grid(column= 6, row= ultimo_label+1)
            labels_creados1.append(indicador_total_faltante)
            label_total = ttk.Label(frm, text='TOTAL', background='#add8e6')
            label_total.grid(column= 3, row= ultimo_label+1)
            labels_creados1.append(label_total)
            boton_limpiar = ttk.Button(frm, text='LIMPIAR', command=limpiar_informacion)
            boton_limpiar.grid(column=5, row=2)
            labels_creados1.append(boton_limpiar)
            boton_actualizar = ttk.Button(frm, text='ACTUALIZAR', command=comando_actualizar_info)
            boton_actualizar.grid(column=6, row=2)
            labels_creados1.append(boton_actualizar)
            try:
             labels_creados1.append[boton_actualizar]#guardamos en labels en boton ya que no afecta el funcionamiento
            except TypeError:
                pass
            ###########RENDIMIENTO TALLER
            taller = mostrar_cursos_combobox.get()
            taller_lista = taller.split('-')
            rendimiento = informacion_rendimiento(taller_lista[0])#[monto_total_gastos, monto_total_ingresos, ganancia, rendimiento, disponibilidad[0][0]]
            rendimiento = rendimiento + [cantidad_clientes]
            label_rendimineto = ttk.Label(frm, text='RENDIMIENTO DE TALLER')
            label_rendimineto.grid(column=0, row=ultimo_label+2)
            labels_creados1.append(label_rendimineto)
            label_ingresos = ttk.Label(frm, text='INGRESOS')
            label_ingresos.grid(column=0, row=ultimo_label+3)
            labels_creados1.append(label_ingresos)
            label_gastos = ttk.Label(frm, text='GASTOS')
            label_gastos.grid(column=1, row=ultimo_label+3)
            labels_creados1.append(label_gastos)
            label_disponibilidad = ttk.Label(frm, text='GANANCIA')
            label_disponibilidad.grid(column=2, row=ultimo_label+3)
            labels_creados1.append(label_disponibilidad)
            label_disponibilidad = ttk.Label(frm, text='RENDIMIENTO %')
            label_disponibilidad.grid(column=3, row=ultimo_label+3)
            labels_creados1.append(label_disponibilidad)
            label_disponibilidad = ttk.Label(frm, text='DISPONIBILIDAD')
            label_disponibilidad.grid(column=4, row=ultimo_label+3)
            labels_creados1.append(label_disponibilidad)
            ############INFORMACION
            label_ingresos_info = ttk.Label(frm, text=rendimiento[1])
            label_ingresos_info.grid(column=0, row=ultimo_label+4)
            labels_creados1.append(label_ingresos_info)
            label_gastos_info = ttk.Label(frm, text=rendimiento[0])
            label_gastos_info.grid(column=1, row=ultimo_label+4)
            labels_creados1.append(label_gastos_info)
            x = rendimiento[3]
            if x < 0.0:
                label_ganancia_info = ttk.Label(frm, text=rendimiento[2], background='red')
                label_ganancia_info.grid(column=2, row=ultimo_label+4)
                labels_creados1.append(label_ganancia_info)
                label_rendimiento_info = ttk.Label(frm, text=round(rendimiento[3],2), background='red')
                label_rendimiento_info.grid(column=3, row=ultimo_label+4)
                labels_creados1.append(label_rendimiento_info)
            elif x > 0.0 and x < 50.0:
                label_ganancia_info = ttk.Label(frm, text=rendimiento[2], background='yellow')
                label_ganancia_info.grid(column=2, row=ultimo_label+4)
                labels_creados1.append(label_ganancia_info)
                label_rendimiento_info = ttk.Label(frm, text=round(rendimiento[3],2), background='yellow')
                label_rendimiento_info.grid(column=3, row=ultimo_label+4)
                labels_creados1.append(label_rendimiento_info)
            elif x > 49.00:
                label_ganancia_info = ttk.Label(frm, text=rendimiento[2], background='green')
                label_ganancia_info.grid(column=2, row=ultimo_label+4)
                labels_creados1.append(label_ganancia_info)
                label_rendimiento_info = ttk.Label(frm, text=round(rendimiento[3],2), background='green')
                label_rendimiento_info.grid(column=3, row=ultimo_label+4)
                labels_creados1.append(label_rendimiento_info)
            else:
                print(type(rendimiento[3]))
                messagebox.showinfo('ERROR', 'CASO EXTRAÑO EN rendimiento[2]')
            label_disponibilidad_info = ttk.Label(frm, text=f'{cantidad_clientes}/{rendimiento[4]}')
            label_disponibilidad_info.grid(column=4, row=ultimo_label+4)
            labels_creados1.append(label_disponibilidad_info)
            ###########DESHABILITAR OPCIONES
            mes_combobox.config(state='disable')
            anio_combobox.config(state='disable')
            mostrar_cursos_combobox.config(state='disable')
            boton_buscar_pCodigo.config(state='disable')
            boton_buscar.config(state='disable')
    
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
    mostrar_cursos_combobox = ttk.Combobox(frm, state="disable", width=20)
    mostrar_cursos_combobox.grid(column=4, row=2)
    mostrar_cursos_combobox.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox)
    #BUSCAR POR CODIGO
    ttk.Label(frm, text='BUSCAR POR CODIGO:').grid(column=0, row=3)
    entry_codigo = ttk.Entry(frm)
    entry_codigo.grid(column=1, row=3)
    boton_buscar_pCodigo = ttk.Button(frm, text='BUSCAR', command=comando_buscar_tallerPCodigo)
    boton_buscar_pCodigo.grid(column=2, row=3)
    #NOMBRE CASILLAS
    ttk.Label(frm, text='CODIGO').grid(column=0, row=4)
    ttk.Label(frm, text='NOMBRE').grid(column=1, row=4)
    ttk.Label(frm, text='APELLIDO').grid(column=2, row=4)
    ttk.Label(frm, text='TALLER').grid(column=3, row=4)
    ttk.Label(frm, text='PAGADO').grid(column=4, row=4)
    ttk.Label(frm, text='COSTO').grid(column=5, row=4)
    ttk.Label(frm, text='FALTANTE').grid(column=6, row=4)
    ttk.Label(frm, text='NOMBRE').grid(column=7, row=4)
    ttk.Label(frm, text='TELEFONO').grid(column=8, row=4)

###############################################    INSCRIBIR CLIENTE       #####################################
def ventana_inscribir_cliente():

    def enviar_cliente_boton():
        nombre = nombre_cliente_entry.get()
        apellido = apellido_cliente_entry.get()
        taller = mostrar_cursos_combobox.get()
        taller_lista = taller.split('-')
        pago = pago_cliente_entry.get()
        telefono = entry_telefono.get()
        informacion = (nombre, apellido, taller_lista[0], pago, telefono)
        if verificar_campos_vacios(informacion) and solonumeros(pago) and verificadorCel(telefono):
            resultado_envio = enviar_cliente_bd(informacion)
            if resultado_envio == 'ERROR':
                indicador = ttk.Label(frm, text='ERROR AL ENVIAR', background='red')
                indicador.grid(column=1, row=7)
                frm.after(3000, lambda: indicador.grid_remove())
            else:
                indicador = ttk.Label(frm, text='ENVIADO', background='green')
                indicador.grid(column=1, row=7)
                frm.after(3000, lambda: indicador.grid_remove())
                codigo_cliente = extraer_Codecliente_recien_agregado(nombre, apellido, taller_lista[0], pago)
                if codigo_cliente == 'NO INFO':
                    print('NO HAY INFO')
                elif codigo_cliente == "ERROR":
                    print('Hubo error')
                else:
                    fecha = datetime.now()
                    fecha_lista = [str(fecha.month), str(fecha.day), str(fecha.year)]
                    fecha_organizada = enlistar_fecha(fecha_lista, 'datetime')
                    info_gastoIng = [codigo_cliente, 'i',  pago, 'taller', taller_lista[0], fecha_organizada[0], fecha_organizada[1], fecha_organizada[2]]
                    result_envio = enviar_gasto_ingreso_db(info_gastoIng)
                    if result_envio == False:
                        messagebox.showinfo('ERROR', 'DATABASE ERROR-enviar_gasto_ingreso_db(info)')
                    else:
                        indicador2 = ttk.Label(frm, text='ING ENVIADO', background='green')
                        indicador2.grid(column=2, row=7)
                        frm.after(3000, lambda: indicador2.grid_remove())
        else:
            messagebox.showinfo('ERROR','EXISTE ERROR EN CAMPO')

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
    label_mostrar_costo = ttk.Label(frm, text='?')
    label_mostrar_costo.grid(column=1, row=6)
    # Botón para enviar informacion
    boton_enviar = ttk.Button(frm, text="ENVIAR", command=enviar_cliente_boton)
    boton_enviar.grid(column=0, row=7)
    ########### NUMERO DE TELEFONO
    ttk.Label(frm, text='TELEFONO').grid(column=2, row=1)
    entry_telefono = ttk.Entry(frm)
    entry_telefono.grid(column=3, row=1)
    
    
    



    #NOMBRE APELLIDO CURSO FECHA CURSO COSTO DE CURSO
    #PAGO   EL CODIGO DE CLIENTE ES

###############################################     DAR DE BAJA TALLER      ########################################

def ventana_baja_taller():
    def comparar_psw():
        global password
        psw_introducida = intro_psw.get()
        if password == psw_introducida:
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
    intro_psw = ttk.Entry(frm, show='*')
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
        info = (nombre_curso, costo, fecha_curso_lista[1],fecha_curso_lista[0],fecha_curso_lista[2], horario, disponibilidad)
        if verificar_campos_vacios(info):
            if envio_bd_curso(info) == None:
                indicador = ttk.Label(frm, text="EXITO", background='green')
                indicador.grid(column=2, row=7)
                frm.after(3000, lambda: indicador.grid_remove())
            else:
                ttk.Label(frm, text="FALLO", background='red').grid(column=2, row=7)
        else:
            messagebox.showinfo('ERROR', 'Existe error en campos')
            



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
    fecha = datetime.now()
    cal = Calendar(frm, selectmode="day", year=fecha.year, month=fecha.month, day=fecha.day)
    cal.grid(column=2, row=3)
    ttk.Label(frm, text="HORARIO").grid(column=1, row=4)
    entry_horario = ttk.Entry(frm)
    entry_horario.grid(column=2 , row=4)
    ttk.Label(frm, text="DISPONIBILIDAD").grid(column=1, row=5)
    entry_disponibilidad = ttk.Entry(frm)
    entry_disponibilidad.grid(column=2 , row=5)
    ttk.Button(frm, text="GUARDAR", command=enviar_curso_a_bd).grid(column=1, row=7)
    ttk.Button(frm, text="CERRAR", command=ventana_secundaria.destroy).grid(column=1, row=8)

########################################## VENTANA ALTA PERSONAL #####################################
def ventana_alta_personal():
    def enviar_personal():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        apellido2 = entry_apellido2.get()
        privilegio = combx_privilegios.get()
        usuario = entry_usuario.get()
        password = entry_contrasena.get()
        info = (nombre, apellido, apellido2, privilegio, usuario, encriptador(password))
        if verificar_campos_vacios(info):
            resultado = enviar_personal_bd(info)
            if resultado == True:
                indicador = ttk.Label(frm, text='ENVIADO', background='green')
                indicador.grid(column=1, row=0)
            else:
                indicador = ttk.Label(frm, text='ERROR', background='red')
                indicador.grid(column=1, row=0)
        else:
            messagebox.showinfo('ERROR', 'Error en campos')

        
        

    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text='DAR DE ALTA PERSONAL').grid(column=0, row=0)
    ttk.Label(frm, text='NOMBRE:').grid(column=0, row=1)
    entry_nombre = ttk.Entry(frm)
    entry_nombre.grid(column=1, row=1)

    ttk.Label(frm, text='APELLIDO').grid(column=0, row=2)
    entry_apellido = ttk.Entry(frm)
    entry_apellido.grid(column=1, row=2)
    
    ttk.Label(frm, text='APELLIDO 2').grid(column=0, row=3)
    entry_apellido2 = ttk.Entry(frm)
    entry_apellido2.grid(column=1, row=3)

    ttk.Label(frm, text='PRIVILEGIO').grid(column=0, row=4)
    combx_privilegios = ttk.Combobox(frm, values=['ADMINISTRADOR', 'USUARIO'])
    combx_privilegios.grid(column=1, row=4)

    ttk.Label(frm, text='USUARIO').grid(column=0, row=5)
    entry_usuario = ttk.Entry(frm)
    entry_usuario.grid(column=1, row=5)

    ttk.Label(frm, text='CONTRASEÑA').grid(column=0, row=6)
    entry_contrasena = ttk.Entry(frm)
    entry_contrasena.grid(column=1, row=6)

    boton_enviar = ttk.Button(frm, text='ENVIAR', command=enviar_personal)
    boton_enviar.grid(column=1, row=7)

######################################### VENTANA ALTA TARJETA ######################################

def ventana_alta_tarjeta():
    def enviar_tarjeta():
        titular = entry_titular.get()
        digitos = entry_4digitos.get()
        banco = entry_banco.get()
        vencimiento = entry_vencimiento.get()
        info = [titular, digitos, banco.upper(), vencimiento]
        if verificar_campos_vacios(info) and solonumeros(digitos):
            resultado_envio = enviar_tarjeta_bd(info)
            if resultado_envio == True:
                indicador = ttk.Label(frm, text='ENVIADO', background='green')
                indicador.grid(column=1, row=0)
                frm.after(3000, lambda: indicador.grid_remove())
            else:
                indicador = ttk.Label(frm, text='NO ENVIADO', background='red')
                indicador.grid(column=1, row=0)
                frm.after(3000, lambda: indicador.grid_remove())
        else:
            messagebox.showinfo('ERROR', 'EXISTE ERROR EN CAMPOS')

    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text='DAR DE ALTA TARJETA').grid(column=0, row=0)
    ttk.Label(frm, text='TITULAR:').grid(column=0, row=1)
    entry_titular = ttk.Entry(frm)
    entry_titular.grid(column=1, row=1)

    ttk.Label(frm, text='ULTIMOS 4 DIGITOS').grid(column=0, row=2)
    entry_4digitos = ttk.Entry(frm)
    entry_4digitos.grid(column=1, row=2)
    
    ttk.Label(frm, text='BANCO').grid(column=0, row=3)
    entry_banco = ttk.Entry(frm)
    entry_banco.grid(column=1, row=3)

    ttk.Label(frm, text='VENCIMIENTO').grid(column=0, row=4)
    entry_vencimiento = ttk.Entry(frm)
    entry_vencimiento.grid(column=1, row=4)
    boton_enviar = ttk.Button(frm, text='ENVIAR', command=enviar_tarjeta)
    boton_enviar.grid(column=1, row=7)

########################################## VENTANA TRANSFERIR EXCEDENTE ##############################

def ventana_trasnferir_exedente():
    widthGeneral = 20
    global labels_creados2
    labels_creados2 = []
    def buscar_curso_boton(op=0):
        print(op)
        widthGeneral = 20
        if op == 1:
            mes_seleccionado = mes_combobox2.get()
            mostrar_cursos_combobox2.set('')
            mostrar_clientes_combobox2.set('')
        else:
            mostrar_cursos_combobox.set('')
            mostrar_clientes_combobox.set('')
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
        if op == 1:
            anio_seleccionado = anio_combobox2.get()
        else:
            anio_seleccionado = anio_combobox.get()
        informacion = extraer_talleres_bd(mes_en_numero[mes_seleccionado], anio_seleccionado)
        if informacion == "ERROR":
            indicador = ttk.Label(frm, text='DATABASE ERROR', background='red')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
            if op == 1:
                mostrar_cursos_combobox2.set('')
                mostrar_cursos_combobox2.config(state='disable', width=widthGeneral)
                mostrar_clientes_combobox2.set('')
                mostrar_clientes_combobox2.config(state='disable', width=widthGeneral)
            else:
                mostrar_cursos_combobox.set('')
                mostrar_cursos_combobox.config(state='disable', width=widthGeneral)  
                mostrar_clientes_combobox.set('')
                mostrar_clientes_combobox.config(state='disable', width=widthGeneral)  
        elif informacion == 'NOT FOUND':
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
            if op == 1:
                mostrar_cursos_combobox2.set('')
                mostrar_cursos_combobox2.config(state='disable', width=widthGeneral)
                mostrar_clientes_combobox2.set('')
                mostrar_clientes_combobox2.config(state='disable', width=widthGeneral)
            else:
                mostrar_cursos_combobox.set('')
                mostrar_cursos_combobox.config(state='disable', width=widthGeneral)  
                mostrar_clientes_combobox.set('')
                mostrar_clientes_combobox.config(state='disable', width=widthGeneral)  
        else:
            indicador = ttk.Label(frm, text='COINCIDENCIA', background='green')
            indicador.grid(column=3, row=1)
            frm.after(3000, lambda: indicador.grid_remove())
            info_lista = []
            for i in informacion:
                formato_codigo_curso = f'{i[0]}-{i[1]}'
                info_lista.append(formato_codigo_curso)
            if op == 1:
                mostrar_cursos_combobox2.config(state='readonly', values=info_lista, width=widthGeneral)
            else:
                mostrar_cursos_combobox.config(state='readonly', values=info_lista, width=widthGeneral)

    def opcion_seleccionada_combobox_cursos(event):
        boton_confirmar.config(state='disable')
        mostrar_clientes_combobox.set('')
        info_curso = mostrar_cursos_combobox.get()
        info_curso_lista = info_curso.split('-')
        clientes = extraer_clientes_bd(info_curso_lista[0])
        if clientes == 'NO INFO':
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=1, row=0)
            mostrar_clientes_combobox.configure(values=[''], state='disable')
            frm.after(3000, lambda: indicador.grid_remove())
        elif clientes == 'ERROR':
            indicador = ttk.Label(frm, text='DB ERROR', background='red')
            indicador.grid(column=1, row=0)
            mostrar_clientes_combobox.configure(values=[''], state='disable')
            frm.after(3000, lambda: indicador.grid_remove())
        else:
           clientes_formateados = formato_a_clientes(clientes)
           mostrar_clientes_combobox.configure(state='enable', values=clientes_formateados)

    def opcion_seleccionada_combobox_cursos2(event):
        mostrar_clientes_combobox2.set('')
        info_curso = mostrar_cursos_combobox2.get()
        info_curso_lista = info_curso.split('-')
        clientes = extraer_clientes_bd(info_curso_lista[0])
        if clientes == 'NO INFO':
            indicador = ttk.Label(frm, text='NO INFO', background='red')
            indicador.grid(column=1, row=0)
            mostrar_clientes_combobox2.configure(values=[''], state='disable')
            frm.after(3000, lambda: indicador.grid_remove())
        elif clientes == 'ERROR':
            indicador = ttk.Label(frm, text='DB ERROR', background='red')
            indicador.grid(column=1, row=0)
            mostrar_clientes_combobox2.configure(values=[''], state='disable')
            frm.after(3000, lambda: indicador.grid_remove())
        else:
           clientes_formateados = formato_a_clientes(clientes)
           mostrar_clientes_combobox2.configure(state='enable', values=clientes_formateados)
    
    def opcion_seleccionada_combobox_clientes(event):
        boton_confirmar.config(state='disable')

    def boton_comprobar_comando():
        global labels_creados2
        eliminar_elementos_creados(labels_creados2)
        labels_creados2 = []
        cliente_t = mostrar_clientes_combobox.get()
        cliente_r = mostrar_clientes_combobox2.get()
        if verificar_campos_vacios([cliente_t, cliente_r]):
            cliente_t_lista = cliente_t.split('-')
            excedente = calcular_excedente(int(cliente_t_lista[0]), int(cliente_t_lista[2]))
            if excedente >= 0:
                messagebox.showinfo('AVISO', 'NO EXISTE EXCEDENTE PARA ESTE CLIENTE')
            elif excedente < 0:
                excedente = abs(excedente)
                indicador_transaccion = ttk.Label(frm, text='RESUMEN DE TRANSACCION:')
                indicador_transaccion.grid(column=0, row=4)
                labels_creados2.append(indicador_transaccion)
                indicador_excedente = ttk.Label(frm, text='EXCEDENTE CALCULADO:')
                indicador_excedente.grid(column=0, row=5)
                labels_creados2.append(indicador_excedente)
                label_excedente = ttk.Label(frm, text=excedente)
                label_excedente.grid(column=0, row=6)
                boton_confirmar.config(state='enable')
            else:
                messagebox.showinfo('ERROR', 'ERROR EN VARIABLE excedente, boton_comprobar_comando()')
        else:
            messagebox.showinfo('ERROR', 'ERROR EN CAMPOS')

    def boton_confirmar_comando():
        eliminar_elementos_creados(labels_creados2)
        cliente_t = mostrar_clientes_combobox.get()
        cliente_r = mostrar_clientes_combobox2.get()
        if verificar_campos_vacios([cliente_t, cliente_r]):
            cliente_t_lista = cliente_t.split('-')
            cliente_r_lista = cliente_r.split('-')
            excedente = calcular_excedente(int(cliente_t_lista[0]), int(cliente_t_lista[2]))
            fecha = datetime.now()
            fecha_lista = [str(fecha.day), str(fecha.month), str(fecha.year)]
            fecha_organizada = enlistar_fecha(fecha_lista, 'datetime')
            info = [int(cliente_t_lista[0]), 'i', excedente, 'AJUSTE', 'taller', int(cliente_t_lista[2]), fecha_organizada[0], fecha_organizada[1], fecha_organizada[2]]#descripcion, tipo, monto, metodo, area, zona, dia, mes, anio
            resultado_envio_ajuste = enviar_gasto_ingreso_db(info, op=2)
            if resultado_envio_ajuste == True:
                excedente = abs(excedente)
                info = [int(cliente_r_lista[0]), 'i', excedente, 'AJUSTE', 'taller', int(cliente_r_lista[2]), fecha_organizada[0], fecha_organizada[1], fecha_organizada[2]]#descripcion, tipo, monto, metodo, area, zona, dia, mes, anio
                resultado_envio_ingreso = enviar_gasto_ingreso_db(info, op=2)
                if resultado_envio_ingreso == True:
                    indicador = ttk.Label(frm, text='ENVIADO', background='GREEN')
                    indicador.grid(column=1, row=0)
                    frm.after(2000,lambda: indicador.grid_remove())
                elif resultado_envio_ingreso == False:
                    messagebox.showerror('ERROR', 'Se dio de alta el ajuste para el cliente con excedente pero ocurrio un error al enviar dicho ingreso al nuevo cliente, hay que eliminar el ajuste del cliente con excedente si no mostrara informacion erronea dicho taller')
                else:
                    messagebox.showinfo('ERROR', 'CASO EXTRAÑO CON VARIABLE resultado_envio_ingreso, hay que eliminar el ajuste del cliente con excedente ya que no se ha logrado enviar dicho excedente al cliente que recibe')
            elif resultado_envio_ajuste == False:
                indicador = ttk.Label(frm, text='ERROR', background='red')
                indicador.grid(column=1, row=0)
                frm.after(2000,lambda: indicador.grid_remove())
            else:
                messagebox.showerror('ERROR', 'Caso extraño en valor variable resultado_envio, boton_confirmar_comando')

    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text='TRANSFERIR EXCEDENTE:').grid(column=0, row=0)
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    anios = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    mes_combobox = ttk.Combobox(frm, values=meses, state="readonly", width=10)
    mes_combobox.grid(column=1, row=2)
    anio_combobox = ttk.Combobox(frm, values=anios, state='readonly', width=10)
    anio_combobox.grid(column=2, row=2)
    ttk.Label(frm, text='SELECCIONAR CLIENTE CON EXCEDENTE:').grid(column=0, row=2 )
    ttk.Label(frm, text='MES').grid(column=1, row=1)
    ttk.Label(frm, text='AÑO').grid(column=2, row=1)
    ttk.Label(frm, text='SELECCIONAR TALLER:').grid(column=4, row=1)
    ttk.Label(frm, text='CLIENTE:').grid(column=5, row=1)
    boton_buscar = ttk.Button(frm, text="Buscar", command=buscar_curso_boton)
    boton_buscar.grid(column=3, row=2)
    mostrar_cursos_combobox = ttk.Combobox(frm, state="disable", width=widthGeneral)
    mostrar_cursos_combobox.grid(column=4, row=2)
    mostrar_cursos_combobox.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox_cursos)
    mostrar_clientes_combobox = ttk.Combobox(frm, state="disable", width=widthGeneral)
    mostrar_clientes_combobox.grid(column=5, row=2)
    mostrar_clientes_combobox.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox_clientes)
    ####################CLIENTE AL QUE SE LE TRANSFERIRA#############
    mes_combobox2 = ttk.Combobox(frm, values=meses, state="readonly", width=10)
    mes_combobox2.grid(column=1, row=3)
    anio_combobox2 = ttk.Combobox(frm, values=anios, state='readonly', width=10)
    anio_combobox2.grid(column=2, row=3)
    ttk.Label(frm, text='SELECCIONAR CLIENTE QUE RECIBE:').grid(column=0, row=3 )
    boton_buscar2 = ttk.Button(frm, text="Buscar", command=lambda op=1: buscar_curso_boton(op))
    boton_buscar2.grid(column=3, row=3)
    mostrar_cursos_combobox2 = ttk.Combobox(frm, state="disable", width=widthGeneral)
    mostrar_cursos_combobox2.grid(column=4, row=3)
    mostrar_cursos_combobox2.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox_cursos2)
    mostrar_clientes_combobox2 = ttk.Combobox(frm, state="disable", width=widthGeneral)
    mostrar_clientes_combobox2.grid(column=5, row=3)
    mostrar_clientes_combobox2.bind("<<ComboboxSelected>>", opcion_seleccionada_combobox_clientes)
    boton_comprobar = ttk.Button(frm, text='COMPROBAR', command=boton_comprobar_comando)
    boton_comprobar.grid(column=5,row=10)
    boton_confirmar = ttk.Button(frm, text='CONFIRMAR', state='disable', command=boton_confirmar_comando)
    boton_confirmar.grid(column=5,row=11)

########################################## VENTANA RENDIMIENTO TALLERES ##############################
    
def ventana_rendimiento_talleres():
    global labels_creados3
    labels_creados3=[]
    def boton_calcular_comando():
        dia_inicio = combobox_dia1.get()
        mes_inicio = combobox_mes1.get()
        anio_inicio = combobox_anio1.get()
        dia_fin = combobox_dia2.get()
        mes_fin = combobox_mes2.get()
        anio_fin = combobox_anio2.get()
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
        fechas_lista = [dia_inicio, mes_en_numero[mes_inicio], anio_inicio, dia_fin, mes_en_numero[mes_fin], anio_fin]
        if verificar_campos_vacios(fechas_lista):
            clientes = extraer_talleres_rangoFechas_db(fechas_lista)
            if clientes == 'NO INFO':
                indicador = ttk.Label(frm, text='NO INFO', background='red')
                frm.after(3000, lambda: indicador.grid_remove())
                indicador.grid(column=3, row=1)
            elif clientes == 'ERROR':
                indicador = ttk.Label(frm, text='DB ERROR', background='red')
                frm.after(3000, lambda: indicador.grid_remove())
                indicador.grid(column=3, row=1)
            else:
                info_rendimientos = informacion_rendimiento_talleres(clientes)#[monto_total_gastos, monto_total_ingresos, ganancia, rendimiento, disponibilidad[0][0]]
                rendimiento_global = calculo_rendimientos_talleres(info_rendimientos)
                indicador_ingresos = ttk.Label(frm, text='INGRESOS')
                indicador_ingresos.grid(column=0, row=4)
                labels_creados3.append(indicador_ingresos)
                indicador_gastos = ttk.Label(frm, text='GASTOS')
                indicador_gastos.grid(column=1, row=4)
                labels_creados3.append(indicador_gastos)
                indicador_ganancia = ttk.Label(frm, text='GANANCIA')
                indicador_ganancia.grid(column=2, row=4)
                labels_creados3.append(indicador_ganancia)
                indicador_rendimiento = ttk.Label(frm, text='RENDIMIENTO')
                indicador_rendimiento.grid(column=3, row=4)
                labels_creados3.append(indicador_rendimiento)
                ########################################
                label_ingresos = ttk.Label(frm, text=rendimiento_global[1])
                label_ingresos.grid(column=0, row=5)
                labels_creados3.append(label_ingresos)
                label_gastos = ttk.Label(frm, text=rendimiento_global[0])
                label_gastos.grid(column=1, row=5)
                labels_creados3.append(label_gastos)
                label_ganancia = ttk.Label(frm, text=rendimiento_global[2])
                label_ganancia.grid(column=2, row=5)
                labels_creados3.append(label_ganancia)
                label_rendimiento = ttk.Label(frm, text=rendimiento_global[3])
                label_rendimiento.grid(column=3, row=5)
                labels_creados3.append(label_rendimiento)

                



    global width_rendimiento 
    width_rendimiento = 10
    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text='RENDIMIENTO TALLERES').grid(column=0,row=0)
    ttk.Label(frm, text='Periodo').grid(column=0,row=1)
    ttk.Label(frm, text='De:').grid(column=0, row=2)
    dias = []
    for i in range(1,32):
        dias.append(str(i))
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    anios = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    combobox_dia1 = ttk.Combobox(frm, width=width_rendimiento, values=dias, state='readonly')
    combobox_dia1.grid(column=1,row=2)
    combobox_mes1 = ttk.Combobox(frm,width=width_rendimiento, values=meses, state='readonly')
    combobox_mes1.grid(column=2,row=2)
    combobox_anio1 = ttk.Combobox(frm,width=width_rendimiento, values=anios, state='readonly')
    combobox_anio1.grid(column=3,row=2)
    ttk.Label(frm, text='A:').grid(column=0, row=3)
    combobox_dia2 = ttk.Combobox(frm,width=width_rendimiento, values=dias, state='readonly')
    combobox_dia2.grid(column=1,row=3)
    combobox_mes2 = ttk.Combobox(frm,width=width_rendimiento, values=meses, state='readonly')
    combobox_mes2.grid(column=2,row=3)
    combobox_anio2 = ttk.Combobox(frm,width=width_rendimiento, values=anios, state='readonly')
    combobox_anio2.grid(column=3,row=3)
    boton_calcular = ttk.Button(frm, text='Calcular', command=boton_calcular_comando)
    boton_calcular.grid(column=4, row=3)

######################################### VENTANA RENDIMIENTO GENERAL #################################
    
def ventana_rendimiento_general():
    global labels_creados4
    global gastosIngresos_extraidos
    labels_creados4=[]
    def boton_calcular_comando():
        global gastosIngresos_extraidos
        dia_inicio = combobox_dia1.get()
        mes_inicio = combobox_mes1.get()
        anio_inicio = combobox_anio1.get()
        dia_fin = combobox_dia2.get()
        mes_fin = combobox_mes2.get()
        anio_fin = combobox_anio2.get()
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
        fechas_lista = [dia_inicio, mes_en_numero[mes_inicio], anio_inicio, dia_fin, mes_en_numero[mes_fin], anio_fin]
        if verificar_campos_vacios(fechas_lista):
            gastos_ingresos = extraer_gastoIngreso_rangoFechas_db(fechas_lista)
            gastosIngresos_extraidos = gastos_ingresos
            if gastos_ingresos == 'NO INFO':
                indicador = ttk.Label(frm, text='NO INFO', background='red')
                frm.after(3000, lambda: indicador.grid_remove())
                indicador.grid(column=3, row=1)
            elif gastos_ingresos == 'ERROR':
                indicador = ttk.Label(frm, text='DB ERROR', background='red')
                frm.after(3000, lambda: indicador.grid_remove())
                indicador.grid(column=3, row=1)
            else:
                rendimiento_global = calcular_rendimiento_general(gastos_ingresos)#[monto_total_gastos, monto_total_ingresos, ganancia, rendimiento, disponibilidad[0][0]]
                if rendimiento_global == 'NO INFO':
                    messagebox.showerror('ERROR', 'LOS GASTOS O LOS INGRESOS SON 0 LO CUAL NO PERMITE QUE EL')
                indicador_ingresos = ttk.Label(frm, text='INGRESOS')
                indicador_ingresos.grid(column=0, row=4)
                labels_creados4.append(indicador_ingresos)
                indicador_gastos = ttk.Label(frm, text='GASTOS')
                indicador_gastos.grid(column=1, row=4)
                labels_creados4.append(indicador_gastos)
                indicador_ganancia = ttk.Label(frm, text='GANANCIA')
                indicador_ganancia.grid(column=2, row=4)
                labels_creados4.append(indicador_ganancia)
                indicador_rendimiento = ttk.Label(frm, text='RENDIMIENTO')
                indicador_rendimiento.grid(column=3, row=4)
                labels_creados4.append(indicador_rendimiento)
                ########################################
                label_ingresos = ttk.Label(frm, text=rendimiento_global[0])
                label_ingresos.grid(column=0, row=5)
                labels_creados4.append(label_ingresos)
                label_gastos = ttk.Label(frm, text=rendimiento_global[1])
                label_gastos.grid(column=1, row=5)
                labels_creados4.append(label_gastos)
                label_ganancia = ttk.Label(frm, text=rendimiento_global[2])
                label_ganancia.grid(column=2, row=5)
                labels_creados4.append(label_ganancia)
                label_rendimiento = ttk.Label(frm, text=rendimiento_global[3])
                label_rendimiento.grid(column=3, row=5)
                labels_creados4.append(label_rendimiento)
                boton_generar_excel = ttk.Button(frm, text='Generar excel', command = boton_generar_excel_comando)
                boton_generar_excel.grid(column=3, row=6)
                
    def boton_generar_excel_comando():
        info_excel_formateada = formato_excel_tablas(gastosIngresos_extraidos, 'gastos')
        funExcel.generar_excel_tablas(info_excel_formateada, 'gastos')
        

    global width_rendimiento 
    width_rendimiento = 10
    ventana_secundaria = tk.Toplevel()
    frm = ttk.Frame(ventana_secundaria, padding=50)
    frm.place(x=100, y=100)
    frm.grid()
    ttk.Label(frm, text='RENDIMIENTO GENERAL').grid(column=0,row=0)
    ttk.Label(frm, text='Periodo').grid(column=0,row=1)
    ttk.Label(frm, text='De:').grid(column=0, row=2)
    dias = []
    for i in range(1,32):
        dias.append(str(i))
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    anios = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    combobox_dia1 = ttk.Combobox(frm, width=width_rendimiento, values=dias, state='readonly')
    combobox_dia1.grid(column=1,row=2)
    combobox_mes1 = ttk.Combobox(frm,width=width_rendimiento, values=meses, state='readonly')
    combobox_mes1.grid(column=2,row=2)
    combobox_anio1 = ttk.Combobox(frm,width=width_rendimiento, values=anios, state='readonly')
    combobox_anio1.grid(column=3,row=2)
    ttk.Label(frm, text='A:').grid(column=0, row=3)
    combobox_dia2 = ttk.Combobox(frm,width=width_rendimiento, values=dias, state='readonly')
    combobox_dia2.grid(column=1,row=3)
    combobox_mes2 = ttk.Combobox(frm,width=width_rendimiento, values=meses, state='readonly')
    combobox_mes2.grid(column=2,row=3)
    combobox_anio2 = ttk.Combobox(frm,width=width_rendimiento, values=anios, state='readonly')
    combobox_anio2.grid(column=3,row=3)
    boton_calcular = ttk.Button(frm, text='Calcular', command=boton_calcular_comando)
    boton_calcular.grid(column=4, row=3)

######################################### MAIN ############################################################
def main():
    def verificar_usuario():
        global password
        usuario_ingresado = entry_usuario.get()
        psw_ingresado = entry_psw.get()
        pswReal = extraer_personal_pverificar(usuario_ingresado)
        if pswReal == 'NO INFO':
            messagebox.showinfo('ERROR', 'NO COINCIDE NINGUN USUARIO')
        elif pswReal == 'ERROR':
            messagebox.showinfo('ERROR', 'ERROR DB')
        elif psw_ingresado == desencriptador(pswReal[0][0]):
            password = desencriptador(pswReal[0][0])
            if pswReal[0][1] == 'ADMINISTRADOR':
                boton_altaPersonal.config(state='enable')
                boton_altaTaller.config(state='enable')
                boton_bajaTaller.config(state='enable')
                boton_buscarCliente.config(state='enable')
                boton_consultaTaller.config(state='enable')
                boton_gastoIngreso.config(state='enable')
                boton_inscribirCliente.config(state='enable')
                boton_pagoCliente.config(state='enable')
                boton_pagoCliente.config(state='enable')
                boton_altaTarjeta.config(state='enable')
                boton_TransExcedente.config(state='enable')
            elif pswReal[0][1] == 'USUARIO':
                #boton_altaPersonal.config(state='enable')
                #boton_altaTaller.config(state='enable')
                #boton_bajaTaller.config(state='enable')
                boton_buscarCliente.config(state='enable')
                boton_consultaTaller.config(state='enable')
                #boton_gastoIngreso.config(state='enable')
                boton_inscribirCliente.config(state='enable')
                boton_pagoCliente.config(state='enable')
                #boton_altaTarjeta.config(state='enable')
                #boton_pagoCliente.config(state='enable')
            else:
                messagebox.showinfo('ERROR', 'Error en variable pswReal[0][1]')
        
        elif pswReal != psw_ingresado:
            messagebox.showinfo('ERROR', 'LA CONTRASEÑA NO COINCIDE')
        else:
            messagebox.showinfo('ERROR', 'ERROR EXTRAÑO VARIABLE pswReal')
            

    root = Tk()
    frm = ttk.Frame(root, padding=50)
    frm.grid()
    ttk.Label(frm, text="ESART SISTEMA ADMINISTRATIVO").grid(column=1, row=0)
    ttk.Label(frm, text='INICIAR SESION:').grid(column=1, row=2)
    ttk.Label(frm, text='USUARIO:').grid(column=2, row=1)
    ttk.Label(frm, text='CONTRASEÑA:').grid(column=3, row=1)
    entry_usuario = ttk.Entry(frm)
    entry_usuario.grid(column=2, row=2)
    entry_psw = ttk.Entry(frm, show='*')
    entry_psw.grid(column=3, row=2)
    ttk.Button(frm, text='ENTER', command=verificar_usuario).grid(column=4, row=2)
    boton_altaTaller = ttk.Button(frm, text="DAR DE ALTA TALLER", command=ventana_alta_taller)
    boton_altaTaller.grid(column=1, row=3)
    boton_bajaTaller = ttk.Button(frm, text="DAR DE BAJA TALLER", command=ventana_baja_taller)
    boton_bajaTaller.grid(column=1, row=4)
    boton_consultaTaller = ttk.Button(frm, text="CONSULTAR TALLER", command=ventana_consultar_taller)
    boton_consultaTaller.grid(column=1, row=5)
    boton_TransExcedente = ttk.Button(frm, text="RENDIMIENTO TALLERES", command=ventana_rendimiento_talleres)
    boton_TransExcedente.grid(column=1, row=6)
    boton_inscribirCliente = ttk.Button(frm, text="INSCRIBIR CLIENTE", command=ventana_inscribir_cliente)
    boton_inscribirCliente.grid(column=2, row=3)
    boton_buscarCliente = ttk.Button(frm, text="BUSCAR CLIENTE", command=ventana_buscar_cliente)
    boton_buscarCliente.grid(column=2, row=4)
    boton_pagoCliente = ttk.Button(frm, text="PAGO CLIENTE", command=ventana_pago_cliente)
    boton_pagoCliente.grid(column=2, row=5)
    boton_TransExcedente = ttk.Button(frm, text="TRANSFERIR EXC", command=ventana_trasnferir_exedente)
    boton_TransExcedente.grid(column=2, row=6)
    boton_gastoIngreso = ttk.Button(frm, text="ALTA GASTO/INGRESO", command=ventana_ingresar_gasto_ingreso)
    boton_gastoIngreso.grid(column=3, row=3)
    boton_altaTarjeta = ttk.Button(frm, text="ALTA TARJETA", command=ventana_alta_tarjeta)
    boton_altaTarjeta.grid(column=3, row=4)
    boton_rendimientoGeneral = ttk.Button(frm, text="RENDIMIENTO GENERAL", command=ventana_rendimiento_general)
    boton_rendimientoGeneral.grid(column=3, row=5)
    boton_altaPersonal = ttk.Button(frm, text="ALTA PERSONAL", command=ventana_alta_personal)
    boton_altaPersonal.grid(column=4, row=3)

    ttk.Button(frm, text="CERRAR", command=root.destroy).grid(column=1, row=8)
    #HOLA
    root.mainloop()


if __name__ == '__main__':
    main()