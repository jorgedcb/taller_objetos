import numpy as np
class Numeros:
    def cifrar(self): 
        try:
            num = input("Ingrese numero de 4 cifras: ")
            if len(num)==4:
                x = [int(a) for a in str(num)]
                array = (np.array(x)+7)%10
                u = array[-1]
                p = array[0]
                array[0] = array[2]
                array[2] = p
                array[-1] = array[1]
                array [1] = u
                a = ''.join(map(str, array))
                return a
            else:
                print("El numero debe ser de 4 digitos")
        except ValueError:
            print("That's not an int!")
    def decifrar(self):
        try:
            num = int(input("Ingrese numero de 4 cifras: "))
            if num < 9999 and num > 999:
                if len(num) == 4:
                    x = [int(a) for a in num]
                    print(x)
                    array = np.array(x)+3-((np.array(x)//7)*10)
                    print (array)
                    u = array[-1]
                    p = array[0]
                    array[0] = array[2]
                    array[2] = p
                    array[-1] = array[1]
                    array [1] = u
                    a = ''.join(map(str, array))
                return a
            else:
                print("El numero debe ser de 4 digitos")
        except ValueError:
            print("That's not an int!")

