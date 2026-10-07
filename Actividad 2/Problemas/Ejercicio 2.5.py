
# Ejercicio 2.5 - Métodos con parámetros (CuentaBancaria)

from enum import Enum


class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"


class CuentaBancaria:
    def __init__(self, nombres_titular: str, apellidos_titular: str, numero_cuenta: int,
                 tipo_cuenta: TipoCuenta):
        self.nombres_titular: str = nombres_titular
        self.apellidos_titular: str = apellidos_titular
        self.numero_cuenta: int = numero_cuenta
        self.tipo_cuenta: TipoCuenta = tipo_cuenta
        self.saldo: float = 0.0   # Modificado para imprimir con el decimal

    def imprimir(self) -> None:
        print("Nombres del titular =", self.nombres_titular)
        print("Apellidos del titular =", self.apellidos_titular)
        print("Número de cuenta =", self.numero_cuenta)
        print("Tipo de cuenta =", self.tipo_cuenta.name)
        print("Saldo =", self.saldo)

    def consultar_saldo(self) -> None:
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        print("El valor a consignar debe ser mayor que cero.")
        return False

    def retirar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        print("El valor a retirar debe ser mayor que cero y no puede superar el saldo.")
        return False


def main():
    cuenta = CuentaBancaria("Kevin", "Monsalve Zype", 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)


if __name__ == "__main__":
    main()