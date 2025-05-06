def eleccionSi(ingrediente, sub, valor1, valor2):
    if ingrediente == 1:
        return sub + valor1
    else:
        return sub + valor2

def eleccionSegun(ingrediente, sub, valor1, valor2, valor3):
    if ingrediente == 1:
        return sub + valor1
    elif ingrediente == 2:
        return sub + valor2
    elif ingrediente == 3:
        return sub + valor3

def valorServicio(sub, porcentaje):
    return sub * porcentaje

def valorTotal(sub, servicio):
    return sub + servicio

def restaurante():
    total = 0
    subtotal = 0
    servicio = 0

    N = int(input("Digite el número de hamburguesas a pedir: "))

    for i in range(1, N + 1):
        print(f"\nIngredientes para la hamburguesa No. {i}\n")

        subtotal = 0  # Reiniciar subtotal por hamburguesa

        while True:
            print("Seleccione el tipo de pan:")
            print("1. Centeno - $1000")
            print("2. Avena - $1500")
            pan = int(input("Opción: "))
            if pan == 1 or pan == 2:
                subtotal = eleccionSi(pan, subtotal, 1000, 1500)
                break

        while True:
            print("Seleccione el tipo de carne:")
            print("1. 250G - $5000")
            print("2. 300G - $7500")
            carne = int(input("Opción: "))
            if carne == 1 or carne == 2:
                subtotal = eleccionSi(carne, subtotal, 5000, 7500)
                break

        while True:
            print("Seleccione el tipo de pollo:")
            print("1. 250G - $4500")
            print("2. 350G - $5500")
            pollo = int(input("Opción: "))
            if pollo == 1 or pollo == 2:
                subtotal = eleccionSi(pollo, subtotal, 4500, 5500)
                break

        while True:
            print("Seleccione el tipo de pollo desmechado:")
            print("1. 250G - $6500")
            print("2. 350G - $7500")
            polloDes = int(input("Opción: "))
            if polloDes == 1 or polloDes == 2:
                subtotal = eleccionSi(polloDes, subtotal, 6500, 7500)
                break

        while True:
            print("Seleccione el tipo de tocineta:")
            print("1. 1 Lonja - $1500")
            print("2. 2 Lonjas - $2500")
            tocineta = int(input("Opción: "))
            if tocineta == 1 or tocineta == 2:
                subtotal = eleccionSi(tocineta, subtotal, 1500, 2500)
                break

        while True:
            print("Seleccione el tipo de papa frita:")
            print("1. A la francesa - $5000")
            print("2. En cascos - $6000")
            papaFrita = int(input("Opción: "))
            if papaFrita == 1 or papaFrita == 2:
                subtotal = eleccionSi(papaFrita, subtotal, 5000, 6000)
                break

        while True:
            print("Seleccione el tipo de bebida:")
            print("1. Gaseosa - $5000")
            print("2. Club Colombia - $8000")
            print("3. Naranjada - $9000")
            bebida = int(input("Opción: "))
            if bebida in [1, 2, 3]:
                subtotal = eleccionSegun(bebida, subtotal, 5000, 8000, 9000)
                break

    servicio = valorServicio(subtotal, 0.1)
    total = valorTotal(subtotal, servicio)

    print(f"\nEl valor del subtotal es de: ${subtotal}")
    print(f"El valor del servicio es de: ${servicio}")
    print(f"El valor total es de: ${total}")

restaurante()
