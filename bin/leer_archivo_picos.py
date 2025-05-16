def leer_archivo_picos(peaks_path):
    """
    Lee un archivo de picos y devuelve una lista de diccionarios con informacion.

    Este metodo permite procesar un archivo de picos en formato TSV, donde cada linea
    contiene datos de los picos asociados a factores de transcripcion (TF). 
    Omite el encabezado y convierte las columnas relevantes en una estructura
    de diccionario para cada pico.

    Args:
        peaks_path (str): Ruta al archivo de picos en formato TSV.

    Returns:
        list[dict]: Una lista de diccionarios, cada uno con las claves:
            - "TF_name" (str): Nombre del factor de transcripcion.
            - "start" (int): Posicion inicial del pico.
            - "end" (int): Posicion final del pico.
    """
    peaks_data = []  # Lista vacia para almacenar los picos
    with open(peaks_path, "r") as archivo:
        for linea in archivo:
            # En caso de que sea el encabezado, nos saltamos esa linea
            if "TF_name" in linea:
                continue
            # Dividir lineas por tabulaciones
            partes = linea.strip().split("\t") 

            # Tomamos las columnas correctas
            tf_name = partes[2]
            start = int(float(partes[3]))
            end = int(float(partes[4]))
            
            pico = {  # Creamos un diccionario con los datos del pico
                "TF_name": tf_name,
                "start": start,
                "end": end
            }
            peaks_data.append(pico)
    return peaks_data