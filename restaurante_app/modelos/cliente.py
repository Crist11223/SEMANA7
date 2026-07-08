from dataclasses import dataclass

@dataclass
class Cliente:
   
    nombre: str
    correo: str
    id_cliente: int

    def mostrar_informacion(self) -> str:
        return (
            f"ID: {self.id_cliente} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )
       

    

    
          

   


    