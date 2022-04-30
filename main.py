from punto1 import Primos
from punto2 import TextoPlano

import re

from punto3 import Numeros

while True:
    print("Bienvenido")
    print("1: para primos en un rango")
    print("2: Calcular # de letras, # de palabras, # palabras repetidas y # de párrafos de un texto plano")
    print("3: Cifrar numero de 4 digitos")
    seleccion = int(input("Que desea realizar: "))

    #punto1
    if seleccion == 1:
        try:
            start = int(input("Ingrese el limite inferior: "))
            stop = int(input("Ingrese el limite inferior: "))
            print("Los numeros primos entre", start, "y", stop, "son:")
            p1 = Primos()
            print(p1.rango_primos(start,stop))
        except ValueError:
            print("los limites deben ser enteros positivos")
    elif seleccion == 2:
        texto_ejemplo = TextoPlano()
        texto_ejemplo.info()
    elif seleccion == 3:
        num = Numeros()
        print("numero cifrado",num.cifrar())
    elif seleccion == 4:
        num4 = Numeros()
        print("numero decifrado",num4.decifrar())

    input()

