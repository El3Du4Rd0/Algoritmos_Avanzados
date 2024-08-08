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