import pandas as pd

def leer_archivo_picos(peaks_path):
    """
    Lee un archivo de picos en formato TSV y devuelve una lista de diccionarios con información.

    Utiliza Pandas para procesar el archivo de picos, donde cada fila contiene datos
    asociados a factores de transcripción (TF). Convierte las columnas relevantes en 
    una estructura de diccionario para cada pico.

    Args:
        peaks_path (str): Ruta al archivo de picos en formato TSV.

    Returns:
        list[dict]: Una lista de diccionarios, cada uno con las claves:
            - "TF_name" (str): Nombre del factor de transcripción.
            - "start" (int): Posición inicial del pico.
            - "end" (int): Posición final del pico.
    """
    try:
        # Leer el archivo TSV usando Pandas
        df = pd.read_csv(peaks_path, sep="\t")

        # Seleccionar las columnas relevantes y convertir a lista de diccionarios
        peaks_data = df[["TF_name", "start", "end"]].to_dict(orient="records")
        return peaks_data

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {peaks_path}.")
        raise 

    except Exception as e: 
        print(f"Error al procesar el archivo de picos: {e}")
        raise