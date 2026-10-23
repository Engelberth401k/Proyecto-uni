# Esto se abre desde el archivo login.py, corre el codigo desde ahi

def menu_vendedor(productos):
    while True:
        print("\n=== MENU VENDEDOR ===")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Editar producto")
        print("4. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))

            productos.append({
                "nombre": nombre,
                "precio": precio
            })

            print("Producto agregado.")

        elif opcion == "2":
            for i, p in enumerate(productos, 1):
                print(i, p["nombre"], "- C$", p["precio"])

        elif opcion == "3":
            for i, p in enumerate(productos, 1):
                print(i, p["nombre"], "- C$", p["precio"])

            numero = int(input("Numero a editar: ")) - 1

            if 0 <= numero < len(productos):
                productos[numero]["nombre"] = input("Nuevo nombre: ")
                productos[numero]["precio"] = float(input("Nuevo precio: "))
                print("Producto editado.")
            else:
                print("Numero incorrecto.")

        elif opcion == "4":
            break

        else:
            print("Opcion incorrecta.")