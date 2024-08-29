def fibonacci_PD (n):
    i = 2
    f = []
    f.append(1)
    if (n > 0): 
        f.append(2)
        for i in range(2,n + 1):
            f.append(((4 * f[i - 1]) + (2 * f[i - 2]))/2)
    return f

print(fibonacci_PD(8))