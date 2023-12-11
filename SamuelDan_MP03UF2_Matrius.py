# Fes un programa en Python amb un menú per fer la crida a cadascuna de les següents funcions. 
# Cap de les funcions té return. El programa serà amb estructura main.
# Dan Maldonado - 3/12/2023

import random

# Funció de multiplicació
def crear_matriu_2d(n1,n2):
    '''Imprimeix el resultat de multiplicar dos números passats 
    com a paràmetres, els inputs es fan a fora de la funció.'''
    m = [[random.randint(1,100) for i in range(n2)] for i in range(n1)]
    print(m)


def fer_llista_unica(m):
    m_unica = list(set([num for row in m for num in row]))
    return m_unica


def cercar_els_que_acaben_en(m,e):
    None

# Funció principal
def main():
    '''Anem demanant que vol fer l'usuari i
    depenent la resposta inicialitzem una funció
    o un altre.'''
    
    n1 = int(input("Introdueix el primer nombre: "))
    n2 = int(input("Introdueix el segon nombre: "))
    m = crear_matriu_2d(n1,n2)
    

    print(fer_llista_unica(m))


    
    print(cercar_els_que_acaben_en(m))
    

    
    print(cercar_els_que_acaben_en(m))    
        
    
if __name__ == "__main__":
    main()