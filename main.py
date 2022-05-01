import re
from punto1 import Primos
from punto2 import TextoPlano
from punto3y4 import Datos
from punto5 import Numeros


while True:
    print("Bienvenido")
    print("1: para primos en un rango")
    print("2: Calcular # de letras, # de palabras, # palabras repetidas y # de párrafos de un texto plano")
    print("3: Cifrar numero de 4 digitos")
    print("4: Decifrar numero de 4 digitos")
    print("5: Factorial de un numero")
    print("6: Estimación del valor de euler")
    print("7: Estimación de exp(x)")
    try: 
        seleccion = int(input("Que desea realizar: "))
    except ValueError:
        print("Use valores enteros entre 1 y 7 para realizar la selección")
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
        num3 = Datos()
        print("numero cifrado",num3.cifrar())
    elif seleccion == 4:
        num4 = Datos()
        print("numero decifrado",num4.decifrar())
    elif seleccion == 5:
        num5 = Numeros()
        try:
           num = int(input("Ingrese un numero entero positivo: "))
           print("El factorial de",num,"es",num5.factorial(num))
        except:
            print("Debe ingresar un numero entero")
    elif seleccion == 6:
        num6 = Numeros()     
        print("Valor de Euler es",num6.estimacion_euler())

    elif seleccion == 7:
        num7 = Numeros()
        try:
           num = int(input("Ingrese un numero entero positivo: "))
           print("El exponencial de",num,"es",num7.estimacion_e_x(num))
        except:
            print("Debe ingresar un numero entero")

    input()

