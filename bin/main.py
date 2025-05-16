"""
Modulo principal (main) que sirve para procesar datos genomicos

Este script ejecuta las funciones principales para cargar un genoma,
leer datos de picos, extraer secuencias correspondientes a factores 
de transcripcion y guardar los resultados en un archivo de formato FASTA

Archivos utilizados por el codigo:
- `cargar_genoma`: Para cargar el archivo de datos genomicos
- `leer_archivo_picos`: Para procesar el archivo de picos de entrada
- `extraer_secuencias`: Para extraer las secuencias basadas en los datos de picos
- `guardar_fasta_por_tf`: Para guardar las secuencias en formato FASTA pero
  tomando en cuenta los TF

Rutas iniciales:
- `fasta_path`: Es la ruta al archivo donde tenemos nuestras secuencias
- `peaks_path`: Es la ruta al archivo de picos en formato TSV
- `output_dir`: Ruta al directorio de salida, donde guardaremos
  los resultados obtenidos con el programa

Autor: Addiel Antonio Platas Renteral
"""


import os
from cargar_genoma import cargar_genoma
from leer_archivo_picos import leer_archivo_picos
from extraer_secuencias import extraer_secuencias
from guardar_fasta_por_tf import guardar_fasta_por_tf

# Declaracion de rutas
fasta_path = os.path.join("..", "data", "datos.txt")
peaks_path = os.path.join("..", "data", "union_peaks_file.tsv")
output_dir = os.path.join("..", "results")

# Ejecucion de las funciones principales
genoma = cargar_genoma(fasta_path)
peaks_data = leer_archivo_picos(peaks_path)
secuencias_por_tf = extraer_secuencias(peaks_data, genoma)
guardar_fasta_por_tf(secuencias_por_tf, output_dir)

# Mensaje con el numero de archivos creados
print(
    f"¡Se guardaron {len(secuencias_por_tf)} archivos FASTA "
    f"en {output_dir}!"
)