from servicios.inventario import Inventario
from modelos.producto import Producto

def menu():
    inventario = Inventario()
    # Mostrar inventario cargado al iniciar
    print("\nInventario cargado desde archivo:")
    inventario.mostrar_inventario()

    while True:
        print("-------------------------------------------")
        print("---- Sistema de Gestión de Inventarios ----")
        print("-------------------------------------------")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nombre = input("Nuevo nombre (dejar vacío si no aplica): ")
            cantidad = input("Nueva cantidad (dejar vacío si no aplica): ")
            precio = input("Nuevo precio (dejar vacío si no aplica): ")
            inventario.actualizar_producto(
                id_producto,
                nombre=str(nombre) if nombre else None,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Gracias por usarnos. Vuelve pronto")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
