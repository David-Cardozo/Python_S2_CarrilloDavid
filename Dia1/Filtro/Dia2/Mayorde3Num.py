num1=int(input("Ingrese el primer numero"))

num2=int(input("Ingrese el segundo numero"))

num3=int(input("Ingrese el tercer numero"))

if (num1 > num2 and num1 > num3):
    print(f"El {num1} es el numero mayor ")
elif ((num2 > num1 and num2 > num3)):
    print(f"El {num2} es el numero mayor ")
elif ((num3 > num1 and num3 > num2)):
    print(f"El {num3} es el numero mayor ")