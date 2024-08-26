/*
Equipo 7:
    Juan Eduardo Rosas Cerón - A01710168
    Juan Carlos Calderón García - A01625696
    Pablo Hazael Hurtado Mireles - A01710778

Actividad 1.4. Implementación de la técnica de programación "divide y vencerás" 

Programa que toma valores del usuario y realiza un merge sort sobre ellos
*/

#include <iostream>
#include <vector>

using namespace std;

/*
Función toma el apuntador a un vector, el indice que va a ser el inicio, el indice que va a ser la mitad y el índice que va a ser el final
Es una función que guarda en vectores temporales una copia de los valores en ambas mitades del vector
y sobreescribe sobre el arreglo original los valores en orden
*/
void merge(vector<double>& vec, int start, int mid, int end)
{
    int sizeL = mid - start + 1;
    int sizeR = end - mid;

    vector<double> Left(sizeL), Right(sizeR);

    for (int i = 0; i < sizeL; i++)
        Left[i] = vec[start + i];
    for (int j = 0; j < sizeR; j++)
        Right[j] = vec[mid + 1 + j];

    int i = 0, j = 0;
    int k = start;

    while (i < sizeL && j < sizeR) {
        if (Left[i] >= Right[j]) {
            vec[k] = Left[i];
            i++;
        }
        else {
            vec[k] = Right[j];
            j++;
        }
        k++;
    }

    while (i < sizeL) {
        vec[k] = Left[i];
        i++;
        k++;
    }

    while (j < sizeR) {
        vec[k] = Right[j];
        j++;
        k++;
    }
}

/*
Función toma el apuntador a un vector, el indice que va a ser el inicio y el índice que va a ser el final
Es una función recursiva que va a dividir el vector hasta que solo haya un elemento,
una vez llegue a un solo elemento va a empezar a juntar los veceglos en orden
*/
void mergeSort(vector<double>& vec, int start, int end)
{
    if (start >= end)
        return;

    int mid = start + (end - start) / 2;
    mergeSort(vec, start, mid);
    mergeSort(vec, mid + 1, end);
    merge(vec, start, mid, end);
}

/*
Toma valores del usuario a través de la consola llama la función merge sort sobre ellos y despliega los valores ordenados
*/
int main(){
    double input;
    vector<double> numbers;

    cout << "Ingresa un número: ";
    cin >> input;
    numbers.push_back(input);

    while(input >= 0){
        cout << "Ingresa otro número, (para terminar ingresa -1): ";
        cin >> input;
        if (input >= 0){
            numbers.push_back(input);
        }
    }

    mergeSort(numbers, 0 , numbers.size() - 1);

    cout << "[";
    for (int i = 0; i < numbers.size(); i++){
        cout << numbers[i];

        if (i + 1 != numbers.size()){
            cout << ", ";
        }
    }
    cout << "]" <<endl;

    return 0;
}