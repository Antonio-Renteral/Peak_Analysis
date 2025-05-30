### Casos de Prueba para el Módulo 1: Extractor y Creador de Secuencias FASTA

1.  **Caso: Generación exitosa de archivos FASTA.**

   - **Entradas:**
       - Archivo de picos válido.
       - Archivo FASTA del genoma válido.
       - Directorio de salida.
   - **Esperado:**
       - Archivos FASTA generados correctamente en el directorio de salida.

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```

```bash
ls fasta_peaks/
```

2.  **Caso: Archivo del genoma no se encuentra.**
    
    -   **Entradas:**
        -   Ruta incorrecta o inexistente para el archivo FASTA del genoma.

    -   **Esperado:** `"Error: Genome file not found"`
    
    ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
    ```
    ```
    Error: "Ecoli.fna" genome file not found
    ```

3.  **Caso: Archivo de picos no se encuentra.**
    
    -   **Entradas:**
        -   Ruta incorrecta o inexistente para el archivo de picos.

    -   **Esperado:** `"Error: Peaks file not found"`
    
    ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
    ```
    ```
    Error: "Ecoli.fna" genome file not found
    ```
    
4.  **Caso: Directorio de salida no existe.**

   - **Entradas:**
      - Archivo de picos válido.
      - Archivo FASTA del genoma válido.
      - Ruta de directorio de salida inexistente.
   - **Esperado:**
      - El sistema debe crear el directorio de salida automáticamente y generar los archivos FASTA.

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o nonexistent_dir/
```

```bash
ls nonexistent_dir/
```