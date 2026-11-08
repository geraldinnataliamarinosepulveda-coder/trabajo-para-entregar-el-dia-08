matVentas = []

# Ingresar los datos de ventas
for f in range(5):
    fila = []
    for c in range(7):
        venta = int(input(f"Ingrese ventas del producto {f+1}, dia {c+1}: "))
        fila.append(venta)
    matVentas.append(fila)

# Ingresar precios de los productos
lstPrecios = []

for f in range(5):
    precio = int(input(f"Ingrese el precio del producto {f+1}: "))
    lstPrecios.append(precio)


def lstTotalesProdSem(Ventas, Precios):
    filas = len(Ventas)
    cols = len(Ventas[0])
    lstTotales = []

    for f in range(filas):
        suma = 0
        for c in range(cols):
            suma += Ventas[f][c] * Precios[f]

        lstTotales.append(suma)

    return lstTotales


# Calcular ingresos por producto
lstTotales = lstTotalesProdSem(matVentas, lstPrecios)

# Producto con mayores ingresos
maxTotal = max(lstTotales)
ProdVentMax = lstTotales.index(maxTotal) + 1

print(f"El producto {ProdVentMax} es el que genera más ingresos en la semana, con ${maxTotal:,}")


# Calcular ingresos por cada día
lstTotalesDias = []

for c in range(7):
    suma = 0
    for f in range(5):
        suma += matVentas[f][c] * lstPrecios[f]

    lstTotalesDias.append(suma)


# Día con mayores ingresos
dias = ["Lunes", "Martes", "Miércoles", "Jueves",
        "Viernes", "Sábado", "Domingo"]

maxDia = max(lstTotalesDias)
diaMayor = lstTotalesDias.index(maxDia)

print(f"El día con mayores ingresos es {dias[diaMayor]}, con ${maxDia:,}")