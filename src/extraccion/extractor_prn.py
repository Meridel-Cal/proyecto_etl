import pandas as pd
from pathlib import Path #De la libreria estandar extrae el Path para trabajar rutas mas modernas que os

# Rutas
BASE_DIR   = Path(__file__).resolve().parent.parent.parent
FILES_DIR  = BASE_DIR / "files"
OUTPUT_DIR = BASE_DIR / "outputs"

def leer_prn(ruta):
    filas = [] #Crealo como un arreglo vacio
    with open(ruta, 'r', encoding='utf-8') as f: #
        for linea in f:
            linea = linea.rstrip('\n') #Busca el salto de linea
            if len(linea) < 10:
                continue #Como un break

            tipo_doc = linea[0:2]        # TI o CC
            num_doc  = linea[2:17]       # Número de documento
            materia  = linea[17:-3]      # Código materia empieza de atras hacia adelante
            nota     = int(linea[-3:])   # Nota

            filas.append({
                'tipo_documento'  : tipo_doc,
                'numero_documento': num_doc,
                'materia'         : materia,
                'nota'            : nota
            })

    return pd.DataFrame(filas)

# ⚠️ Verifica primero el nombre exacto del archivo
'''
print("Archivos disponibles en files/:")
for archivo in FILES_DIR.iterdir():
    print(f"  → {archivo.name}")'''

# Luego cambia el nombre por el que aparezca arriba
df = leer_prn(FILES_DIR / "Asistencia.prn")

print(df.head(10))
print(f"\nTotal registros: {len(df)}")