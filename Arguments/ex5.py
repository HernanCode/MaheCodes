# Fes un programa que accepta una data com a argument, en 
# format dd/mm/aaaa, - comprova que el format és correcte tenint en compte
# que hi ha mesos 1-12 que tenen 28, 29, 30 i 31 dies -, i ens retorna a 
# quin dia de la setmana correspon. Podeu fer servir weekday de la biblioteca datetime, 
# però el dia ha de mostrar-se en català. [31,28,31,..] []

from mahedate import calc_day
import sys


def main():
    days = ["Diumenge", "Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte"]
    months = ["Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre"]
    date = sys.argv[1].split("/")
    day = calc_day(int(date[0]),int(date[1]),int(date[2]))
    print(f"{days[day]} {date[0]} de {months[int(date[1]) - 1]} del {date[2]}")

if __name__ == "__main__":  
    main()

