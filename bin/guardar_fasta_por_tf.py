def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """
    Se encarga de guardar archivos FASTA separados por cada TF_name.

    Esta funcion crea un archivo FASTA para cada TF_name en el diccionario
    proporcionado, almacenando las secuencias asociadas en el directorio
    especificado.

    Args:
        secuencias_por_tf (dict): Diccionario donde las claves son nombres
            de factores de transcripcion (TF_name) y los valores son listas
            de secuencias asociadas.
        output_dir (str): Ruta al directorio donde se guardaran los archivos.
    """
    import os

    if not os.path.exists(output_dir):  # Verificar existencia
        os.mkdir(output_dir)  # Crear la carpeta si no existe

    tf_names = list(secuencias_por_tf.keys())  # Obtener todas las claves (TF_names)

    for i, tf_name in enumerate(tf_names):  # Recorrer cada TF_name
        secuencias = secuencias_por_tf[tf_name]
        file_path = os.path.join(output_dir, f"{tf_name}.fasta")
        with open(file_path, "w") as archivo:  # Crear un archivo para cada TF_name
            for j, secuencia in enumerate(secuencias):  # Recorrer las secuencias
                archivo.write(f">secuencia_{j + 1}\n")  # Escribir encabezado
                archivo.write(f"{secuencia}\n")  # Escribir la secuencia