''''
scriptt descripcion:
crea un script python que lance dos dados Nveces y visualie por pantalla los resultados .

La cantidad o número de veces debe ser ingresada por el usuario.
deben lanzarce dos dados 
usara función.
'''
import os 
from random import randint

lan = int(input( '¿cuántas veces deseas lanzar los datos ?:'))

i = 1
while i <= lan :
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(f"Lanzamiento{i}:")
    print(f"Dice 1: {d1}")
    print(f"Dice 1:{d2}")
    print("\n")

i+=1