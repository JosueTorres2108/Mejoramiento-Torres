import random

def NoRpetir(n):
    lista1 = [0] * n
    for i in range(n):
        lista1[i] = random.randint(1,100)
        for j in range(i):
            while lista1[i] == lista1[j]:
                print("se esta ingresando un numero repetido: ",lista1[i])
                lista1[i] = random.randint(1,100)
    print(lista1)

n = int(input("Ingrese el numero de elementos que quiera para la lista: "))
Resultado = NoRpetir(n)

