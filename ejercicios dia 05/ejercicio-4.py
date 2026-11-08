def dividir_equipos():
    n = int(input("Ingrese la cantidad de personas: "))
    suma1 = 0
    suma2 = 0

    for i in range(1, n + 1):
        peso = int(input(f"Ingrese el peso de la persona {i}: "))
        if i % 2 == 1:
            suma1 += peso
        else:
            suma2 += peso

    print("Peso total del equipo 1:", suma1)
    print("Peso total del equipo 2:", suma2)


if __name__ == "__main__":
    dividir_equipos()
