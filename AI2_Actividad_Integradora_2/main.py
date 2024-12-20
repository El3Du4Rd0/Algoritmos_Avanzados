"""
Juan Carlos Calderon García         A01625696
Juan eduardo Rosas Cerón            A01710168
Juan Pablo Hurtado Mireles          A01710778

¿Qué tengo que hacer?

El programa debe:

1. Leer un archivo de entrada que contiene la información de un grafo representado en forma de una matriz de adyacencias 
con grafos ponderados.

- El peso de cada arista es la distancia en kilómetros entre colonia y colonia, por donde es factible meter cableado.
- El programa debe desplegar cuál es la forma óptima de cablear con fibra óptica conectando colonias de tal forma que se 
pueda compartir información entre cualesquiera dos colonias.

2. Debido a que las ciudades apenas están entrando al mundo tecnológico, se requiere que alguien visite cada colonia para 
ir a dejar estados de cuenta físicos, publicidad, avisos y notificaciones impresos. por eso se quiere saber ¿cuál es la 
ruta más corta posible que visita cada colonia exactamente una vez y al finalizar regresa a la colonia origen?

- El programa debe desplegar la ruta a considerar, tomando en cuenta que la primera ciudad se le llamará A, a la segunda 
B, y así sucesivamente.

3. El programa también debe leer otra matriz cuadrada de N x N datos que representen la capacidad máxima de transmisión 
de datos entre la colonia i y la colonia j. Como estamos trabajando con ciudades con una gran cantidad de campos 
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

script_location = Path(__file__).absolute().parent

entrada = []

file_location = script_location / "prueba1.txt"
file = file_location.open()

for row in file:
    
    print(row)