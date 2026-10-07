
# Ejercicio 2.4 - Métodos con y sin valor de retorno (figuras geométricas)

import math


class Circulo:
    def __init__(self, radio: float):
        self.radio: float = radio

    def calcular_area(self) -> float:
        return math.pi * self.radio ** 2

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base: float = base
        self.altura: float = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * self.base + 2 * self.altura


class Cuadrado:
    def __init__(self, lado: float):
        self.lado: float = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.base: float = base
        self.altura: float = altura

    def calcular_area(self) -> float:
        return self.base * self.altura / 2

    def calcular_hipotenusa(self) -> float:
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "equilátero"
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "escaleno"
        else:
            return "isósceles"


def main():
    circulo = Circulo(2)
    rectangulo = Rectangulo(1, 2)
    cuadrado = Cuadrado(3)
    triangulo = TrianguloRectangulo(3, 5)

    print(f"El área del círculo es = {circulo.calcular_area():.2f}")
    print(f"El perímetro del círculo es = {circulo.calcular_perimetro():.2f}")
    print()
    print(f"El área del rectángulo es = {rectangulo.calcular_area():.2f}")
    print(f"El perímetro del rectángulo es = {rectangulo.calcular_perimetro():.2f}")
    print()
    print(f"El área del cuadrado es = {cuadrado.calcular_area():.2f}")
    print(f"El perímetro del cuadrado es = {cuadrado.calcular_perimetro():.2f}")
    print()
    print(f"El área del triángulo es = {triangulo.calcular_area():.2f}")
    print(f"El perímetro del triángulo es = {triangulo.calcular_perimetro():.2f}")
    print("Es un triángulo", triangulo.determinar_tipo_triangulo())


if __name__ == "__main__":
    main()