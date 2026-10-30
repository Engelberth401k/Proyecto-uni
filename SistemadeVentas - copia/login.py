
from vendedor import menu_vendedor
from comprador import menu_comprador

# Cuentas predeterminadas, las cuentas usa el formato nombre : contraseña
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

# Inventario compartido entre el comprador y el vendedor
productos = [
    {"nombre": "Arroz", "precio": 25},
    {"nombre": "Leche", "precio": 40},
    {"nombre": "Pan", "precio": 15},
    {"nombre": "Aceite", "precio": 65}
]

# Seleccionar el tipo de usuario que ingresara
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
    print("Opcion no valida.")
    exit()

# Inicio de sesion
print("\n=== INICIO DE SESION ===")

usuario = input("Nombre de usuario: ")
contrasena = input("Contrasena: ")

# Verificar si la informacion es correcta
if usuario in cuentas and cuentas[usuario] == contrasena:

    print("\nInicio de sesion exitoso.")
    print("Bienvenido:", usuario)

    if tipo == "vendedor":
        menu_vendedor(productos)

    else:
        menu_comprador(productos)

else:
    print("\nUsuario o contrasena incorrectos.")