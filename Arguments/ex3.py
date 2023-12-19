# Fes un programa que genera una llista formada per tots els paràmetres que li passem com argument i la mostra per consola.

import sys

def generar_i_mostrar_llista():
    created_list = sys.argv[1:]
    print(created_list)

def main():
    generar_i_mostrar_llista()

if __name__ == "__main__":
    main()

