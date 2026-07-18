from modelos.producto import Producto


class Bebida(Producto):

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        presentacion: str,
        envase: str,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.presentacion = self._validar_texto(presentacion, "La presentacion no puede estar vacia.")
        self.envase = self._validar_texto(envase, "El envase no puede estar vacio.")

    def mostrar_informacion(self) -> str:
        return (
            f"{super().mostrar_informacion()} | "
            f"Presentacion: {self.presentacion} | "
            f"Envase: {self.envase}"
        )
