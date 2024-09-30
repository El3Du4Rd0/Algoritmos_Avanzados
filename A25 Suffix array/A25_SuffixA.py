
#Entrada y preparar entrada
string = str(input("Ingresa una palabra para generar el arreglo de sufijos: "))
string += "!"

#Generar arreglo de sufijos (sufijo, indice) O(n)
SA = []
for i in range(len(string)):
    SA.append((string[i:], i))

#Quicksort para ordenar arreglo O(n log n)
def sort(array):
    if array or len(array) > 1:
        mid = int(len(array)/2)
        pivot = array[mid]
        left = [i for i in array if i[0] < pivot[0]]
        right = [i for i in array if i[0] > pivot[0]]
    
        sortedL = sort(left)
        sortedR = sort(right)

        return sortedL + [pivot] + sortedR
    else:
        return array

#Ordenar arreglo
sortedSA = sort(SA)

#Mostrar resultados O(n)
print("Arreglo de sufijos para " + string + ":")
for i in sortedSA:
    print(str(i[1]) + ":\t" + i[0])