def Exponente(base,exponente1):
    resultado = base
    for i in range(1,exponente1):
        resultado = resultado * base
    
    return resultado

n1 = int(input("Ingresa el base número: "))
n2 = int(input("Ingresa el exponente número: "))

resultado = (Exponente(n1,n2))
print(resultado)
