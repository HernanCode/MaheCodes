# Fes un programa que accepta 2 arguments. En el primer comprova que és un string que només 
# conté lletres, en el segon comprova que són dígits i el transforma a sencer. 
# Si és així, es fa un print de l’string tantes vegades com indica el segon paràmetre.


import sys 


import sys

def check_params(char,num):
    is_letter = char.isalpha()
    is_num = num.isnumeric()
    
    if is_letter and is_num:
        print(char*int(num))
    else:
        print(f"El valor {char} no es una letra") if not is_letter else ""
        print(f"El valor {num} no es un numero") if not is_num else ""
        
    
def main():
    char = sys.argv[1]
    num = sys.argv[2]
    check_params(char,num)
    

if __name__ == "__main__":  
    main()

