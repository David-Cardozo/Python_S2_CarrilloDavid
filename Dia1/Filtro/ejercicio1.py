
numIngresado = int(input("Ingrese el número a calcular el factorial: "))
resultado = numIngresado

for i in range(numIngresado - 1, 1, -1):
        resultado *= i

print(f"El factorial de {numIngresado} es: {resultado}")

