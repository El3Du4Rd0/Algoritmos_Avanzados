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

# Algoritmo Z
def AlgoritmoZ(txt, Z):
    left = right = 0

    for i in range(len(txt)):
        if i > right:
            left = right = i
            
            while right < len(txt) and txt[right - left] == txt[right]:
                right += 1

            Z[i] = right - left
            right -= 1 
        else:
            k = i - left

            if Z[k] < right - i + 1:
                Z[i] = Z[k]

            else:
                left = i

                while right < len(txt) and txt[right - left] == txt[right]:
                    right += 1


                Z[i] = right - left
                right -= 1
    

# search algoritmo Z
def search(trans, mcode):
    print("\nBuscando Archivo")
    conca = mcode + "$" + trans
    Z = [0] * len(conca)
    
    AlgoritmoZ(conca, Z)

    found = False
    for i in range(len(conca)):
        if Z[i] == len(mcode):
            print(f"Patron encontrado en el indice:{i - len(mcode) - 1}")
            found = True

    if not found:
        print(f"Patrón no encontrado")

# Manacher
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

# Longest Common Subsequence
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    max_length = 0
    end_index = 0

    # Crear la tabla dp
    dp = [[0] * (n + 1) for _ in range(m + 1)]

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
print(result)  # Salida: (0, 2) que corresponde a "ace"
