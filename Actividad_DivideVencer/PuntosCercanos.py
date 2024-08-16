'''
Equipo 7:
    Juan Eduardo Rosas Cerón - A01710168
    Juan Carlos Calderón García - A01625696
    Pablo Hazael Hurtado Mireles - A01710778

Actividad 1.3: Aplicaciones de la técnica de programación "divide y vencerás"

7) Par de puntos más cercanos (Closest pair of points)
'''

# Librerías
from math import sqrt

# Constantes
PUNTOS = [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8,9), (9,0), (0,0)]
ORDEN_X = sorted(PUNTOS, key=lambda p: p[0])
ORDEN_Y = sorted(PUNTOS, key=lambda p: p[1])

# Funcion para obtener la distancia entre dos puntos
def distancia(punto1, punto2):
    res = sqrt( ( ( punto1[0] - punto2[0] ) ** 2) + ( ( punto1[1] - punto2[1] ) ** 2) )
    return res

# Funcion recursiva para obtener la distancia minima entre dos puntos
def parCercano(puntosX, puntosY):
    n = len(puntosX)

    # Caso base de nuetra funcion recursiva
    if n <= 3:
        mini = float('inf')
        p1, p2 = None, None

        for i in range(n):
            dist = distancia(puntosX[i], puntosY[i])
            if dist < mini:
                mini = dist
                p1, p2 = puntosX[i], puntosY[i]
        return p1, p2, mini
    
    micha = n // 2
    puntoM = puntosX[micha]

    IzqX = list( filter( lambda p: p[0] <= puntoM[0], puntosX ) )
    DerX = list( filter( lambda p: p[0] > puntoM[0], puntosX ) )

    IzqY = list( filter( lambda p: p[0] <= puntoM[0], puntosY ) )
    DerY = list( filter( lambda p: p[0] > puntoM[0], puntosY ) )

    (p1_Izq, p2_Izq, dist_Izq) = parCercano(IzqX, IzqY)
    (p1_Der, p2_Der, dist_Der) = parCercano(DerX, DerY)

    min_dist = min(dist_Izq, dist_Der)
    (p1, p2) = (p1_Izq, p2_Izq) if dist_Izq < dist_Der else (p1_Der, p2_Der)

    res = [p for p in puntosY if abs(p[0] - puntoM[0]) < min_dist]

    for i in range(len(res)):
        for j in range( i + 1, min(i + 7, len(res)) ):
            dist_res = distancia(res[i], res[j])
            if dist_res < min_dist:
                min_dist = dist_res
                p1, p2 = res[i], res[j]

    return p1, p2, min_dist

print(parCercano(ORDEN_X, ORDEN_Y))



