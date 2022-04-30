class Primos():
    def rango_primos(self,start,stop):
        prime_list=[]
        for num in range(start, stop + 1):
            # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime_list.append(num)
        return prime_list