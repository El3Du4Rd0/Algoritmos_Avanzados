
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
suma = 0
i = 0

for j in denominacion_Moneda:
    cambio_Moneda.append(0)

copia_denominacion_Moneda = denominacion_Moneda.copy()

while suma <= cambio and copia_denominacion_Moneda:
    if(suma + copia_denominacion_Moneda[0] <= cambio):
        suma += copia_denominacion_Moneda[0]
        cambio_Moneda[i] += 1
    else:
        i += 1
        copia_denominacion_Moneda.pop(0)
        

print(f"\nTu cambio es de: {cambio} \nCon denominacion de {denominacion_Moneda} \ncon estas monedas   {cambio_Moneda} ")