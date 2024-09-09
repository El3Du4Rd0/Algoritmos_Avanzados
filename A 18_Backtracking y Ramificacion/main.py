import numpy as np

m = int(input("Valor de M: "))
n = int(input("Valor de N: "))

laberinto = np.zeros((m,n))
for i in range(m):
    for j in range(n):
        valor = int(input(f"{i} , {j}: "))
        laberinto[i][j] = valor


print(laberinto)



# Función para verificar si la posición es válida
def esLugarValido(laberinto, x, y):
    # Verifica si está dentro del laberinto y si la celda es accesible (1)
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 1

# Función recursiva para resolver el laberinto
def resolverLaberinto(laberinto):

    solucion = np.zeros((m,n))

    # Función auxiliar recursiva
    def mover(x, y):
        # Si hemos llegado a la esquina inferior derecha, el laberinto está resuelto
        if x == len(laberinto) - 1 and y == len(laberinto[0]) - 1:
            solucion[x][y] = 1
            return True

        # Verificar si el movimiento es válido
        if esLugarValido(laberinto, x, y):
            # Marcar la celda actual como parte de la solución
            solucion[x][y] = 1

            # Moverse hacia la derecha en el laberinto
            if mover(x, y + 1):
                return True
            
            # Moverse hacia abajo en el laberinto
            if mover(x + 1, y):
                return True

            

            # Si ninguno de los movimientos funciona, desmarcar la celda (backtracking)
            solucion[x][y] = 0

        return False

    # Iniciar la solución desde la esquina superior izquierda
    if mover(0, 0):
        # Imprimir la matriz de solución
        for fila in solucion:
            print(fila)
        return True
    else:
        print("No hay solución para este laberinto.")
        return False


resolverLaberinto(laberinto)