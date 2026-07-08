from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")

def registrar_producto(restaurante):
    print("\n--- Registrar producto ---")

    nombre = input("Nombre: ")
    isbn = input("ISBN :")
    precio = float(input("Precio: "))
    disponible = input("¿Disponible? (s/n): ").lower() == "s"

    producto = Producto(nombre, isbn, precio, disponible)

    restaurante.registrar_producto(producto)

    print("\nProducto registrado correctamente.")


def listar_productos(restaurante):
    print("\n--- Lista de productos ---")

    productos = restaurante.listar_productos()

    if productos:
        for producto in productos:
            print(producto.mostrar_informacion())
    else:
        print("No existen productos registrados.")


def buscar_producto(restaurante):
    print("\n--- Buscar producto ---")

    nombre = input("Ingrese el nombre del producto: ")

    producto = restaurante.buscar_producto(nombre)

    if producto:
        print("\nProducto encontrado:")
        print(producto.mostrar_informacion())
    else:
        print("\nNo se encontró el producto.")


def registrar_cliente(restaurante):
    print("\n--- Registrar cliente ---")

    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")
    id_cliente = int(input("ID del cliente: "))

    cliente = Cliente(id_cliente, nombre, correo)

    restaurante.registrar_cliente(cliente)

    print("\nCliente registrado correctamente.")


def listar_clientes(restaurante):
    print("\n--- Lista de clientes ---")

    clientes = restaurante.listar_clientes()

    if clientes:
        for cliente in clientes:
            print(cliente.mostrar_informacion())
    else:
        print("No existen clientes registrados.")


def buscar_cliente(restaurante):
    print("\n--- Buscar cliente ---")

    nombre = input("Ingrese el nombre del cliente: ")

    cliente = restaurante.buscar_cliente(nombre)

    if cliente:
        print("\nCliente encontrado:")
        print(cliente.mostrar_informacion())
    else:
        print("\nNo se encontró el cliente.")


def main():
    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            buscar_producto(restaurante)

        elif opcion == "4":
            registrar_cliente(restaurante)

        elif opcion == "5":
            listar_clientes(restaurante)

        elif opcion == "6":
            buscar_cliente(restaurante)

        elif opcion == "7":
            print("\nGracias por utilizar el sistema Restaurante.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()