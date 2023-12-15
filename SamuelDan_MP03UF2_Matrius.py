# Tasca de Funcions i Matrius de dues dimensions
# Feta per: Samuel Hernan i Dan Maldonado
# Data: 13/12/2023

import random
import utils

# Ex1
def crear_matriu_2d(n1, n2):
    '''Crea una matriu de dues dimensions agafant els nombres que hi passem.'''
    m = [[random.randint(1, 100) for i in range(n2)] for i in range(n1)]
    return m

# Ex2
def imprimir_matriu(m):
    '''Imprimeix la matriu de manera ordenada ajustant l'amplada dels nombres.'''
    max_width = max(len(str(num)) for row in m for num in row)
    
    for row in m:
        print(" ".join(f"{num:>{max_width}}" for num in row))

# Ex3
def llistar_multiples(m,n):
    '''Retorna una llista amb els múltiples de n presents a la matriu.'''
    multiples = [num for row in m for num in row if num % n == 0]
    return multiples

# Ex4
def fer_llista_unica(m):
    '''Retorna una llista única amb els valors de la matriu.'''
    m_unica = list(set([num for row in m for num in row]))
    return m_unica

# Ex5
def buscar_min_i_max(m):
    '''Retorna el valor mínim i màxim de la matriu.'''
    m1d = [num for row in m for num in row]
    return(min(m1d), max(m1d))

# Ex6
def cercar_els_que_acaben_en(m,e):
    '''Retorna una llista amb els nombres que acaben en el dígit e.'''
    n_ultim = [num for row in m for num in row if str(num)[-1] == str(e)]
    return n_ultim

# Ex7
def crear_quadrat(s,c):
    '''Crea una matriu quadrada de mida s x s inicialitzada amb el caràcter c.'''
    quadrat = [[c for j in range(s)] for i in range(s)]
    return quadrat

# Ex8
def inicialitzar_matriu(q,c):
    '''Inicialitza tots els elements de la matriu amb el caràcter c.'''
    matriu = [[c for j in i] for i in q]
    for row in matriu:
        print(*row)

# Ex9
def diagonal(q,c):
    '''Posa el caràcter c a les diagonals de la matriu quadrada.'''
    for i in range(len(q)):
        q[i][i] = c
    return q

# Ex10
def posar_en_diagonal(q,c):
    '''Posa el caràcter c a les diagonals de la matriu quadrada.'''
    diagonal(q,c)
    diagonal(q[::-1],c)
    return q

# Ex11
def dibuixar_creu(q,c):
    '''Dibuixa una creu amb el caràcter c en una matriu quadrada de mida senar.'''
    mid = len(q) // 2 
    for i in range(len(q)):
        q[i][mid] = c  
        q[mid][i] = c  
    return q

# Funció principal
def main():
    n1 = utils.secure_int("Introdueix el primer nombre: ")
    n2 = utils.secure_int("Introdueix el segon nombre: ")
    m = crear_matriu_2d(n1, n2)
    
    imprimir_matriu(m)
    
    n = utils.secure_int("Introdueix un nombre (1-10): ", 1, 10)
    print(llistar_multiples(m, n))
    
    print(fer_llista_unica(m))
    
    print(buscar_min_i_max(m))

    e = utils.secure_int("Introdueix un nombre (0-9): ", 0, 9)
    print(cercar_els_que_acaben_en(m, e))
    
    # Comprovem que sigui senar
    senar = False
    while not senar:
        s = utils.secure_int("Introdueix un nombre (10-20): ", 10, 20)
        if s % 2 != 0:
            senar = True
    crear_quadrat(s, "*")

    q = crear_matriu_2d(5, 5)
    inicialitzar_matriu(q, "-")

    q = crear_quadrat(s, "-")
    diagonal = posar_en_diagonal(q, "*")
    imprimir_matriu(diagonal)
    
    imprimir_matriu(dibuixar_creu(diagonal, "|"))
    
if __name__ == "__main__":
    main()
