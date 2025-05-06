def sueldoBruto(numeroHoras, valorHora):
    return numeroHoras * valorHora

def sueldoNeto(sueldoB, descuento1, descuento2):
    return sueldoB - descuento1 - descuento2

def descuentos(sueldoB, porcentaje):
    return sueldoB * porcentaje

def totales(total, valorTotal):
    return total + valorTotal

def promedios(total, n):
    return total / n

def nomina():
    nombre = ""
    nMayor = ""
    nMenor = ""
    totalBruto = 0
    totalEps = 0
    totalNeto = 0
    totalPension = 0
    maxNeto = 0
    minNeto = 0

    N = int(input("Digite el número de empleados a hacer la nómina: "))

    for i in range(1, N + 1):
        print(f"No. de empleado: {i}")
        nombre = input("Ingrese el nombre del empleado: ")
        horasTrabajadas = float(input("Digite las horas trabajadas: "))

        sueldoBrutoEmpleado = sueldoBruto(horasTrabajadas, 20000)
        print(f"El sueldo bruto del empleado {nombre} es de: {sueldoBrutoEmpleado}")

        eps = descuentos(sueldoBrutoEmpleado, 0.04)
        print(f"El descuento de EPS es de: {eps}")

        pension = descuentos(sueldoBrutoEmpleado, 0.04)
        print(f"El descuento de pensión es de: {pension}")

        sueldoNetoEmpleado = sueldoNeto(sueldoBrutoEmpleado, pension, eps)
        print(f"El sueldo neto del empleado es de: {sueldoNetoEmpleado}\n")

        totalBruto = totales(totalBruto, sueldoBrutoEmpleado)
        totalEps = totales(totalEps, eps)
        totalNeto = totales(totalNeto, sueldoNetoEmpleado)
        totalPension = totales(totalPension, pension)

        if sueldoNetoEmpleado > maxNeto:
            minNeto = maxNeto
            nMenor = nMayor
            maxNeto = sueldoNetoEmpleado
            nMayor = nombre
        elif sueldoNetoEmpleado < minNeto or minNeto == 0:
            minNeto = sueldoNetoEmpleado
            nMenor = nombre

    promBruto = promedios(totalBruto, N)
    promNeto = promedios(totalNeto, N)

    print("\nTotales de las nóminas:")
    print(f"Sueldos brutos: {totalBruto}")
    print(f"EPS: {totalEps}")
    print(f"Pensión: {totalPension}")
    print(f"Sueldos netos: {totalNeto}\n")

    print("Promedios de los sueldos:")
    print(f"Sueldo bruto promedio: ${promBruto}")
    print(f"Sueldo neto promedio: ${promNeto}\n")

    print(f"El empleado {nMayor} tiene el sueldo más alto, siendo este de: {maxNeto}")
    print(f"El empleado {nMenor} tiene el sueldo más bajo, siendo este de: {minNeto}")

nomina()
