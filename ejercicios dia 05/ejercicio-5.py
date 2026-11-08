resultados = input("Ingrese una cadena:")
resultado = []

for caracter in s:
    if resultado and resultado[-1] == caracter:
        resultado.pop()
    else:
        resultado.append(caracter)

resultado = "".join(resultado)
print(resultado if resultado else "Empty String")

