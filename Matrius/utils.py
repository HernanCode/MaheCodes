def check_int(num):
    is_int = num.isdigit()
    while not is_int:
        print("Error el valor no es un numero")
        num = input("Introduzca el valor de nuevo: ")
        is_int = num.isdigit()
    return int(num)

def correct_range(num, min=None,max=None):
    # Tiene minimos pero no tiene máximo
    if min is not None and max is None:
        return num >= min
    # No tiene minimo pero si hay maximo
    elif min is None and max is not None:
        return num <= max
    # Hay minimo y máximo
    elif min is not None and max is not None:
        return num >= min and num <= max
    # No tiene minimo ni máximo 
    else:
        return True
    
def secure_int(text, min=None, max=None):
    correct_num = False
    while not correct_num:
        num = input(text)
        num = check_int(num)
        correct_num = correct_range(num, min, max)
    return num
