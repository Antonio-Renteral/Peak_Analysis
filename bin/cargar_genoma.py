def cargar_genoma(fasta_path):
    """
    Carga el genoma desde un archivo en formato FASTA.

    Este método procesa un archivo para cargar el contenido del genoma,
    omitiendo las líneas de encabezado que comienzan con el carácter '>'.
    Devuelve el genoma como una única cadena de texto.

    Args:
        fasta_path (str): Ruta al archivo FASTA que contiene el genoma.

    Returns:
        str: El genoma completo como una sola cadena de texto, 
        sin encabezados ni saltos de línea.
    """
    genoma = ""  # Inicializa el genoma como cadena vacía
    with open(fasta_path, "r") as archivo:
        for linea in archivo:
            if linea.startswith(">"):  # Omite encabezados
                continue
            genoma += linea.strip()  # Elimina saltos de línea y agrega el contenido
    return genoma