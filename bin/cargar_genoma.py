def cargar_genoma(fasta_path):
    """
    Permite cargar el genoma a partir de un archivo en formato FASTA

    Este metodo procesa un archivo para cargar el contenido del genoma,
    omitiendo las lineas de encabezado que comienzan con el caracter '>'.
    Devuelve el genoma como una unica cadena de texto.

    Args:
        fasta_path (str): Ruta al archivo FASTA que contiene el genoma.

    Returns:
        str: El genoma completo representado como una sola cadena de texto,
        sin encabezados ni saltos de línea.
    """
    genoma = ""  # Inicializamos el genoma como cadena vacia
    with open(fasta_path, "r") as archivo:
        for linea in archivo:  # Leer linea por linea nuestro archivo
            if linea.startswith(">"):  # Evita los encabezados (">")
                continue 
            genoma += linea.strip()  # Con strip quitamos saltos de linea y agregamos la linea
    return genoma