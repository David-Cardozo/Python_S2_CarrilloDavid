
numIngresado=int(input("Ingrese el numero que quiere verificar:   "))
divisores = 0
for i in range(1, numIngresado):
    i += 1
    residuo = numIngresado % i

    if (residuo == 0):
        divisores += 1

if (divisores > 2):
        print(f"El numero {numIngresado} no es primo")
elif (divisores <=2):
        print(f"El numero {numIngresado} si es primo")