
# Ejercicio 2.2 - Atributos con tipos primitivos (Planeta)

from enum import Enum

UA_MILLONES_KM = 149.59787 


class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"


class Planeta:
    def __init__(self, nombre: str = None, cantidad_satelites: int = 0, masa: float = 0,
                 volumen: float = 0, diametro: int = 0, distancia_sol: int = 0,
                 tipo: TipoPlaneta = None, es_observable: bool = False):
        self.nombre: str = nombre
        self.cantidad_satelites: int = cantidad_satelites
        self.masa: float = masa                    # en kg
        self.volumen: float = volumen              # en km3
        self.diametro: int = diametro              # en km
        self.distancia_sol: int = distancia_sol    # en millones de km
        self.tipo: TipoPlaneta = tipo
        self.es_observable: bool = es_observable

    def imprimir(self) -> None:
        print("Nombre del planeta =", self.nombre)
        print("Cantidad de satélites =", self.cantidad_satelites)
        print(f"Masa del planeta = {self.masa:.4e} kg")
        print(f"Volumen del planeta = {self.volumen:.4e} km3")
        print("Diámetro del planeta =", self.diametro, "km")
        print("Distancia al sol =", self.distancia_sol, "millones de km")
        print("Tipo de planeta =", self.tipo.value)
        print("Es observable =", self.es_observable)

    def calcular_densidad(self) -> float:
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        limite = 3.4 * UA_MILLONES_KM
        return self.distancia_sol > limite


def main():
    tierra = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150, TipoPlaneta.TERRESTRE, True)
    tierra.imprimir()
    print(f"Densidad del planeta = {tierra.calcular_densidad():.4e} kg/km3")
    print("Es planeta exterior =", tierra.es_planeta_exterior())
    print()

    jupiter = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 139820, 750, TipoPlaneta.GASEOSO, True)
    jupiter.imprimir()
    print(f"Densidad del planeta = {jupiter.calcular_densidad():.4e} kg/km3")
    print("Es planeta exterior =", jupiter.es_planeta_exterior())


if __name__ == "__main__":
    main()