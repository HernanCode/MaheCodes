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

# Funció principal
def main():
    n1 = int(input("Introdueix el primer nombre: "))
    n2 = int(input("Introdueix el segon nombre: "))
    m = crear_matriu_2d(n1, n2)
    
    print(print_matrix(m))
    
    print(llistar_multiples(m,n))
    
    print(fer_llista_unica(m))
    
    print(buscar_min_i_max(m))
    
    
if __name__ == "__main__":
    main()
