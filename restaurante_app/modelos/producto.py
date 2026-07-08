class Producto():
    def __init__(self, nombre : str, isbn : str, precio : str, disponible: str):
        self.nombre = nombre
        self.isbn = isbn
        self.precio = precio
        self.disponible = disponible


    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("El título no puede estar vacío.")
        self.__nombre = nuevo_nombre


    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, nuevo_isbn: str):
        if not nuevo_isbn.strip():
            raise ValueError("El isbn no puede estar vacío.")

        self._isbn = nuevo_isbn

    @property
    def precio(self) -> str:
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio: str):
        if not nuevo_precio.strip():
            raise ValueError(" El precio no puede estar vacío.")

        self._precio = nuevo_precio

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, estado: bool):
        self._disponible = estado

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información del libro en formato legible.
        """

        estado = "Disponible" if self.disponible else "Prestado"

def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"ISBN: {self.__isbn}")
        print(f"Precio: {self.__precio}")
        print(f"Disponible: {self.__disponible}")