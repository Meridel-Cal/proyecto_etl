import os #operative systems

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #Quiero la carpeta raiz de mi proyecto asi que buscala
FILES_DIR = os.path.join(BASE_DIR, "files") #Genera ruta internas de cada carpeta
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs") # ""
LOGS_DIR = os.path.join(BASE_DIR, "logs") # ""

import pandas as pd

def leer_csv(ruta):  #Funcion
    try:
        df = pd.read_csv(ruta)
        return df
    except Exception as e:
        raise Exception(f"Error al leer el CSV: {e}") #Toma el error y haz que lo maneja otro (raise(escalalo))

estudiantes = leer_csv(os.path.join(FILES_DIR, "Matriculas.csv")) #Llamo a la funcion y ve a files, extrae Matriculas y guardalo en estudiantes
print (estudiantes)