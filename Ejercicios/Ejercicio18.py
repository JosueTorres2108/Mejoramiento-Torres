def fibonacci(n):
    listaf =[1]*n
    i = 2
    while (i<n):
        listaf[i] = listaf[i-1] + listaf[i-2]
        i+=1
    return(listaf)
n = int(input("Ingresa el numero de elementos de la serie: "))
print(fibonacci(n))
