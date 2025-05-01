def cargar_genoma(fasta_path):
    """Nos permite cargar el genoma a partir de un FASTA y devuelve una unica cadena de texto"""
    genoma = ""  # Inicializamos el genoma como una cadena vacia
    with open(fasta_path, "r") as archivo:
        for linea in archivo:  # Es un ciclo que nos permite leer linea por linea nuestro archivo
            if linea.startswith(">"):  # Pregunta si la linea empieza con ">", ya que esos son los encabezados
                continue  # Dado que es un encabezado lo que queremos hacer es evitarlo y no agregarlo a nuestra cadena
            genoma += linea.strip()  # Con el strip quitamos saltos de linea y luego agregamos ese renglon al genoma
    return genoma

def leer_archivo_picos(peaks_path):
    """Lee el archivo de picos y devuelve una lista de diccionarios con TF_name, start y end."""
    peaks_data = []  # Inicializamos una lista vacia para almacenar los picos
    with open(peaks_path, "r") as archivo:
        for linea in archivo:
            # En caso de que sea el encabezado, nos saltamos esa linea
            if "TF_name" in linea:
                continue
            # Podemos dividir las lineas por tabulaciones y al mimso tiempo quitamos saltos de linea y espacios
            partes = linea.strip().split("\t") 

            # Tomamos las columnas correctas
            tf_name = partes[2]  # TF_name esta en la columna 1 (indice 1)
            start = int(float(partes[3]))  # Peak_start esta en la columna 2 (indice 2), lo convertimos a entero
            end = int(float(partes[4]))    # Peak_end esta en la columna 3 (indice 3), lo convertimos a entero
            
            pico = {  # Creamos un diccionario con los datos del pico
                "TF_name": tf_name,
                "start": start,
                "end": end
            }
            peaks_data.append(pico)
    return peaks_data

def extraer_secuencias(peaks_data, genoma):
    """Agrupa las secuencias extraídas por TF_name en un diccionario."""
    secuencias_por_tf = {}  # Crea un diccionario vacio
    for pico in peaks_data:  # Iteramos directamente sobre los elementos de la lista
        tf_name = pico["TF_name"]
        start = pico["start"]
        end = pico["end"]
        secuencia = genoma[start:end]  # Extraer la secuencia
        if tf_name not in secuencias_por_tf:  # Si no existe la clave en el diccionario
            secuencias_por_tf[tf_name] = []  # Crear una lista vacia para ese TF_name
        secuencias_por_tf[tf_name].append(secuencia) # Agregamos la secuencia extraida a la lista asociada al TF_name
    return secuencias_por_tf

def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """Guarda archivos FASTA separados por cada TF_name."""
    import os
    if not os.path.exists(output_dir):  # Verificar si la carpeta no existe
        os.mkdir(output_dir)  # Crear la carpeta

    tf_names = list(secuencias_por_tf.keys())  # Obtener todas las claves (TF_names)
    for i in range(len(tf_names)):  # Recorrer cada TF_name
        tf_name = tf_names[i]
        secuencias = secuencias_por_tf[tf_name]
        with open(f"{output_dir}/{tf_name}.fasta", "w") as archivo: # Crear un archivo para cada TF_name
            for j in range(len(secuencias)):  # Recorrer las secuencias
                archivo.write(f">secuencia_{j + 1}\n")  # Escribir encabezado
                archivo.write(f"{secuencias[j]}\n")  # Escribir la secuencia

"""Esta es la parte principal del codigo que se encarga de ejecutar como tal el script"""

fasta_path = "C:\\Users\\addie\\Documents\\Peak_Analysis\\data\\E_coli_K12_MG1655_U00096.3.txt"  # Ruta al archivo FASTA
peaks_path = "C:\\Users\\addie\\Documents\\Peak_Analysis\\data\\union_peaks_file.tsv"  # Ruta al archivo TSV de picos
output_dir = "C:\\Users\\addie\\Documents\\Peak_Analysis\\results"  # Carpeta de salida

# Ejecucion de las funciones principales
genoma = cargar_genoma(fasta_path)
peaks_data = leer_archivo_picos(peaks_path)
secuencias_por_tf = extraer_secuencias(peaks_data, genoma)
guardar_fasta_por_tf(secuencias_por_tf, output_dir)

# Un mensaje en la pantalla meramente estetico y para saber que ya esta listo nuestro
print(f"¡Se guardaron {len(secuencias_por_tf)} archivos FASTA en {output_dir}!")