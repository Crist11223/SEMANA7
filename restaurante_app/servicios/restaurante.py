from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.cliente = []
        self.producto = []

def agregar_producto(self, producto : Producto):
    self.producto.append(producto)

def listar_producto(self):
    
        return self.producto

def buscar_producto(self, nombre: str):
        
        for producto in self.productos:

            if producto.nombre.lower() == nombre.lower():
                return producto

        return None

def agregar_usuario(self, cliente: Cliente):
       

        self.usuarios.append(cliente)

def listar_cliente(self):
        

        return self.cliente
        
def buscar_cliente(self, id_cliente: int):
        

        for cliente in self.cliente:

            if cliente.id_usuario == id_cliente:
                return cliente

        return None
    

    