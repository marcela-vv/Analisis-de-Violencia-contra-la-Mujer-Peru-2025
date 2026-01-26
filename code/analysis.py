import pandas as pd
import os

# Función para procesar la información y generar los resultados
def procesar_data():
    # Definimos la ubicación del archivo unificado que tenemos en la carpeta data
    ruta_archivo = "data/DATASET_UNIFICADO_2025.csv"
    
    if os.path.exists(ruta_archivo):
        # Paso 1: Carga de datos y limpieza de los nombres de las columnas
        df = pd.read_csv(ruta_archivo)
        df.columns = df.columns.str.strip().str.upper()
        
        # Paso 2: Limpieza de la columna cantidad para que sea numérica
        df['CANTIDAD'] = pd.to_numeric(df['CANTIDAD'], errors='coerce').fillna(0)
        
        # Paso 3: Análisis por departamentos para ver el crecimiento de denuncias
        # Agrupamos por departamento y año para calcular cuánto variaron las cifras
        resumen_dptos = df.groupby(['DPTO_HECHO', 'AÑO'])['CANTIDAD'].sum().reset_index()
        resumen_dptos = resumen_dptos.sort_values(['DPTO_HECHO', 'AÑO'])
        resumen_dptos['VARIACION_%'] = resumen_dptos.groupby('DPTO_HECHO')['CANTIDAD'].pct_change() * 100
        
        # Guardamos el ranking de departamentos de 2025 ordenado por crecimiento
        ranking_dptos = resumen_dptos[resumen_dptos['AÑO'] == 2025].sort_values('VARIACION_%', ascending=False)
        ranking_dptos.to_csv("data/ranking_departamentos_2025.csv", index=False)

        # Paso 4: Análisis por provincias para tener un detalle más específico
        # Agrupamos por provincia para identificar los focos críticos este año
        ranking_prov = df[df['AÑO'] == 2025].groupby('PROV_HECHO')['CANTIDAD'].sum().sort_values(ascending=False).reset_index()
        ranking_prov.to_csv("data/ranking_provincias_2025.csv", index=False)

        # Paso 5: Análisis por meses para identificar patrones en el tiempo
        # Sumamos las denuncias de 2025 por cada mes disponible
        if 'MES' in df.columns:
            resumen_mensual = df[df['AÑO'] == 2025].groupby('MES')['CANTIDAD'].sum().reset_index()
            resumen_mensual.to_csv("data/analisis_mensual_2025.csv", index=False)

        print("El procesamiento ha terminado y los archivos están en la carpeta data")
    else:
        print("No se encontró el archivo unificado en la carpeta data")

# Ejecución del proceso
if __name__ == "__main__":
    procesar_data()