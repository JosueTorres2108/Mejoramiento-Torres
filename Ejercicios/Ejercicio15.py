def SolicitarImprimir(num):
    for i in range(num, 0, -1):
        for j in range(1, i+1):  
            print(j, end=' ')
        print()

n1 = int(input("Ingresa un numero: "))
resultado = SolicitarImprimir(n1)
