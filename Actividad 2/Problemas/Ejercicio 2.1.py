
# Ejercicio 2.1 - Definición de clases (Persona)

class Persona:
    def __init__(self, nombre: str, apellidos: str, numero_documento: str, anio_nacimiento: int):
        self.nombre: str = nombre
        self.apellidos: str = apellidos
        self.numero_documento: str = numero_documento
        self.anio_nacimiento: int = anio_nacimiento

    def imprimir(self) -> None:
        print("Nombre =", self.nombre)
        print("Apellidos =", self.apellidos)
        print("Número de documento de identidad =", self.numero_documento)
        print("Año de nacimiento =", self.anio_nacimiento)
        print()


def main():
    p1 = Persona("Elay", "Rivas Alvarez", "1053121010", 1998)
    p2 = Persona("Vec", "Diaz Monsalve", "1053223344", 2001)

    p1.imprimir()
    p2.imprimir()


if __name__ == "__main__":
    main()