#=========================================================
#Lectura del Archivo
#=========================================================
archivo = True
while archivo:
    nombre = str(input("Nombre del Archivo (sin extension) : "))
    nombre = nombre + ".txt"
    try:
        fichero = open(nombre)
        archivo = False
    except:
        print("Archivo no valido")

#=========================================================
#Comprobacion del multiplo
#=========================================================
multiplo = True
while multiplo == True:
    try:
        n = int(input("Ingresa un multiplo de 4 entre 16 y 64: "))

        if(n >= 16 and n <= 64 and n % 4 == 0):
            multiplo = False
        else:
            print("Este numero no es multiplo de 4")
    except:
        print("Entrada no valida")

#=========================================================
#Leemos el archivo y ponemos cada letra en un rengon de la matriz
#=========================================================
lista = []
linea_lista = []

for linea in fichero.readlines():
    for letter in linea:
        if(len(linea_lista) < n):
            linea_lista.append(letter)
        elif (len(linea_lista) >= n):
            lista.append(linea_lista)
            linea_lista = []
            linea_lista.append(letter)
#Comprobamos si la ultima linea esta entera
if(len(linea_lista) < n):
    while len(linea_lista) < n:
        linea_lista.append(chr(n)) #Convertimos n en su caracter a traves de ascii
#Colocamos la ultima linea        
lista.append(linea_lista)
#Mostramos el resultado
for i in lista:
    print(i)


#=========================================================
#Sumamos de las columnas con el modulo ASCII
#=========================================================
count = 0
suma = 0
columnas_n = []

while count < n:
    for i in lista:
        suma = suma + ord(i[count])
    columnas_n.append(suma)
    suma = 0
    count = count + 1
#Sacamos %256
columnas_255 = []
for i in columnas_n:
    columnas_255.append(i%256)
print(columnas_255)

#=========================================================
#Convmertimos a Hexadecimal
#=========================================================
columnas_hex = []
for i in columnas_255:
    columnas_hex.append(hex(i).replace("0x",""))

columnas_hex_concat = []
hex_val = ""
concat = n/4
count = 0
while columnas_hex:
    hex_val = ""
    while count < concat:
        hex_val = hex_val + columnas_hex[0]
        count = count + 1
        columnas_hex.pop(0)
    
    count = 0
    columnas_hex_concat.append(hex_val)
columnas_hex_concat.append(hex_val)
print(columnas_hex_concat)