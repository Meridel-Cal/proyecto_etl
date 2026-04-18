import os #operative systems

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #Crea la ruta el mismo sistema de mi proyecto
FILES_DIR = os.path.join(BASE_DIR, "files")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

import pandas as pd

def leer_fwf(ruta):  #Funcion para leer un archi
    try:
        df = pd.read_fwf(ruta)
        return df
    except Exception as e:
        raise

estudiantes = leer_fwf(os.path.join(FILES_DIR, "Asistencias (1).prn"))
print (estudiantes)