import pandas as pd
from datetime import datetime
def generar_excel_tablas(info, op):
    if op == 'gastos':
        datos_base_de_datos = info
        fecha = datetime.now()

        # Crea un DataFrame de Pandas
        df = pd.DataFrame(datos_base_de_datos)

        # Guarda el DataFrame en un archivo Excel
        nombre_archivo = f'Consulta_RG_GI_{str(fecha.day)}_{str(fecha.month)}_{str(fecha.year)}.xlsx'
        df.to_excel(nombre_archivo, index=False)
    
