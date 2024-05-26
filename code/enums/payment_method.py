from enum import Enum


class PaymentMethod(Enum):
    CASH = "Efectivo"
    CREDIT_CARD = "Tarjeta de crédito"
    DEBIT_CARD = "Tarjeta de débito"
    BANK_TRANSFER = "Transferencia bancaria"
    PAYPAL = "PayPal"
    BITCOIN = "Bitcoin"

    def __str__(self):
        return self.name
