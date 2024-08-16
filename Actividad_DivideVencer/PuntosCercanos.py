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
PUNTOS = [(0, 21),(4, 3),(32, 30),(16, 26),(23, 48),(36, 15),(40, 16),(45, 38),(35, 26),(19, 31),(28, 28),(33, 13),(33, 17),(37, 23),(18, 11),(47, 21),(12, 40),(34, 9),(3, 32),(20, 45)]
ORDEN_X = sorted(PUNTOS, key=lambda p: p[0])
# Funcion para obtener la distancia entre dos puntos
def distancia(punto1, punto2):
    res = sqrt( ( ( punto1[0] - punto2[0] ) ** 2) + ( ( punto1[1] - punto2[1] ) ** 2) )
    return res

# Funcion recursiva para obtener la distancia minima entre dos puntos
def parCercano(puntos):
    n = len(puntos)

    # Caso base de nuetra funcion recursiva
    if n <= 3:
        mini = float('inf')
        p1, p2 = None, None

        for i in range(n):
            for j in range(i + 1, n):
                dist = distancia(puntos[i], puntos[j])
                if dist < mini:
                    mini = dist
                    p1, p2 = puntos[i], puntos[j]
        return p1, p2, mini
    
    micha = n // 2
    puntoM = puntos[micha]

    PuntosIzq = list( filter( lambda p: p[0] <= puntoM[0], puntos ) )
    PuntosDer = list( filter( lambda p: p[0] > puntoM[0], puntos ) )

    (p1_Izq, p2_Izq, dist_Izq) = parCercano(PuntosIzq)
    (p1_Der, p2_Der, dist_Der) = parCercano(PuntosDer)

    #print(p1_Izq, p2_Izq, dist_Izq, p1_Der, p2_Der, dist_Der)

    min_dist = min(dist_Izq, dist_Der)
    (p1, p2) = (p1_Izq, p2_Izq) if dist_Izq < dist_Der else (p1_Der, p2_Der)

    res = [p for p in puntos if abs(p[0] - puntoM[0]) < min_dist]

    for i in range(len(res)):
        for j in range( i + 1, min(i + 7, len(res)) ):
            dist_res = distancia(res[i], res[j])
            if dist_res < min_dist:
                min_dist = dist_res
                p1, p2 = res[i], res[j]

    return p1, p2, min_dist

print(parCercano(ORDEN_X))



