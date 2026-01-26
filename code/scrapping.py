import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# --- PASO 1: PREPARAMOS NUESTRAS CARPETAS DE TRABAJO ---
# Creamos la carpeta 'data' si no existe para organizar nuestros archivos descargados
folder_data = "data"
if not os.path.exists(folder_data):
    os.makedirs(folder_data)

# --- PASO 2: DEFINIMOS EL SCRAPING PARA BUSCAR LOS DATOS ---
# Creamos una función para que Python entre a la web del Mininter y busque los links de 2025
def extraer_enlaces_mininter(url_web):
    headers = {"User-Agent": "Mozilla/5.0"}
    print(f"Conectando a la fuente: {url_web}...")
    
    # Usamos BeautifulSoup para leer el HTML y encontrar las etiquetas de descarga
    response = requests.get(url_web, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    enlaces_validos = []
    
    # Recorremos todos los enlaces y filtramos solo los que dicen 'violencia' y '2025'
    for link in soup.find_all("a", href=True):
        texto_link = link.get_text().lower()
        if "violencia" in texto_link and "2025" in texto_link:
            enlaces_validos.append(link['href'])
    
    return enlaces_validos

# --- PASO 3: DESCARGAMOS Y UNIFICAMOS TODA LA INFORMACIÓN ---
# Esta función baja los archivos uno por uno y los une en una sola tabla de Pandas
def procesar_archivos(lista_urls):
    todos_los_datos = []
    
    for url in lista_urls:
        nombre_archivo = url.split("/")[-1]
        ruta_guardado = os.path.join(folder_data, nombre_archivo)
        
        # Realizamos la descarga programática de cada mes detectado
        print(f"Descargando archivo mensual: {nombre_archivo}")
        archivo_binario = requests.get(url).content
        with open(ruta_guardado, "wb") as f:
            f.write(archivo_binario)
        
        # Leemos el archivo (sea CSV o Excel) y lo agregamos a nuestra lista
        if ruta_guardado.endswith(".csv"):
            df_mes = pd.read_csv(ruta_guardado)
        else:
            df_mes = pd.read_excel(ruta_guardado)
            
        # Limpiamos los nombres de las columnas para que todas coincidan al unir
        df_mes.columns = df_mes.columns.str.strip().str.upper()
        todos_los_datos.append(df_mes)
        time.sleep(1) # Pausa de seguridad para no saturar el servidor del Mininter
        
    # Unimos todos los meses en un solo dataset unificado
    if todos_los_datos:
        return pd.concat(todos_los_datos, ignore_index=True)
    return None

# --- PASO 4: EJECUCIÓN FINAL DE NUESTRO PROYECTO ---
if __name__ == "__main__":
    url_fuente = "https://observatorio.mininter.gob.pe/proyectos/base-de-datos-hechos-delictivos-basados-en-denuncias-en-el-sidpol"
    
    # Iniciamos el proceso de extracción (Scraping)
    links_encontrados = extraer_enlaces_mininter(url_fuente)
    print(f"Hemos encontrado {len(links_encontrados)} archivos mensuales para procesar.")
    
    # Iniciamos la descarga y la unión de los datos
    if links_encontrados:
        dataset_final = procesar_archivos(links_encontrados)
        
        # Guardamos nuestro resultado final en la carpeta data
        if dataset_final is not None:
            ruta_final = os.path.join(folder_data, "DATASET_UNIFICADO_2025.csv")
            dataset_final.to_csv(ruta_final, index=False)
            print(f"✅ ¡Trabajo terminado! Hemos unificado {len(dataset_final)} registros en {ruta_final}")