import random
import utils

# Ex1
def crear_matriu_2d(n1, n2):
    m = [[random.randint(1, 100) for i in range(n2)] for i in range(n1)]
    print(m)
    return m

# Ex2
def print_matrix(m):
    for row in m:
        print(*row)

# Ex3
def llistar_multiples(m,n):
    multiples = [num for row in m for num in row if num % n == 0]
    return multiples

# Ex4
def fer_llista_unica(m):
    m_unica = list(set([num for row in m for num in row]))
    return m_unica

# Ex5
def buscar_min_i_max(m):
    m1d = [num for row in m for num in row]
    return(min(m1d),max(m1d))

# Ex6
def cercar_els_que_acaben_en(m,e):
    n_ultim = [num for row in m for num in row if str(num)[-1] == str(e)]
    return n_ultim

# Ex7
def crear_quadrat(s,c):
    quadrat = [[c for j in range(s)] for i in range(s)]
    return quadrat

# Funció principal
def main():
    n1 = utils.secure_int("Introdueix el primer nombre: ")
    n2 = utils.secure_int("Introdueix el segon nombre: ")
    m = crear_matriu_2d(n1, n2)
    
    print_matrix(m)
    
    n = utils.secure_int("Introdueix un nombre (1-10): ", 1, 10)
    print(llistar_multiples(m,n))
    
    print(fer_llista_unica(m))
    
    print(buscar_min_i_max(m))

    e = utils.secure_int("Introdueix un nombre (0-9): ", 0, 9)
    print(cercar_els_que_acaben_en(m,e))
    
    s = utils.secure_int("Introdueix un nombre (10-20): ", 10, 20)
    print(crear_quadrat(s,"*"))
    
if __name__ == "__main__":
    main()
