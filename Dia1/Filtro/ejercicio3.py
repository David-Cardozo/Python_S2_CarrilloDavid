def operacionS(num1, num2):
    return num1 + num2

def operacionR(num1, num2):
    return num1 - num2

def operacionM(num1, num2):
    return num1 * num2

def operacionD(num1, num2):
    return num1 / num2

def main():
    primerNum = float(input("Digite el primer número: "))
    segundoNum = float(input("Digite el segundo número: "))

    print("Elija la operación deseada según:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    eleccion = int(input("Opción: "))

    if eleccion == 1:
        suma = operacionS(primerNum, segundoNum)
        print("La suma de los números es:", suma)
    elif eleccion == 2:
        resta = operacionR(primerNum, segundoNum)
        print("La resta de los números es:", resta)
    elif eleccion == 3:
        multiplicacion = operacionM(primerNum, segundoNum)
        print("La multiplicación de los números es:", multiplicacion)
    elif eleccion == 4:
        if segundoNum != 0:
            division = operacionD(primerNum, segundoNum)
            print("La división de los números es:", division)
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Opción no válida.")
main()
