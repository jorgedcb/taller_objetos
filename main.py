from punto1 import Primos
from punto2 import TextoPlano
import re

while True:
    print("Bienvenido")
    print("1 para primos en un rango")
    print("2 para saber # de letras, # de palabras, # palabras repetidas y # de párrafos de un texto plano")
    seleccion = int(input("Que desea realizar: "))

    #punto1
    if seleccion == 1:
        start = int(input("Ingrese el limite inferior: "))
        stop = int(input("Ingrese el limite inferior: "))
        print("Los numeros primos entre", start, "y", stop, "son:")
        p1 = Primos()
        print(p1.rango_primos(start,stop))

    #punto2
    if seleccion == 2:
        texto_ejemplo = TextoPlano()
        texto_ejemplo.info()
    input()

