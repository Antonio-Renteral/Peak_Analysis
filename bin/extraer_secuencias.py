def extraer_secuencias(peaks_data, genoma):
    """
    Agrupa las secuencias extraídas por TF_name en un diccionario.

    Args:
        peaks_data (list[dict]): Lista de diccionarios con información 
            de los picos, cada uno con las claves "TF_name", "start" y "end".
        genoma (str): Cadena de texto que representa el genoma completo.

    Returns:
        dict: Un diccionario donde las claves son los nombres de los 
            factores de transcripción (TF_name) y los valores son listas 
            con las secuencias extraídas correspondientes.
    """
    secuencias_por_tf = {}  # Diccionario para almacenar las secuencias
    for pico in peaks_data:
        tf_name = pico["TF_name"]
        start = pico["start"]
        end = pico["end"]
        secuencia = genoma[start:end]  # Extrae la secuencia del genoma
        if tf_name not in secuencias_por_tf:
            secuencias_por_tf[tf_name] = []  # Crea una lista para el TF_name
        secuencias_por_tf[tf_name].append(secuencia)  # Añade la secuencia extraída
    return secuencias_por_tf