# Librerías 
import numpy as np

m = int(input("Valor de M (lineas): "))
n = int(input("Valor de N (columnas): "))

laberinto = []
print("Un 1 representa una casilla en la que es posible moverse, un 0 es una casilla por la que NO se puede pasar.")

for i in range(m):
    line = input(f"Introduce la {i + 1}° línea: ")
    x = list(map(int, line.split()))

    while len(x) != n:
        print("La línea ingresada no tiene la cantidad especificada de columnas")
        line = input(f"Introduce la {i + 1}° línea: ")
        x = line.split()
        
    laberinto.append(x)


# Imprimir el laberinto ingresado
print("\nLaberinto ingresado:")
for fila in laberinto:
    print(str(fila))

# Función para verificar si la posición es válida
def esLugarValido(laberinto, x, y):
    # Verifica si está dentro del laberinto y si la celda es accesible (1)
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 1

# Función recursiva para resolver el laberinto
def resolverLaberinto(_laberinto):

    # Crear la matriz de solución con dimensiones adecuadas
    solucion = np.zeros((m, n), dtype=int)

    # Iniciar la búsqueda
    solucion = mover(0, 0, solucion, _laberinto)

    # Verificar si se encontró una solución
    if len(solucion):
        print("\nSolución encontrada en BackTracking:")
        for fila in solucion:
            print(str(fila))
    else:
        print("\nNo hay solución para este laberinto.")   

# Función recursiva para mover al ratón
def mover(x, y, _solucion, _laberinto):
    # Verificar si la posición actual es válida
    if esLugarValido(_laberinto, x, y):
        # Verificar si hemos llegado a la esquina inferior derecha (destino)
        if x == len(_laberinto) - 1 and y == len(_laberinto[0]) - 1:
            _solucion[x][y] = 1
            return _solucion

        # Marcar la celda actual como parte de la solución
        _solucion[x][y] = 1

        # Intentar moverse a la derecha, asegurando que no se sale de los límites
        if y + 1 < len(_laberinto[0]):
            der = mover(x, y + 1, _solucion, _laberinto)
            if len(der):
                return der
        
        # Intentar moverse hacia abajo, asegurando que no se sale de los límites
        if x + 1 < len(_laberinto):
            abajo = mover(x + 1, y, _solucion, _laberinto)
            if len(abajo):
                return abajo

        # Si ninguno de los movimientos funciona, desmarcar la celda (backtracking)
        _solucion[x][y] = 0

    # Si no es un lugar válido o no es el destino, regresar una lista vacía
    return []
    
# Llamada para resolver el laberinto
resolverLaberinto(laberinto)


# =============================================================================================================
# =============================================================================================================
# =============================================================================================================

# Librerías
from queue import PriorityQueue

def ramificacionPoda(laberinto):
    M, N = len(laberinto), len(laberinto[0])
    res = np.zeros((n, m)) # matriz de ceros de respuestos
    cola = PriorityQueue() # cola prioritaria para guardar los datos

    cola.put(( 0, 0, 0, [0,0] )) # Prioridad, x, y, direccion actual

    mov = [(1,0), (-1,0), (0,1), (0,-1)] # posibles sirecicones

    while not cola.empty():

        prio, x, y, camino = cola.get()

        if x == M - 1 and y == N - 1:
            for (i, j) in camino:
                res[i][j] = 1
            return res

        for movimiento in mov:
            new_x, new_y = x + movimiento[0], y + movimiento[1]

            if esLugarValido(laberinto, new_x, new_y) and (new_x, new_y) not in camino:
                new_prio = len(camino) + 1
                new_camino = camino + [( new_x, new_y )]
                cola.put(( new_prio, new_x, new_y, new_camino ))

    return "No se pudo joven"

# resultado = ramificacionPoda(laberinto)
# if isinstance(resultado, np.ndarray):
#     for fila in resultado:
#         print(" ".join(map(str, map(int, fila))))