''''
scriptt descripcion:
crea un script python que lance dos dados Nveces y visualie por pantalla los resultados .

La cantidad o número de veces debe ser ingresada por el usuario.
deben lanzarce dos dados 
usara función.
'''
import os 
from random import randint



i = 1
status = True 
while status :
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(f"Lanzamiento{i}:")
    print(f"Dice 1: {d1}")
    print(f"Dice 1:{d2}")
    print("\n")
i+=1
while True:
try_again = input("¿Try again?[s\S\n\N]")
if try_again == 's' or try_again == 'S' or try_again == 'n' or try_again ==
    status_try_again = False
    else:
        print("invalid option, please press s\S\n(N)")
     break 
if try_again =='n' or 'N':
    break