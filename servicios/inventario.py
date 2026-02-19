import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # -------------------------------
    # Manejo de archivos
    # -------------------------------
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                # Si no existe, se crea vacío
                with open(self.archivo, "w") as f:
                    pass
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_producto, nombre, cantidad, precio = datos
                        try:
                            producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                            self.productos.append(producto)
                        except ValueError:
                            print(f"Advertencia: línea corrupta en archivo -> {linea.strip()}")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al cargar inventario: {e}")

    def guardar_en_archivo(self):
        """Guarda todos los productos en el archivo."""
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al guardar inventario: {e}")

    # -------------------------------
    # Operaciones sobre el inventario
    # -------------------------------
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe en el inventario.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado correctamente y guardado en archivo.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado y archivo actualizado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nombre is not None:
                    p.set_nombre(nombre)
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado y archivo sincronizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for r in resultados:
                print(r)
        else:
            print("No se encontraron coincidencias.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)