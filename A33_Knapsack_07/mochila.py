'''
    Juan Eduardo Rosas Cerón - A01710168
    Juan Carlos Calderón García - A01625696
    Pablo Hazael Hurtado Mireles - A01710778

    Knapsack Algorithm

    Complejidad: O(N * W)

'''

def knapsack(N, values, weights, W):
    # Crear una matriz para almacenar los valores óptimos
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    
    # Llenar la matriz dp
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                # Si el peso del elemento actual es menor o igual al peso w,
                # tomar el máximo entre incluir el elemento o no incluirlo
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # No incluir el elemento actual ya que excede el peso
                dp[i][w] = dp[i - 1][w]

    print("Matriz generada:")
    for row in dp:
        print(row)

    print("Beneficio óptimo:", dp[N][W])

# Ejemplo de uso:
values = [1, 1, 2, 3, 5, 8, 13]
weights = [2, 3, 5, 7, 11, 13, 17]
N = len(values)
W = 23

knapsack(N, values, weights, W)