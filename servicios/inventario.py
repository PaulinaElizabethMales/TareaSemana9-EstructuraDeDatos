from modelos.producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Validar ID único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe en el inventario.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
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
                print("Producto actualizado.")
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