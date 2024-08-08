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
print("Ingresa el numero inferior: ")
num_infer = int(input())

print("Ingresa el numero superior: ")
num_super = int(input())

random_num = randint(num_infer, num_super)
print(random_num)


'''4. Se muestren todos los números, la suma y el promedio de la siguiente serie
3, 6, 9, 12,… 99. '''
lista = []
i = 3
total = 0
count = 0
while i != 99:
    lista.append(i)
    total = total + i
    count = count + 1
    i = i + 3

total = total + i
count = count + 1
lista.append(i)


prom = total / count

print(lista)
print(total)
print(prom)