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

    # Crea un analizador de argumentos con una descripción breve de su propósito
    parser = argparse.ArgumentParser(description="Procesa datos genómicos para extraer y guardar secuencias.")
    
    # Agrega el argumento para la ruta del archivo FASTA del genoma
    parser.add_argument(
        "-f", # Podrías agregar un atajo para este argumento, por ejemplo, "-f" para facilitar su uso
        "--fasta_path",  # Nombre del argumento
        type=str,  # Tipo de dato esperado (cadena de texto)
        default=os.path.join("..", "data", "E_coli_K12_MG1655_U00096.3.txt"),  # Valor predeterminado
        help="Ruta al archivo FASTA del genoma."  # Descripción del argumento
    )
    
    # Agrega el argumento para la ruta del archivo de picos en formato TSV
    parser.add_argument(
        "-p", # Otra opción para facilitar el uso, por ejemplo, "-p" para picos
        "--peaks_path",  # Nombre del argumento
        type=str,  # Tipo de dato esperado
        default=os.path.join("..", "data", "union_peaks_file.tsv"),  # Valor predeterminado
        help="Ruta al archivo de picos en formato TSV."  # Descripción del argumento
    )
    
    # Agrega el argumento para el directorio de salida donde se guardarán los resultados
    parser.add_argument(
        "-o",  # Podrías agregar un atajo para este argumento también, por ejemplo, "-o" para output
        "--output_dir",  # Nombre del argumento
        type=str,  # Tipo de dato esperado
        default=os.path.join("..", "results"),  # Valor predeterminado
        help="Directorio de salida para guardar los resultados."  # Descripción del argumento
    )
    
    # Retorna los argumentos analizados en un objeto Namespace
    return parser.parse_args()