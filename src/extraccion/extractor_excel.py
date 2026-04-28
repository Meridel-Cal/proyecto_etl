import os #operative systems

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #Quiero la carpeta raiz de mi proyecto asi que buscala
FILES_DIR = os.path.join(BASE_DIR, "files")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

import pandas as pd
#Hay otra libreria de python que se trae directamente en el terminal (openpyxl) para que se pueda abrir documentos actuales 

def leer_excel(ruta):  #Funcion
    try:
        df = pd.read_excel(ruta)
        return df
    except Exception as e:
        raise Exception(f"Error al leer el CSV: {e}") #Toma el error y haz que lo maneja otro (raise(escalalo))

estudiantes = leer_excel(os.path.join(FILES_DIR, "estudiantes.xlsx")) #Llamo a la funcion y ve a files, extrae estudiantes y guardalo en estudiantes
print (estudiantes)