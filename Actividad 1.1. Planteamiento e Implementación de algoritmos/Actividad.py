

from random import *


# Se desea calcular el factorial de un número dado por el usuario.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
    
x = int(input())
print(factorial(x))

''' 3. Que solicite un número que indica cuántos números aleatorios (positivos y
negativos) se mostrarán.'''
print("Ingresa el numero: ")
num_infer = input()
random_num = randrange(0, 100, 1)
print(random_num)


'''4. Se muestren todos los números, la suma y el promedio de la siguiente serie
3, 6, 9, 12,… 99. '''