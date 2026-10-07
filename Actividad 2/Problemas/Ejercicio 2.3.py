
# Ejercicio 2.3 - Estado de un objeto (Automóvil)

from enum import Enum
from typing import Optional


class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas natural"


class TipoAutomovil(Enum):
    CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"


class Automovil:
    def __init__(self, marca: str, modelo: int, motor: int, tipo_combustible: TipoCombustible,
                 tipo_automovil: TipoAutomovil, numero_puertas: int, cantidad_asientos: int,
                 velocidad_maxima: int, color: Color):
        self.marca: str = marca
        self.modelo: int = modelo                  # año de fabricación
        self.motor: int = motor                    # cilindraje en litros
        self.tipo_combustible: TipoCombustible = tipo_combustible
        self.tipo_automovil: TipoAutomovil = tipo_automovil
        self.numero_puertas: int = numero_puertas
        self.cantidad_asientos: int = cantidad_asientos
        self.velocidad_maxima: int = velocidad_maxima   # km/h
        self.color: Color = color
        self.velocidad_actual: int = 0                  # km/h

    # --- get y set ---
    def get_marca(self) -> str:
        return self.marca

    def set_marca(self, marca: str) -> None:
        self.marca = marca

    def get_modelo(self) -> int:
        return self.modelo

    def set_modelo(self, modelo: int) -> None:
        self.modelo = modelo

    def get_motor(self) -> int:
        return self.motor

    def set_motor(self, motor: int) -> None:
        self.motor = motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self.tipo_combustible

    def set_tipo_combustible(self, tipo_combustible: TipoCombustible) -> None:
        self.tipo_combustible = tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self.tipo_automovil

    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil) -> None:
        self.tipo_automovil = tipo_automovil

    def get_numero_puertas(self) -> int:
        return self.numero_puertas

    def set_numero_puertas(self, numero_puertas: int) -> None:
        self.numero_puertas = numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self.cantidad_asientos

    def set_cantidad_asientos(self, cantidad_asientos: int) -> None:
        self.cantidad_asientos = cantidad_asientos

    def get_velocidad_maxima(self) -> int:
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima: int) -> None:
        self.velocidad_maxima = velocidad_maxima

    def get_color(self) -> Color:
        return self.color

    def set_color(self, color: Color) -> None:
        self.color = color

    def get_velocidad_actual(self) -> int:
        return self.velocidad_actual

    def set_velocidad_actual(self, velocidad_actual: int) -> None:
        self.velocidad_actual = velocidad_actual

    # --- comportamiento ---
    def acelerar(self, incremento: int) -> None:
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

    def desacelerar(self, decremento: int) -> None:
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self) -> None:
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: float) -> Optional[float]:
        # distancia en km, el resultado queda en horas
        if self.velocidad_actual == 0:
            print("El automóvil está detenido, no se puede calcular el tiempo.")
            return None
        return distancia / self.velocidad_actual

    def imprimir(self) -> None:
        print("Marca =", self.marca)
        print("Modelo =", self.modelo)
        print("Motor =", self.motor)
        print("Tipo de combustible =", self.tipo_combustible.name)
        print("Tipo de automóvil =", self.tipo_automovil.name)
        print("Número de puertas =", self.numero_puertas)
        print("Cantidad de asientos =", self.cantidad_asientos)
        print("Velocida máxima =", self.velocidad_maxima)
        print("Color =", self.color.name)


def main():
    auto1 = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL, TipoAutomovil.EJECUTIVO,
                      5, 6, 250, Color.NEGRO)
    auto1.imprimir()

    auto1.set_velocidad_actual(100)
    print("Velocidad actual =", auto1.get_velocidad_actual())

    auto1.acelerar(20)
    print("Velocidad actual =", auto1.get_velocidad_actual())

    auto1.desacelerar(50)
    print("Velocidad actual =", auto1.get_velocidad_actual())

    auto1.frenar()
    print("Velocidad actual =", auto1.get_velocidad_actual())

    # con el carro frenado esto debe mostrar el mensaje de error
    auto1.desacelerar(20)


if __name__ == "__main__":
    main()