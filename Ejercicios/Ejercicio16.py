import random
def inicio():
    opcion = int(input('Escriba una opcion para comenzar con el programa: '))
    menu(opcion)

def menu(opcion):
    print("opcion=",opcion)
    if (opcion == 1):
        ImprimirLista(Listar)
        inicio()
    elif(opcion == 2):
        sumalist = sumar(Listar)
        print("La suma de los elementos de la lista es: ",sumalist) 
        inicio()
    elif(opcion == 3):
        sumalist = sumar(Listar)
        promediolista = promedio(sumalist,n)
        print("el promedio de Lista es: ",promediolista)
        inicio()
    elif(opcion == 4):
        menor(Listar)
        inicio()
    elif(opcion == 5):
        mayor(Listar)
        inicio()
    elif(opcion == 6):
        Ascedente(Listar)
        inicio()
    elif(opcion == 7):
        Descedente(Listar)
        inicio()
    elif(opcion == 8):
        Moda(Listar)
        inicio()
    elif(opcion == 9):
        Mediana(Ascedente(Listar))
        inicio()
    elif(opcion == 10):
        buscar(Listar)
        inicio()

    elif(opcion == 11):
        print("vemos lokas")
        quit()

def llenarLista(elementos):
    lista = [0]  * elementos
    for i in range(n):
       lista[i] = random.randint(1,100)
    return lista

def ImprimirLista(lista1):
    print(lista1)

def sumar(lista2):
    sumal= 0
    for i in lista2:
        sumal = sumal + i
    return sumal

def promedio(suma,n):
    prom = suma/n
    return prom
         
def menor(lista3):
    menor = lista3[0]
    for i in lista3:
        if i < menor:
            menor = i
    print("El numero menor es", menor)
         

def mayor(lista4):
    mayor = lista4[0]
    for i in lista4:
        if i > mayor:
            mayor = i
    print("El numero mayor es", mayor)

def Ascedente(lista5):
    for i in range(n):
        for j in range(i+1,n):
            if lista5[i]>lista5[j]:
                aux=lista5[i]
                lista5[i]=lista5[j]
                lista5[j]=aux
    print(lista5)

def Descedente(lista6):
    for i in range(n):
        for j in range(i+1,n):
            if lista6[i]<lista6[j]:
                aux=lista6[i]
                lista6[i]=lista6[j]
                lista6[j]=aux
    print(lista6)

def Moda(lista7):
    cuenta = 0
    mayor = 0
    for i in range(n):
        cuenta = 0
        for j in range(n):
            if lista7[i] == lista7[j]:
                cuenta = cuenta + 1 
        if (cuenta > mayor):
            mayor = cuenta
            moda = lista7[i]
    print("la moda es: ",moda," y se reptite: ",mayor," veces")

def Mediana(lista8):
    # Obtener longitud
    longitud = n
    mitad = int(longitud / 2)
    # Si la longitud es par, promediar elementos centrales
    if longitud % 2 == 0:
        me = mitad - 1
        mediana = (lista8[me]+lista8[mitad]) / 2
    else:
        # Si no, es la del centro
        med = mitad+1
        mediana = lista8[med]
    print(mediana)

def buscar(lista9):
    num = int(input('Escriba el numero que quiere buscar: '))
    for i in range(n):
        if num == lista9[i]:
            print("el numero se ecuentra en la posicion ",i)

    

listar = []
n = int(input("Ingresa el numero de elementos de la lista: "))
Listar = llenarLista(n)
#menu
menul = """
1. imprimir Lista.
2. Sumar Lista. 
3. Promedio
4. Menor
5. Mayor
6. Ascendente
7. Descendente
8. Moda
9. Mediana 
10. Buscar
11. Terminar programa
"""
print(menul)
inicio()




