'''
Juan Carlos Calderónn García
Juan Eduardo Rosas Cerón
Pablo Hazael Hurtado Mireles

Actividad 3.2b Implementación de "Dijkstra and Floyd" 
'''

# Librerías
import heapq

# Función para ejecutar el algoritmo de Dijkstra desde un nodo de inicio dado
# Complejidad O(n^3)
def dijkstra(matrix):
    n = len(matrix)
    distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
        pq = [(0, i)]  # (distance, node)
        
        while pq:
            current_distance, node = heapq.heappop(pq)
            
            if current_distance > distances[i][node]:
                continue
            
            for neighbor in range(n):
                if matrix[node][neighbor] != -1:  # -1 indica que no hay conexión
                    distance = current_distance + matrix[node][neighbor]
                    if distance < distances[i][neighbor]:
                        distances[i][neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
                    
    return distances


# Función para ejecutar el algoritmo de Floyd-Warshall
# Complejidad O(n^3)
def floyd_warshall(matrix):
    n = len(matrix)
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
    
    # Inicializar la matriz de distancias con la matriz de adyacencia
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != -1:
                dist[i][j] = matrix[i][j]
    
    # Actualizar distancias usando el algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < float('inf') and dist[k][j] < float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


# Función principal para leer la entrada y ejecutar ambos algoritmos
def main():
    # Leer el número de nodos
    n = int(input("Escribe cuantas filas va a tener: "))
    
    # Leer la matriz de adyacencia
    matrix = []
    for _ in range(n):
        row = list(map(int, input(f"Escribe la fila {len(matrix)} : ").split()))
        matrix.append(row)
    
    # Ejecutar y mostrar el resultado de Dijkstra para cada nodo
    print("\nDijkstra:")
    distances = dijkstra(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                print(f"node {i + 1} to node {j + 1}: {distances[i][j] if distances[i][j] != float('inf') else 'unreachable'}")

    # Ejecutar y mostrar el resultado de Floyd-Warshall
    print("\nFloyd:")
    floyd_distances = floyd_warshall(matrix)
    for row in floyd_distances:
        print(" ".join(str(x if x != float('inf') else "inf") for x in row))


# Funcion main
main()