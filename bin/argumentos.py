import os
import argparse

def parse_args():
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