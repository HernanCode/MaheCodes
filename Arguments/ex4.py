# Fes un programa que comprova que el nombre d’arguments és superior a 1, que són alfabètics (lletres) 
# i en aquest cas que els ordeni alfabèticament. Sinó que mostri quin error hi ha.

import sys

def comprovar_i_ordenar(arg):
    if len(arg) > 1 and all(element.isalpha() for element in arg[1:]):
        print(sorted(arg[1:]))
    else:
        print("ERROR: No tots els elements són alfabètics.")

def main():
    arg = sys.argv
    comprovar_i_ordenar(arg)
    
if __name__ == "__main__":
    main()
