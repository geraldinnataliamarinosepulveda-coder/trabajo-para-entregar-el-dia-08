# Algoritmo GestionInventario

def gestionar_inventario():
    productos = []

    while True:
        print("===== MENU DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Agregar lote de productos")
        print("3. Eliminar producto del inventario")
        print("4. Eliminar el producto mas reciente")
        print("5. Ordenar productos alfabeticamente")
        print("6. Mostrar numero total de productos")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Opcion no valida")
            continue

        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ").strip()
            productos.append(nombre)
            print("Producto agregado correctamente")
        elif opcion == 2:
            try:
                cantidad = int(input("Cuantos productos desea agregar? "))
                if cantidad < 0:
                    raise ValueError
            except ValueError:
                print("Ingrese una cantidad valida (cero o mayor)")
                continue

            for _ in range(cantidad):
                nombre = input("Ingrese el nombre del producto: ").strip()
                productos.append(nombre)
            print("Lote agregado correctamente")
        elif opcion == 3:
            nombre = input("Ingrese el producto que desea eliminar: ").strip()
            if nombre in productos:
                productos.remove(nombre)
                print("Producto eliminado correctamente")
            else:
                print("El producto no existe")
        elif opcion == 4:
            if productos:
                productos.pop()
                print("Se elimino el producto mas reciente")
            else:
                print("El inventario esta vacio")
        elif opcion == 5:
            productos.sort(key=str.casefold)
            print("Inventario ordenado:")
            for nombre in productos:
                print(nombre)
        elif opcion == 6:
            print(f"Total de productos: {len(productos)}")
        elif opcion == 7:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    gestionar_inventario()