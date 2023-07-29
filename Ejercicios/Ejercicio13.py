def SolicitarNumero(num):
    invertido = 0
    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num //= 10
    return invertido

n1 = int(input("Ingresa un numero de varios caracteres: "))
resultado = SolicitarNumero(n1)
print(resultado)