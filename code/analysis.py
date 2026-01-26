import pandas as pd
import os

def procesar_datos():
    ruta_datos = "data/DATASET_UNIFICADO_2025.csv"
    
    if not os.path.exists(ruta_datos):
        print("No se encontró el dataset unificado.")
        return

    df = pd.read_csv(ruta_datos)
    
    # --- 1. LIMPIEZA TÉCNICA (Punto 4 de las pautas) ---
    df['CANTIDAD'] = pd.to_numeric(df['CANTIDAD'], errors='coerce').fillna(0)
    # Limpiamos espacios en los nombres de las columnas
    df.columns = df.columns.str.strip()

    # --- 2. ANÁLISIS GEOGRÁFICO (El que ya tenías) ---
    resumen_dpto = df.groupby(['DPTO_HECHO', 'AÑO'])['CANTIDAD'].sum().reset_index()
    resumen_dpto = resumen_dpto.sort_values(['DPTO_HECHO', 'AÑO'])
    resumen_dpto['VARIACION_%'] = resumen_dpto.groupby('DPTO_HECHO')['CANTIDAD'].pct_change() * 100
    
    ranking_dpto = resumen_dpto[resumen_dpto['AÑO'] == 2025].sort_values('VARIACION_%', ascending=False)
    ranking_dpto.to_csv("data/ranking_departamentos_2025.csv", index=False)

    # --- 3. NUEVO: ANÁLISIS POR MODALIDAD (Punto 4.2 de las pautas) ---
    # Esto responde a: ¿Qué tipo de violencia es la más común?
    if 'MODALIDAD' in df.columns:
        ranking_modalidad = df[df['AÑO'] == 2025].groupby('MODALIDAD')['CANTIDAD'].sum().sort_values(ascending=False).reset_index()
        ranking_modalidad.to_csv("data/ranking_modalidad_2025.csv", index=False)
        print("\n🔥 Top Modalidades de Violencia en 2025:")
        print(ranking_modalidad.head(3))

    # --- 4. NUEVO: ANÁLISIS MENSUAL (Punto 4.3 de las pautas) ---
    # Esto responde a: ¿En qué meses hay más denuncias?
    if 'MES' in df.columns:
        ranking_mes = df[df['AÑO'] == 2025].groupby('MES')['CANTIDAD'].sum().reset_index()
        ranking_mes.to_csv("data/analisis_mensual_2025.csv", index=False)

    print("Procesamiento completado")
    print("Se han generado 3 archivos en la carpeta /data para tu informe.")

# Ejecutamos la función
if __name__ == "__main__":
    procesar_datos()