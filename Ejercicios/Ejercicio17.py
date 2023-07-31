import random
def llenarLista1(elementos):
    lista1 = [0] * elementos
    for i in range(n):
        lista1[i] = random.randint(1,100)
    return lista1

def llenarLista2(elementos):
    lista2 = [0] * elementos
    for i in range(n):
        lista2[i] = random.randint(1,100)
    return lista2

def CompararSuma(lista1,lista2):
    suma1= 0
    for i in lista1:
        suma1 = suma1 + i

    suma2= 0
    for i in lista2:
        suma2 = suma2 + i

    print("Suma de la lista 1: ",suma1)
    print("Suma de las lista 2: ",suma2)

    if suma1 > suma2:
        print("La suma de la lista 1 es mayor que la suma de la lista 2")
    elif suma1 < suma2:
        print("La suma de la lista 2 es mayor que la suma de la lista 1")
    else:
        print("Ambas sumas de las listas son iguales")

def CompararMayor(lista1,lista2):
    mayor1 = lista1[0]
    for i in lista1:
        if i > mayor1:
            mayor1 = i
    print("El numero mayor de la lista 1 es: ", mayor1)

    mayor2 = lista2[0]
    for i in lista2:
        if i > mayor2:
            mayor2 = i
    print("El numero mayor de la lista 2 es: ", mayor2)

    if mayor1 > mayor2:
        print("El numero mayor de la lista 1 es mayor que el de la lista 2")
    elif mayor1 < mayor2:
        print("El numero mayor de la lista 2 es mayor que el de la lista 1")
    else: 
        print("Ambos numeros de las listas tiene el mismo valor")
    
def Promedio(lista1, lista2):
    suma1= 0
    for i in lista1:
        suma1 = suma1 + i

    suma2= 0
    for i in lista2:
        suma2 = suma2 + i

    promedio = (suma1 + suma2) /2


    print("El promedio de las sumas de las listas es: ", promedio)
    return promedio

def CompararPromedios(lista1,lista2,elementos,promediocon):
    suma1= 0
    for i in lista1:
        suma1 = suma1 + i
    suma2= 0
    for i in lista2:
        suma2 = suma2 + i
    
    promedio1 = suma1 / elementos
    promedio2 = suma2 / elementos

    print("El promedio de la lista 1 es: ",promedio1)
    print("El promedio de la lista 2 es: ",promedio2)
    if promedio1 > promediocon:
        print("El promedio de la lista 1 esta por encima del promedio en conjunto")
    else:
        promedio1 < promediocon
        print("El promedio de la lista 1 esta por abajo del promedio en conjunto")
    if promedio2 > promediocon:
        print("El promedio de la lista 2 esta por encima del promedio en conjunto")
    else: 
        promedio2 < promediocon
        print("El promedio de la lista 2 esta por abajo del promedio en conjunto")

def pares(lista1,lista2,elementos):
    pares1 = 0
    for i in range (elementos):
        if lista1[i] % 2 == 0:
            pares1 += 1

    pares2 = 0
    for i in range (elementos):
        if lista2[i] % 2 == 0:
            pares2 += 1

    print("La lista 1 tiene ", pares1,"pares")
    print("La lista 2 tiene ", pares2, "pares")
    if pares1 > pares2:
        print("La lista 1 tiene mas pares que la lista 2")
    elif pares1 < pares2:
        print("La lista 2 tiene mas pares que la lista 1")
    else:
        print("Ambas listas tienen la misma cantidad de pares")

def impares(lista1,lista2,elementos):
    impar1 = 0
    for i in range (elementos):
        if lista1[i] % 2 != 0:
            impar1 += 1

    impar2 = 0
    for i in range (elementos):
        if lista2[i] % 2 != 0:
            impar2 += 1

    print("La lista 1 tiene ", impar1,"impares")
    print("La lista 2 tiene ", impar2, "impares")
    if impar1 > impar2:
        print("La lista 1 tiene mas impares que la lista 2")
    elif impar1 < impar2:
        print("La lista 2 tiene mas impares que la lista 1")
    else:
        print("Ambas listas tienen la misma cantidad de impares")

n = int(input("Ingresa el numero de elementos de la lista: "))
Listar1 = llenarLista1(n)
Listar2 = llenarLista2(n)
print("lista random 1: ",Listar1)
print("Lista random 2:",Listar2)
CompararSuma(Listar1,Listar2)
CompararMayor(Listar1,Listar2)
promedioc = Promedio(Listar1,Listar2)
CompararPromedios(Listar1,Listar2,n,promedioc)
pares(Listar1,Listar2,n)
impares(Listar1,Listar2,n)
