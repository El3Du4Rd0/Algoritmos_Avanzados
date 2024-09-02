
denominacion_Moneda = []
cambio_Moneda = []

cicle = True

while cicle:
    y = int(input("Denominacion de la moneda \nColoca 0 para terminar: "))
    if(y <= 0):
        cicle = False
    else:
        denominacion_Moneda.append(y)

denominacion_Moneda.sort(reverse=True)

precio = int(input("Precio: "))
pago = int(input("Pago: "))
cambio = pago - precio


# Inicializamos una tabla de DP con infinito
dp = [float('inf')] * (cambio + 1)
dp[0] = 0  # No se necesita ninguna moneda para hacer un total de 0

# Tabla para almacenar la combinación de monedas utilizada
monedas_usadas = [-1] * (cambio + 1)

# Llenamos la tabla DP
for i in range(1, cambio + 1):
    for j in range(len(denominacion_Moneda)):
        if denominacion_Moneda[j] <= i:
            if dp[i - denominacion_Moneda[j]] + 1 < dp[i]:
                dp[i] = dp[i - denominacion_Moneda[j]] + 1
                monedas_usadas[i] = j

# Reconstruimos la solución
resultado = [0] * len(denominacion_Moneda)
while cambio > 0:
    moneda = monedas_usadas[cambio]
    resultado[moneda] += 1
    cambio -= denominacion_Moneda[moneda]

    

print(f"\nTu cambio es de: {cambio} \nCon denominacion de {denominacion_Moneda} \ncon estas monedas   {resultado} ")