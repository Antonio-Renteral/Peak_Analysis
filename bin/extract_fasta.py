def cargar_genoma(fasta_path):
    """Permite cargar el genoma a partir de un FASTA, devuelve una cadena de texto"""
    genoma = ""  # Inicializamos el genoma como cadena vacia
    with open(fasta_path, "r") as archivo:
        for linea in archivo:  # Leer linea por linea nuestro archivo
            if linea.startswith(">"):  # Evita los encabezados (">")
                continue 
            genoma += linea.strip()  # Con strip quitamos saltos de linea y agregamos la linea
    return genoma


def leer_archivo_picos(peaks_path):
    """Lee el archivo de picos y devuelve una lista de diccionarios con TF_name, start y end."""
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
        secuencias_por_tf[tf_name].append(secuencia) # Agrega secuencia extraida a la lista asociada al TF_name
    return secuencias_por_tf


def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """Guarda archivos FASTA separados por cada TF_name."""
    import os
    if not os.path.exists(output_dir):  # Verificar existencia
        os.mkdir(output_dir)  # Crear la carpeta

    tf_names = list(secuencias_por_tf.keys())  # Obtener todas las claves (TF_names)
    for i in range(len(tf_names)):  # Recorrer cada TF_name
        tf_name = tf_names[i]
        secuencias = secuencias_por_tf[tf_name]
        with open(
            f"{output_dir}/{tf_name}.fasta", "w"
        ) as archivo:  # Crear un archivo para cada TF_name
            for j in range(len(secuencias)):  # Recorrer las secuencias
                archivo.write(f">secuencia_{j + 1}\n")  # Escribir encabezado
                archivo.write(f"{secuencias[j]}\n")  # Escribir la secuencia


"""Esta es la parte principal del codigo que se encarga de ejecutar como tal el script"""

# Solicitar rutas al usuario
print("Introduce las rutas de los archivos y directorio:")
fasta_path = input("Ruta del archivo FASTA: ").strip()
peaks_path = input("Ruta del archivo TSV de picos: ").strip()
output_dir = input("Ruta del directorio de salida: ").strip()

# Ejecucion de las funciones principales
genoma = cargar_genoma(fasta_path)
peaks_data = leer_archivo_picos(peaks_path)
secuencias_por_tf = extraer_secuencias(peaks_data, genoma)
guardar_fasta_por_tf(secuencias_por_tf, output_dir)

# Mensaje con el numero de archivos creados
print(
    f"¡Se guardaron {len(secuencias_por_tf)} archivos FASTA en {output_dir}!"
)