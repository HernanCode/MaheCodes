# Fes un programa que comprova que el nombre d’arguments és superior a 1, que són alfabètics (lletres) 
# i en aquest cas que els ordeni alfabèticament. Sinó que mostri quin error hi ha.

import sys

def comprovar_i_ordenar():
    if len(sys.argv) > 1 and all(element.isalpha() for element in sys.argv[1:]):
        print(sorted(sys.argv[1:]))
        
    else:
        print("ERROR: No tots els elements són alfabètics.")

if __name__ == "__main__":
    comprovar_i_ordenar()
