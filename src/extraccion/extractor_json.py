import os #operative systems

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #Quiero la carpeta raiz de mi proyecto asi que buscala
FILES_DIR = os.path.join(BASE_DIR, "files")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

import pandas as pd

def leer_json(ruta):  #Funcion
    try:
        df = pd.read_json(ruta)
        return df
    except Exception as e:
        raise Exception(f"Error al leer el CSV: {e}") #Toma el error y haz que lo maneja otro (raise(escalalo))

estudiantes = leer_json(os.path.join(FILES_DIR, "EspaciosAcademicos.json")) #Llamo a la funcion y ve a files, extrae EspaciosAcaedmicos y guardalo en estudiantes
print (estudiantes)