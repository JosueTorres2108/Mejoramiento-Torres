def ContarPositivos():
    contador = 0
    num = int(input("Ingresa el número: "))
    if num > 0: 
        contador += 1
    while num >= 1:
        contador += 1
        num = int(input("Ingresa el número: "))
        if num < 0:
            break 
    return (contador-1)

print("el maximo de numeros positivos es ",ContarPositivos())
