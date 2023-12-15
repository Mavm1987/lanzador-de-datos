import os 
os.system("cls")
from random import randint
import turtle
from dibujos import *


#turtle.speed(300)

dado1=randint(1,6)
dado2=randint(1,6)

suma =dado1 +dado2



valor_dados(dado1) 
valor_dados(dado2)

print("\n")
print("la suma de los dados es ",suma)
print("\n")