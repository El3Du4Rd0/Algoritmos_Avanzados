"""
Juan Carlos Calderon García         A01625696
Juan Eduardo Rosas Cerón            A01710168
Pablo Hazael Hurtado Mireles          A01710778
"""

from pathlib import Path
from ast import literal_eval as make_tuple

# Lectura de Datos

script_location = Path(__file__).absolute().parent

Nciudades = NuevaCentral = 0
ciudades = []
capacidad = []
centrales = []

file_location = script_location / "Equipo_06_Entrada_3.txt"
file = file_location.open()

counter = 0
for row in file:
    line = row.strip("\n")
    if line == "":
        counter+= 1
    else:
        match counter:
            case 0:
                Nciudades = int(line)
            case 1:
                ciudades.append(list(map(int, line.split())))
            case 2:
                capacidad.append(list(map(int, line.split())))
            case 3:
                centrales.append(make_tuple(line))
            case 4:
                NuevaCentral = make_tuple(line)

'''
1. El programa debe desplegar cuál es la forma óptima de cablear con fibra óptica conectando colonias de tal forma que se 
pueda compartir información entre cualesquiera dos colonias.

Resultado: Forma de cablear las colonias con fibra (lista de arcos de la forma (A,B)).

Complejidad O(n^2)
'''
import heapq

def GrafoExtensionMin():
    extension_min = []
    listaPriorizada = []
    insertados = [False] * Nciudades

    #Inserta el primer nodo al grafo y sus adjacencias a la fila
    insertados[0] = True

    for i in range(len(ciudades)):
        if (i > 0):
            heapq.heappush(listaPriorizada, (ciudades[0][i], 0, i))

    #Termina cuando se han añadido todos los nodos
    while len(extension_min) != Nciudades - 1:
        #Toma el elemento con la distancia más pequeña que no se haya insertado
        _, origen, destino = heapq.heappop(listaPriorizada)
        if not insertados[destino]:
            #Inserta el nodo obtenido al grafo y sus adjacencias a la fila
            extension_min.append((origen, destino))
            insertados[destino] = True
            
            for j in range(len(ciudades)):
                if (j > 0):
                    if not insertados[j]:
                        heapq.heappush(listaPriorizada, (ciudades[destino][j], destino, j))
    
    return extension_min

ExtensionMin = GrafoExtensionMin()
arcos = ""
for k in range(len(ExtensionMin)):
    arcos += str(ExtensionMin[k])
    if k + 1 != len(ExtensionMin):
        arcos += ", "
        
print(f"1.- Arcos para cablear colonias: \n{arcos}\n")

'''
2. ¿cuál es la ruta más corta posible que visita cada colonia exactamente una vez y al finalizar regresa a la colonia origen?

Resultado: ruta a seguir por el personal que reparte correspondencia, considerando inicio y fin en al misma colonia y que
la primera ciudad se le llamará A, a la segunda B, y así sucesivamente.

Complejidad: O(n!)
'''

from itertools import permutations

def tsp(grafo, inicio):

    # Obtenermos todas las colonias sin la inicial
    colonias = []
    for i in range(Nciudades):
        if i != inicio:
            colonias.append(i)

    # Guardamos la distancia minima y todas las permutaciones de las rutas
    distancia_min = float('inf')
    permutar_rutas = permutations(colonias)
    ruta = []

    for ruta_permutada in permutar_rutas:
        peso = 0
        k = inicio
        ruta_actual = [inicio]
        
        # calculamos el peso de la ruta actual
        for colonia in ruta_permutada:
            peso += grafo[k][colonia]
            k = colonia
            ruta_actual.append(colonia)

        # Agregamos el punto inicial en el peso y en la ruta de colonias
        peso += grafo[k][inicio]
        ruta_actual.append(inicio)

        # Actualizamos la ruta y la distancia minima si encontramos una mejor
        if peso < distancia_min:
            distancia_min = peso
            ruta = ruta_actual

    return distancia_min, ruta

d, r = tsp(ciudades, 0)
print(f"2.- La ruta de ciudades es: {r} \nCon una distancia de {d}\n")

'''
3. La empresa quiere conocer el flujo máximo de información del nodo inicial al nodo final. Esto debe desplegarse también 
en la salida estándar.

Resultado: valor de flujo máximo de información del nodo inicial al nodo final.

Complejudad O(VA^2) donde V son los cértices y A las aristas
'''

def BFS(capacidadRes, inicio, final):
        
    visitados = [False]*(Nciudades)
    queue = []
    camino = [-1] * Nciudades

    queue.append(inicio)
    visitados[inicio] = True

    while queue:        
        eval = queue.pop(0)
        
        for i in range(len(capacidadRes[eval])):
            if not visitados[i] and capacidadRes[eval][i] > 0:
                queue.append(i)
                visitados[i] = True
                camino[i] = eval
                if i == final:
                    return True, camino
                    
    return False, camino

def FlujoMaximo(inicio, final):
    capacidadRes = capacidad
    flujoMax = 0

    #Busca el camino inicial
    exiteCamino, camino = BFS(capacidadRes, inicio, final)
    
    #Termina cuando sno haya caminos hacia el destino
    while exiteCamino:
        flujoCamino = float("Inf")

        #Encontrar el flujo del camino encontrado
        next = final

        while(next != inicio):
            flujoCamino = min(flujoCamino, capacidadRes[camino[next]][next])
            next = camino[next]
        
        flujoMax += flujoCamino

        #Actualizar la capacidad residual de vértices visitados
        next = final

        while(next != inicio):
            eval = camino[next]
            capacidadRes[eval][next] -= flujoCamino
            capacidadRes[next][eval] += flujoCamino
            next = eval
        
        #Busca nuevo caminp
        exiteCamino, camino = BFS(capacidadRes, inicio, final)
    
    return flujoMax

print(f"3.- El flujo máximo de la red es de: {FlujoMaximo(0, 3)}\n")

'''
4. Investiga un algoritmo que te permite realizar lo siguiente:
Teniendo en cuenta la ubicación geográfica de varias "centrales" a las que se pueden conectar nuevas casas, la empresa 
quiere contar con una forma de decidir, dada una nueva contratación del servicio, cuál es la central más cercana 
geográficamente a esa nueva contratación. No necesariamente hay una central por cada colonia. Se pueden tener colonias 
sin central, y colonias con más de una central.

Resultado: la salida será la distancia más corta entre dos puntos: el de la ubicación de la nueva central con respecto al más cercano.

Complejidad: O(n)
'''

from math import sqrt

def punto_mas_cercano(puntos, p):

    punto_cercano = None
    min_distancia = float('inf')
    
    for punto in puntos:
        distancia = sqrt( (punto[0] - p[0])**2 + (punto[1] - p[1])**2 ) # Teorema de pitagoras
        
        # Buscamos la distancia mas corta y su punto más cercano
        if distancia < min_distancia:
            min_distancia = distancia
            punto_cercano = punto
    
    return punto_cercano, min_distancia

c, nc = punto_mas_cercano(centrales, NuevaCentral)

print(f"4.- Central más cercana con respecto a {NuevaCentral}: {c}\nCon una distancia de: {nc}")

