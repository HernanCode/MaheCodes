# Exercici 3:  calcular_any_traspas: Paràmetre: un sencer. Funcionalitat: donat un any retorna si és un any de traspàs o no (quin tipus haurà de retornar??).
def check_leap(year):
    year = int(year)
    leap = year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0
    return leap


def calc_day(day,month,year):
    module = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6] if check_leap(year) else [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    result = ((year - 1) % 7 + (int((year - 1) / 4) - (3 * int((int((year - 1) / 100) + 1) / 4))) % 7 + module[month - 1] + day % 7) % 7
    return result

