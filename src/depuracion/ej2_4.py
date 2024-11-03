"""

Algoritmo burbuja
Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y entiendes su funcionamiento

"""

a = [8, 3, 1, 19, 14]

n = len(a)


for i in range(n):
    
    for j in range (0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print (a)
