def conversionBin(numeroIng):
    binario = ""  
    while numeroIng > 1:
        binario = str(numeroIng % 2) + binario  
        numeroIng = numeroIng // 2  
    binario = str(numeroIng) + binario 
    return binario  

def conversionDeci(binario):
    decimal = 0
    base = 0

    while binario > 0:
        residuo = binario % 10
        decimal = decimal + residuo * (2 ** base)
        base = base + 1
        binario = int(binario // 10)

    return decimal

def main():
    eleccion = 1
    numIngresado = int(input("Digite el numero a convertir: "))

    while eleccion >= 1 and eleccion <= 4:
        print("Elija la opcion que desee: ")
        print("1. Convertir a binario")
        print("2. Convertir a decimal")
        print("3. Digitar otro numero")
        print("4. Salir")
        eleccion = int(input())

        if eleccion == 1:
            binario = conversionBin(numIngresado)
            print("\nEl numero en binario es: ", binario, "\n")
        elif eleccion == 2:
            decimal = conversionDeci(numIngresado)
            print("\nEl numero en decimal es: ", decimal, "\n")
        elif eleccion == 3:
            numIngresado = int(input("Digite el nuevo numero a convertir: "))
            print("")
        elif eleccion == 4:
            print("Gracias por usar nuestro programa :D")
            eleccion = 0

main()
