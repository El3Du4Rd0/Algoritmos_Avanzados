#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int main()
{
    cout << "\nEjemplo" << endl;
    // char txt[]= "anitalavalatina";
    // char txt[]= "9102019";
    char txt[] = "70616e206465206e6172716e6a6150616e206465206e6172616e6a61";
    int N = strlen(txt);
    N = 2 * N + 1;
    int palArray[N];
    palArray[0] = 0;
    palArray[1] = 1;
    int middle = 1;
    int middleRightPos = 2;
    int iMirror;
    int sizePal = 0;
    int maxPivo = 0;
    int difference = -1;
    int res = -1;
    int end = -1;
    // int min;
    for (int i = 2; i < N; i++)
    {
        iMirror = 2 * middle - i;
        palArray[i] = 0;
        difference = middleRightPos - i;
        if (difference > 0)
        {
            int min = palArray[iMirror];
            if (difference < palArray[iMirror])
            {
                min = difference;
                palArray[i] = min;
            }
        }

        while (((i + palArray[i]) < N && (i - palArray[i]) > 0) &&
               (((i + palArray[i] + 1) % 2 == 0) ||
                (txt[(i + palArray[i] + 1) / 2] ==
                 txt[(i - palArray[i] - 1) / 2])))
        {
            palArray[i]++;
        }
        if (palArray[i] > sizePal)
        {
            sizePal = palArray[i];
            maxPivo = i;
        }
        if (i + palArray[i] > middleRightPos)
        {
            middle = i;
            middleRightPos = i + palArray[i];
        }
    }
    res = (maxPivo - sizePal) / 2;
    end = res + sizePal - 1;
    
    for (int i = 0; i < N; i++) 
        cout << palArray[i] << ", ";

    cout << endl << res << " " << end << endl;
}