def extraer_secuencias(peaks_data, genoma):
    """
    Permite agrupar las secuencias extraidas por TF_name en un diccionario.

    Args:
        peaks_data (list[dict]): Lista de diccionarios con informacion 
            de los picos, cada uno con las claves "TF_name", "start" y "end".
        genoma (str): Cadena de texto que representa el genoma completo.

    Returns:
        dict: Un diccionario donde las claves son los nombres de los 
        factores de transcripcion (TF_name) y los valores son listas 
        con las secuencias extraidas correspondientes.
    """
    secuencias_por_tf = {}  # Crea un diccionario vacio
    for pico in peaks_data:  # Itera directamente sobre los elementos de la lista
        tf_name = pico["TF_name"]
        start = pico["start"]
        end = pico["end"]
        secuencia = genoma[start:end]  # Extrae la secuencia
        if tf_name not in secuencias_por_tf:  # Si no existe la clave en el diccionario
            secuencias_por_tf[tf_name] = []  # Crea una lista vacia para ese TF_name
        secuencias_por_tf[tf_name].append(secuencia)  # Agrega la secuencia extraida
    return secuencias_por_tf