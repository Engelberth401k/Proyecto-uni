from vendedor import menu_vendedor
from comprador import menu_comprador
from inventario import cargar_productos


# Cuentas predeterminadas
vendedores = {
    "vendedor1": "1234",
    "vendedor2": "5678",
    "vendedor3": "abcd"
}

compradores = {
    "comprador1": "1111",
    "comprador2": "2222",
    "comprador3": "3333"
}

# Cargar inventario
productos = cargar_productos()


# Seleccionar usuario
print("=== SISTEMA DE VENTAS ===")
print("1. Ingresar como vendedor")
print("2. Ingresar como comprador")

opcion = input("Seleccione una opcion: ")

if opcion == "1":
    cuentas = vendedores
    tipo = "vendedor"

elif opcion == "2":
    cuentas = compradores
    tipo = "comprador"

else:
    print("Opcion incorrecta.")
    exit()


# Inicio de sesion
print("\n=== INICIO DE SESION ===")

usuario = input("Nombre de usuario: ")
contrasena = input("Contrasena: ")


# Verificar credenciales
if usuario in cuentas and cuentas[usuario] == contrasena:

    print("\nInicio de sesion exitoso.")
    print("Bienvenido:", usuario)

    if tipo == "vendedor":
        menu_vendedor(productos)

    else:
        menu_comprador(productos)

else:
    print("\nUsuario o contrasena incorrectos.")