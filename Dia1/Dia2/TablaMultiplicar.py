
numTabla = int(input("Ingrese el numero del cual quiere saber la tabla de multiplicar :   "))
numLimite = int(input("Ingrese hasta donde quiere la tabla de multiplicar :   "))

for i in range (0,numLimite + 1):
    multiplicacion = numTabla * i
    print(f" {numTabla}  x  {i}  =  {multiplicacion}") 