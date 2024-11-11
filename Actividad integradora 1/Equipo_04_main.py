"""
El programa lee varios archivos y les aplica los siguiente algoritmos:
Algoritmo Z, Manahcer y Longest Common Substring

Juan Eduardo Rosas Cerón - A01710168 
Juan Carlos Calderón García - A01625696 
Pablo Hazael Hurtado Mireles - A01710778 

Creacion- 02//10/2024
Modifcacion- 07/10/2024

"""


#La libreria pathlib toma la carpeta 
from pathlib import Path

script_location = Path(__file__).absolute().parent

#Lectura de primer código malicioso
file_location = script_location / "mcode1.txt"
file = file_location.open()
mcode1 = file.readline()

#Lectura de segundo código malicioso
file_location = script_location / "mcode2.txt"
file = file_location.open()
mcode2 = file.readline()

#Lectura de tercer código malicioso
file_location = script_location / "mcode3.txt"
file = file_location.open()
mcode3 = file.readline()

#Lectura de primera transmisión
file_location = script_location / "transmission1.txt"
file = file_location.open()
transmission1 = ""

for line in file.readlines():
    transmission1 += line.strip("\n")

#Lectura de segunda transmisión
file_location = script_location / "transmission2.txt"
file = file_location.open()
transmission2 = ""

for line in file.readlines():
    transmission2 += line.strip("\n")


'''
Algoritmo Z

Recibe un string concatenado con el patron que se tiene que buscar, un caracter especial que no se repita en el texto
y un arreglo Z donde se guardaran las coinsidencias encontradas del patron dentro del texto

Regresa ese mismo arreglo Z ya con todas las coincidencias encontradas
'''
def AlgoritmoZ(txt, Z):
    left = right = 0

    for i in range(len(txt)):
        if i > right:
            # Se inicializan los valores donde empezara  a buscar considencias
            left = right = i

            # Se amplia los valores a buscar dentro del texto
            while right < len(txt) and txt[right - left] == txt[right]:
                right += 1

            # Se coloca un valor en la matriz Z correspondiente a las considencias encontradas
            Z[i] = right - left
            right -= 1 
            
        else:
            k = i - left

            # Se coloca un valor en la matriz Z correspondiente a las considencias encontradas
            if Z[k] < right - i + 1:
                Z[i] = Z[k]

            else:
                left = i

                # Se amplia los valores a buscar dentro del texto
                while right < len(txt) and txt[right - left] == txt[right]:
                    right += 1

                # Se coloca un valor en la matriz Z correspondiente a las considencias encontradas
                Z[i] = right - left
                right -= 1
    
"""
Funcion auxiliar Search algoritmo Z

Recibe la transmision y el patron a buscar
Devuelve en donde se encontro el patron o si no se encontro nada
"""
def search(trans, mcode):
    print("\nBuscando Archivo")
    
    # Se realiza la concatenación del patron a buscar y el texto donde se va a buscar
    conca = mcode + "$" + trans
    
    # Se crea el arreglo Z vacio que guardara el numero de considencias que se encuentre en el texto
    Z = [0] * len(conca)
    
    # Se ejecuta la funcion de Algoritmo Z
    AlgoritmoZ(conca, Z)
    found = False
    
    # Esta parte solo imprime si se encontro el patron y en que parte 
    for i in range(len(conca)):
        if Z[i] == len(mcode):
            print(f"Patron encontrado en el indice:{i - len(mcode) - 1}")
            found = True

    if not found:
        print(f"Patrón no encontrado")

"""
Algoritmo de Manacher
Recibe el texto de una transmisión y busca en esta el palíndromo más largo
Esto lo hace al ir avanzando de caracter en caracter y buscando un palíndromo centrado en ese caracter
al comparar los caracteres a ambos lados y expandiendo el rango de búsqueda mientras haya coincidencias
y almacenando en el arreglo palArray.
Al encontrar un palíndromo aprovecha la propiedad simétrica de un palíndromo para utilizar los valores
ya calculados para obtener los valores de caracteres dentro del palíndromo
"""
def Manacher(txt):
    n = len(txt)
    n = 2 * n + 1
    txt += " "

    palArray = [None] * n
    palArray[0] = 0
    palArray[1] = 1

    middle = 1
    middleRightPos = 2
    iMirror = 0
    sizePal = 0
    maxPivo = 0
    difference = -1
    res = -1
    end = -1

    for i in range(2, n):
        iMirror = 2 * middle - i
        palArray[i] = 0
        difference = middleRightPos - i
        if (difference > 0):
            min = palArray[iMirror]
            if (difference < palArray[iMirror]):
                min = difference
                palArray[i] = min

        while (((i + palArray[i]) < n and (i - palArray[i]) > 0) and (((i + palArray[i] + 1) % 2 == 0) or
            (txt[int((i + palArray[i] + 1) / 2)] == txt[int((i - palArray[i] - 1) / 2)]))):
            palArray[i] += 1
        
        if (palArray[i] > sizePal):
            sizePal = palArray[i]
            maxPivo = i
        
        if (i + palArray[i] > middleRightPos):
            middle = i
            middleRightPos = i + palArray[i]

    res = (maxPivo - sizePal) / 2
    end = res + sizePal - 1
    return (int(res), int(end))

"""
Longest Common Substring
Recibe dos transmisiones y de estas de busca la substring mas larga de una transmison en la otra,
finalmente si encuentra una substring con una longitud mayor a 1 devuelve la posicion de esta substring
"""
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    max_length = 0
    end_index = 0

    # Crear la tabla dp
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    #Recorre la lista de X, Y
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Si los caracteres coinciden
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:  # Actualizar el máximo si se encuentra una nueva longitud mayor
                    max_length = dp[i][j]
                    end_index = i - 1

    if max_length == 0:
        return (-1, -1)

    start_index = end_index - max_length + 1
    return (start_index, end_index)



# -> -> Parte 1
search(transmission1, mcode1)
search(transmission1, mcode2)
search(transmission1, mcode3)
search(transmission2, mcode1)
search(transmission2, mcode2)
search(transmission2, mcode3)

# -> -> Parte 2
LongPal1 = Manacher(transmission1)
LongPal2 = Manacher(transmission2)

print("Parte 2:")
print(f"Transmisión 1: {LongPal1[0]} {LongPal1[1]}")
print(f"Transmisión 2: {LongPal2[0]} {LongPal2[1]}")

# -> -> Parte 3
result = lcs(transmission1, transmission2)
print("Parte 3:")
print(result)
