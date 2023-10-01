import os
import chardet

# Obtiene la ruta actual
ruta_actual = os.getcwd()

# Función para buscar archivos 'index.md' y mostrar su codificación
def buscar_index_md(ruta):
    for root, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo == "index.md":
                ruta_completa = os.path.join(root, archivo)
                with open(ruta_completa, 'rb') as f:
                    resultado = chardet.detect(f.read())
                    print(f"Archivo: {ruta_completa}, Codificación: {resultado['encoding']}")

buscar_index_md(ruta_actual)
