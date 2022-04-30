import re
from tkinter import Tk    
from tkinter.filedialog import askopenfilename

class TextoPlano:
    def __init__(self):
        self.num_palabras =0
        self.num_letras =0
        self.num_parrafos =0

    def info(self):  
        Tk().withdraw() 
        filename = askopenfilename() 
        if filename == ():
            print("No se selecciono ningun archivo")
            return
        elif not filename.endswith('.txt'):
             print("El archivo tiene que ser .txt")
             return
        elif filename.endswith('.txt'):
            text = open(filename)
            print('Numero de letras:', self.calcular_num_letras(text)," \n")
            text = open(filename)
            print('Numero de palabras:', self.calcular_num_palabras(text)," \n")
            text = open(filename)
            print("Numero de parrafos:", self.calcular_num_parrafos(text)," \n")
            text = open(filename)
            d = self.palabras_repetidas(text)
            print("Palabras repetidas:")
            if d:
                for key in list(d.keys()):
                    print(key, ":", d[key])
            else: 
                print("o hay palabras repetidas")

    
    def calcular_num_palabras(self,text):
        number_of_words = 0
        for lines in text:
            number_of_words += len(lines.split())
        self.num_palabras = number_of_words
        return number_of_words
    
    def calcular_num_letras(self,text):
        letras = 0
        for line in text:
            letras += len(re.sub("[^a-zA-Z]", "", line))
        self.num_letras=letras
        return letras
    
    def palabras_repetidas(self,text):
        d = dict()
        l = []
        for line in text:
            line = line.rstrip()
            line = line.lower()
            words = re.split(',|_|-|!|\s|\(|\)|\?|\¿|\.|\:|\;', line)
            for word in words:
                if word.isalpha():
                    if word in d:
                        d[word] = d[word] + 1
                    else:
                        if word in l :
                            d[word] = 2
                        else:
                            l.append(word)
                            

        return d
        
    def calcular_num_parrafos(self,text):
        n = 0
        a = False
        for line in text:
            line = line.rstrip()
            if line == "":
                a = True
            elif n==0 and line !="":
                n=1
            elif a:
                n += 1

        self.num_parrafos = n
        return n  