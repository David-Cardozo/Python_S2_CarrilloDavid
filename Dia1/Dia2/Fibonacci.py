
n = int(input("Ingrese los n terminos fibonacci que desea imprimir :   "))

a = 0
b = 1

for i in range (n):
    print(f" - {a} - ")
    temp = a
    a = b
    b = temp + b