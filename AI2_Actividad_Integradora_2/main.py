"""
Juan Carlos Calderon García         A01625696
Juan eduardo Rosas Cerón            A01710168
Juan Pablo Hurtado Mireles          A01710778

¿Qué tengo que hacer?

El programa debe:

1. Leer un archivo de ciudades que contiene la información de un grafo representado en forma de una matriz de adyacencias 
con grafos ponderados.

- El peso de cada arista es la distancia en kilómetros entre colonia y colonia, por donde es factible meter cableado.
- El programa debe desplegar cuál es la forma óptima de cablear con fibra óptica conectando colonias de tal forma que se 
pueda compartir información entre cualesquiera dos colonias.

2. Debido a que las Nciudades apenas están entrando al mundo tecnológico, se requiere que alguien visite cada colonia para 
ir a dejar estados de cuenta físicos, publicidad, avisos y notificaciones impresos. por eso se quiere saber ¿cuál es la 
ruta más corta posible que visita cada colonia exactamente una vez y al finalizar regresa a la colonia origen?

- El programa debe desplegar la ruta a considerar, tomando en cuenta que la primera ciudad se le llamará A, a la segunda 
B, y así sucesivamente.

3. El programa también debe leer otra matriz cuadrada de N x N datos que representen la capacidad máxima de transmisión 
de datos entre la colonia i y la colonia j. Como estamos trabajando con Nciudades con una gran cantidad de campos 
electromagnéticos, que pueden generar interferencia, ya se hicieron estimaciones que están reflejadas en esta matriz.

- La empresa quiere conocer el flujo máximo de información del nodo inicial al nodo final. Esto debe desplegarse también 
en la salida estándar.
- Por último, investiga un algoritmo que te permite realizar lo siguiente:

4. Teniendo en cuenta la ubicación geográfica de varias "centrales" a las que se pueden conectar nuevas casas, la empresa 
quiere contar con una forma de decidir, dada una nueva contratación del servicio, cuál es la central más cercana 
geográficamente a esa nueva contratación. No necesariamente hay una central por cada colonia. Se pueden tener colonias 
sin central, y colonias con más de una central.
"""

#La libreria pathlib toma la carpeta 
from pathlib import Path
import heapq

script_location = Path(__file__).absolute().parent

ciudades = []
Nciudades = 0

file_location = script_location / "prueba1.txt"
file = file_location.open()

for row in file:
    line = row.strip("\n")
    if len(line) == 1:
        Nciudades = int(line)
    else:
        ciudades.append(list(map(int, line.split())))

extension_min = []

listaPriorizada = []
insertados = [0]

for i in range(len(ciudades)):
    if (i > 0):
        heapq.heappush(listaPriorizada, (ciudades[0][i], 0, i))


while len(insertados) != Nciudades:
    peso, origen, destino = heapq.heappop(listaPriorizada)
    clear = True
    for i in insertados:
        if destino == i:
            clear = False
    if clear:
        extension_min.append((origen, destino))
        insertados.append(destino)
        
        for j in range(len(ciudades)):
            if (j > 0):
                clear2 = True
                for k in insertados:
                    if j == k:
                        clear2 = False
                if clear2:
                    heapq.heappush(listaPriorizada, (ciudades[destino][j], destino, j))

print(extension_min)



    

'''
•	Crea un grafo vacío, inserta cualquier nodo
•	Inserta cualquier nodo
•	Inserta a la fila priorizada a todos sus vecinos
•	Mientras la fila no esté vacía y no se hayan insertado todos los nodos :
    o	Saca un nodo de la fila priorizada
    o	Si el nodo no se ha agregado al grafo:
        	Lo agrega al grafo con su correspondiente arco
        	Mete a sus vecinos en la fila priorizada
'''


