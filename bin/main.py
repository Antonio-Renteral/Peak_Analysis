"""
Modulo principal (main) que sirve para procesar datos genomicos.

Este script ejecuta las funciones principales para cargar un genoma,
leer datos de picos, extraer secuencias correspondientes a factores 
de transcripcion y guardar los resultados en un archivo de formato FASTA.

Las rutas de entrada y salida pueden especificarse mediante argumentos
de línea de comandos al ejecutar el script:

Argumentos disponibles:
- `--fasta_path`: Ruta al archivo FASTA del genoma 
- `--peaks_path`: Ruta al archivo de picos en formato TSV 
- `--output_dir`: Directorio donde se guardarán los archivos de salida 
  (por defecto: ../results).

Archivos utilizados por el codigo:
- `cargar_genoma`: Para cargar el archivo de datos genomicos.
- `leer_archivo_picos`: Para procesar el archivo de picos de entrada.
- `extraer_secuencias`: Para extraer las secuencias basadas en los datos de picos.
- `guardar_fasta_por_tf`: Para guardar las secuencias en formato FASTA 
  pero tomando en cuenta los TF.

Autor: Addiel Antonio Platas Renteral.
"""

import os
from cargar_genoma import cargar_genoma
from leer_archivo_picos import leer_archivo_picos
from extraer_secuencias import extraer_secuencias
from guardar_fasta_por_tf import guardar_fasta_por_tf
from argumentos import parse_args


if __name__ == "__main__":
    # Parseo de los argumentos desde la línea de comandos
    args = parse_args()

    # Asignación de las rutas desde los argumentos
    fasta_path = args.fasta_path
    peaks_path = args.peaks_path
    output_dir = args.output_dir

    # Verificar que el archivo del genoma existe
    if not os.path.exists(fasta_path):
        raise FileNotFoundError(f"Error: El archivo FASTA del genoma no existe en la ruta: {fasta_path}")
    
    # Verificar que el archivo de picos existe
    if not os.path.exists(peaks_path):
        raise FileNotFoundError(f"Error: El archivo de picos no existe en la ruta: {peaks_path}")

    # Ejecución de las funciones principales del script
    genoma = cargar_genoma(fasta_path)
    peaks_data = leer_archivo_picos(peaks_path)
    secuencias_por_tf = extraer_secuencias(peaks_data, genoma)
    guardar_fasta_por_tf(secuencias_por_tf, output_dir)

    # Mensaje final con el número de archivos generados
    print(
        f"¡Se guardaron {len(secuencias_por_tf)} archivos FASTA "
        f"en {output_dir}!"
    )