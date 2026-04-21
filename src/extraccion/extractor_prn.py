import pandas as pd
from pathlib import Path

# Rutas
BASE_DIR   = Path(__file__).resolve().parent.parent.parent
FILES_DIR  = BASE_DIR / "files"
OUTPUT_DIR = BASE_DIR / "outputs"

def leer_prn(ruta):
    filas = []
    with open(ruta, 'r', encoding='latin-1') as f:
        for linea in f:
            linea = linea.rstrip('\n')
            if len(linea) < 10:
                continue

            tipo_doc = linea[0:2]        # TI o CC
            num_doc  = linea[2:17]       # Número de documento
            materia  = linea[17:-3]      # Código materia
            nota     = int(linea[-3:])   # Nota

            filas.append({
                'tipo_documento'  : tipo_doc,
                'numero_documento': num_doc,
                'materia'         : materia,
                'nota'            : nota
            })

    return pd.DataFrame(filas)

# ⚠️ Verifica primero el nombre exacto del archivo
print("Archivos disponibles en files/:")
for archivo in FILES_DIR.iterdir():
    print(f"  → {archivo.name}")

# Luego cambia el nombre por el que aparezca arriba
df = leer_prn(FILES_DIR / "Asistencia.prn")

print(df.head(10))
print(f"\nTotal registros: {len(df)}")