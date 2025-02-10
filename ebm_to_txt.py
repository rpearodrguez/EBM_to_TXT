# Script en python que convierte un archivo de formato EBM a un archivo de texto plano
# Autor: Richard Peña Rodríguez
# Fecha: 2025-02-08

import sys
import os

# Funcion que extrae los strings de un archivo de extensión .ebm
def extract_strings(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            with open(file_name.replace('.ebm', '.txt'), 'w') as new_file:
                for line in lines:
                    new_line = ''
                    char_counter = 0
                    char_stock = ''
                    for char in line:
                        if char.isalpha() or char.isdigit() or char in [' ', '.', ',', '!', '?', '\'', '\"',':', ';', '(', ')', '-', '_']:
                            if char == 'ÿ':
                                continue
                            char_counter += 1
                            char_stock += char
                        elif char == '\n':
                            new_line += '\n'
                        elif char == '\t':
                            new_line += '\t'
                        else:
                            if char_counter >= 2:
                                new_line += char_stock
                                char_counter = 0
                                char_stock = ''
                            else:
                                char_counter = 0
                                char_stock = ''
                    new_file.write(new_line)
    except FileNotFoundError:
        print(f'Error: El archivo {file_name} no fue encontrado')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    # El script debe revisar todos los archivos con extensión .ebm en el directorio actual
    for file_name in os.listdir():
        if file_name.endswith('.ebm'):
            extract_strings(file_name)
    print('Proceso terminado')
    sys.exit(0)