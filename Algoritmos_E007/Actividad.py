import random
import math

#Algoritmo 1
#un programa que permita saber en cuantos días es posible surtir un pedido de N camisas

linea1 = []
linea2 = []
No_camisetas = int(input("Escribe el número de camisetas del pedido: "))

#Crear datos de prueba
for i in range(5):
    linea1.append(random.randint(5,20))
    linea2.append(random.randint(5,20))

#Obtener el proedio de camisetas producidas en un día
total_linea = linea1 + linea2
avg_total = 0

for i in total_linea:
    avg_total += i

avg_total /= len(total_linea)

#Calcular tiempo del pedido
dias = round(No_camisetas / avg_total)

print("\nEl pedido tomará aproximadamente " + str(dias) + " días en producirse\n")

#Algoritmo 2
#Saber cuántos refrescos puede llenar la máquina de una sola vez, sin recargar el contenedor.
#Solo se tienen los datos del radio de la base y la altura medidos en metros. 

radio = int(input("Escribe el radio del contenedor de la embotelladora (m): "))
altura = int(input("Escribe la altura del contenedor de la embotelladora (m): "))
mililitros = int(input("Escribe el contenido en mililitros de cada botella: "))

#En mililitros
volumen = (math.pi * (radio**2)) * 1000000

botellas = math.floor(volumen/mililitros)

print("\nLa embotelladora puede embotellar " + str(botellas) + " botellas con un solo tanque")


'''
3. Que solicite un número que indica cuántos números aleatorios (positivos y
negativos) se mostrarán.
'''
print("Ingresa el numero inferior: ")
num_infer = int(input())

print("Ingresa el numero superior: ")
num_super = int(input())

random_num = random.randint(num_infer, num_super)
print(random_num)


'''
4. Se muestren todos los números, la suma y el promedio de la siguiente serie
3, 6, 9, 12,… 99. 
'''
lista = []
i = 3
total = 0
count = 0
while i != 99:
    lista.append(i)
    total = total + i
    i = i + 3

total = total + i
lista.append(i)

for i in lista:
    count = count + 1

prom = total / count

print(lista)
print(total)
print(prom)

"""
5. Se desea calcular los primeros 15 números de la siguiente sumatoria:
Suma = 1 + 1/2² + 1/3³ + 1/4² + 1/5⁵ + 1/6² + ...
"""
def sumatoria(n):
    res = 0
    if n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            if (i % 2) == 0:
                res += (1/i**2)
            else:
                res += (1/i**i)
        return res

print("Resultado: " + str(sumatoria(15)))

# 6. Se desea calcular el factorial de un número dado por el usuario.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
    
numFactorial = int(input("Factorial: "))
print("Resultado: " + str(factorial(numFactorial)))