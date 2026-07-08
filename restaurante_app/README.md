# Sistema de Restaurante

## Nombre del estudiante

** Cristopher Alexander Narváez Romero** 
---

## Descripción del sistema

Este proyecto corresponde al desarrollo de un sistema básico de gestión de restaurante utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite registrar, listar y buscar productos y clientes mediante un menú interactivo ejecutado desde la consola.

El proyecto fue desarrollado siguiendo una arquitectura modular, separando las clases del modelo, los servicios y el archivo principal.

---

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md
```

---

## Clase Producto

La clase **Producto** fue implementada utilizando el constructor tradicional `__init__()`, el cual permite crear objetos con los siguientes atributos:

- Nombre
- Categoría
- Precio
- Disponibilidad

Además, se aplicó encapsulación mediante atributos privados.

---

## Uso de @property y @setter

La clase **Producto** utiliza los decoradores `@property` y `@setter` para controlar el acceso y modificación de los atributos.

Se implementaron las siguientes validaciones:

- El nombre no puede estar vacío.
- La categoría no puede estar vacía.
- El precio debe ser mayor que cero.

Estas validaciones ayudan a mantener la integridad de la información registrada.

---

## Clase Cliente

La clase **Cliente** fue implementada utilizando el decorador `@dataclass`, lo que permite simplificar la creación de objetos y reducir la cantidad de código necesario para definir sus atributos.

Los datos almacenados son:

- ID del cliente
- Nombre
- Correo electrónico

---

## Clase Restaurante

La clase **Restaurante** actúa como una clase de servicio encargada de administrar la información del sistema.

Entre sus funciones principales se encuentran:

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar clientes.
- Listar clientes.
- Buscar clientes.

Toda la información se almacena en listas durante la ejecución del programa.

---

## Menú interactivo

El sistema presenta un menú interactivo que permite al usuario seleccionar diferentes opciones mediante la consola.

Las opciones disponibles son:

1. Registrar producto
2. Listar productos
3. Buscar producto
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
7. Salir del sistema

Los objetos se crean dinámicamente utilizando la función `input()` para solicitar la información al usuario.

---

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Visual Studio Code
- Git
- GitHub

---

## Reflexión

Durante el desarrollo de este proyecto fue posible comprender la importancia de la Programación Orientada a Objetos para organizar mejor el código mediante clases y objetos. Además, el uso de constructores, propiedades, setters y el decorador `@dataclass` permitió crear un sistema más seguro, organizado y fácil de mantener. La creación de objetos a partir de datos ingresados por el usuario hace que el programa sea más dinámico y cercano a una aplicación real.

---

## Autor

**Cristopher Alexander Narvaez Romero** 