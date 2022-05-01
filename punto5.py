class Numeros():

    def factorial(self, num):
        factorial = 1
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,num + 1):
                factorial = factorial*i
        return factorial
    def estimacion_euler(self):
        sum=1
        for i in range(1,101):
            sum += 1/self.factorial(i)
        return sum
    def estimacion_e_x(self,x):
        sum=1
        for i in range(1,101):
            sum= sum+pow(x,i)/self.factorial(i)
        return sum