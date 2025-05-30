import os
import argparse

def parse_args():
    """
    Define y analiza los argumentos de línea de comandos para el procesamiento de datos genómicos.

    Esta función utiliza argparse para configurar y leer los argumentos necesarios para
    ejecutar el programa principal. Los argumentos incluyen las rutas a los archivos de
    entrada y el directorio de salida, con valores predeterminados para simplificar la ejecución.

    Argumentos definidos:
    - `--fasta_path` (str): Ruta al archivo FASTA que contiene las secuencias genómicas. 
      Valor predeterminado: "../data/E_coli_K12_MG1655_U00096.3.txt".
    - `--peaks_path` (str): Ruta al archivo de picos en formato TSV. 
      Valor predeterminado: "../data/union_peaks_file.tsv".
    - `--output_dir` (str): Directorio donde se guardarán los resultados generados. 
      Valor predeterminado: "../results".

    Retorna:
        argparse.Namespace: Un objeto que contiene los valores de los argumentos proporcionados.
    """

    
    parser = argparse.ArgumentParser(description="Procesa datos genómicos para extraer y guardar secuencias.")
    parser.add_argument(
        "--fasta_path",
        type=str,
        default=os.path.join("..", "data", "E_coli_K12_MG1655_U00096.3.txt"),
        help="Ruta al archivo FASTA del genoma."
    )
    parser.add_argument(
        "--peaks_path",
        type=str,
        default=os.path.join("..", "data", "union_peaks_file.tsv"),
        help="Ruta al archivo de picos en formato TSV."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=os.path.join("..", "results"),
        help="Directorio de salida para guardar los resultados."
    )
    return parser.parse_args()