# Complejidad: O(N^2) para el pre-procesamiento y O(N^2 log(N)) para el coloreo del grafo
def GraphColor(Matriz):
    N = len(Matriz)
    MGrados = [0] * N

    for i in range(N):
        Grado = 0
        for j in Matriz[i]:
            if j > 0:
                Grado += 1
        
        MGrados[i] = (i, Grado)
    
    print(MGrados)
    MGrados.sort(key=lambda x: x[1], reverse=True)
    print(MGrados)

    AColor = [None] * N
    Color = 0

    #Revisar nodos en orden
    for Nodo in MGrados:
        #Si el nodo actual no está coloreado
        if AColor[Nodo[0]] == None:
            #Coloreo el nodo actual
            AColor[Nodo[0]] == Color
            for Adj in range(N):
                MAdjacentes = []
                #Revisar los nodos no adjacentes que no estén coloreados
                if Matriz[Nodo[0]][Adj] == 0 and AColor[Adj] == None:
                    if len(MAdjacentes) == 0:
                        AColor[Adj] = Color
                        #Añadir nodos adjacentes a arreglo de nodos adjacentes
                        for j in range(N):
                            if Matriz[i][j] > 0:
                                MAdjacentes.append(j)
                    else:
                        Clear = True
                        #Revisar que el nodo que se está revisando no es adjacente al que se acaba de colorear
                        for i in MAdjacentes:
                            if Adj == i:
                                Clear = False
                                break
                        if Clear:
                            Color[Adj] = Color
                            #Añadir nodos adjacentes a arreglo de nodos adjacentes
                            for j in range(N):
                                if Matriz[i][j] > 0:
                                    MAdjacentes.append(j)
            Color += 1
    
    return AColor


N = 5
MA = [[0, 0, 1, 0, 1],
      [0, 0, 1, 1, 1],
      [1, 1, 0, 1, 0],
      [0, 1, 1, 0, 1],
      [1, 1, 0, 1, 0]]


Colors = GraphColor(MA)

for i in range(len(Colors)):
    print(f"Vértice {i}: Color asignado: {Colors[i]}")