# Sistema de Restaurante — Semana 8

**Estudiante:** Joselyn Yomaira Fuentes Rosero  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 8 — Organización modular de un sistema orientado a objetos en Python

---

## Descripción del sistema

Aplicación de consola desarrollada en Python que gestiona productos, bebidas y clientes de un restaurante. El sistema permite registrar y listar cada entidad a través de un menú interactivo. La arquitectura está organizada en módulos con responsabilidades claramente separadas y aplica los principios SRP, OCP y LSP.

---

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

---

## Responsabilidad de cada clase

| Clase / Archivo | Responsabilidad |
|---|---|
| `Producto` | Define los atributos comunes de un producto del restaurante: codigo, nombre, categoria y precio. Valida sus datos en el constructor. |
| `Bebida` | Extiende `Producto` con los atributos `presentacion` y `envase`. Sobreescribe `mostrar_informacion()` para incluirlos. |
| `Cliente` | Almacena la información de un cliente registrado: identificacion, nombre y correo. Valida formato de correo. |
| `Restaurante` | Servicio central que administra las listas de productos y clientes, valida duplicados y expone métodos de consulta. |
| `main.py` | Controla el flujo del programa: muestra el menú, recoge datos del usuario, crea objetos y delega al servicio. |

---

## Relación entre Producto y Bebida

`Bebida` hereda de `Producto` porque una bebida es un tipo de producto dentro del sistema. Esta relación permite almacenar ambos en la misma colección sin listas separadas. Durante el listado, el servicio llama a `mostrar_informacion()` en cada elemento y cada objeto responde con sus propios datos según su implementación, sin que el servicio necesite saber el tipo concreto.

---

## Principios SOLID aplicados

### S — Responsabilidad única (SRP)

Cada clase tiene una sola razón para cambiar. `Producto` y `Bebida` representan entidades del dominio y se encargan de validar sus propios datos. `Restaurante` administra colecciones y verifica duplicados. `main.py` gestiona únicamente la interacción con el usuario. Ninguna clase toma responsabilidades de otra.

### O — Abierto/Cerrado (OCP)

`Bebida` extiende el sistema agregando `presentacion` y `envase` sin modificar `Producto` ni `Restaurante`. Si se quisiera incorporar una nueva especialización, como `Postre`, bastaría con crear la clase correspondiente heredando de `Producto` y el servicio la procesaría sin cambios.

### L — Sustitución de Liskov (LSP)

Un objeto `Bebida` puede ocupar cualquier lugar donde se espera un `Producto`. El servicio recibe `Producto` como tipo en `registrar_producto()` y llama a `mostrar_informacion()` sin condiciones que distingan el tipo concreto. La lista `_productos` almacena instancias de ambas clases y las trata de forma uniforme.

---

## Instrucciones de ejecución

1. Descargar o clonar el repositorio.
2. Desde la carpeta raíz del proyecto ejecutar:

```bash
python restaurante_app/main.py
```

3. Navegar por el menú para registrar o listar productos, bebidas y clientes.

---

## Reflexión

Separar las responsabilidades entre clases distintas permite que cada parte del sistema evolucione de forma independiente. Un cambio en cómo se representa un producto no debería afectar la lógica del servicio ni la interacción por consola. Aplicar estos principios desde el inicio reduce el esfuerzo necesario para mantener y ampliar el proyecto a medida que los requisitos cambian.
