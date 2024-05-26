from enum import Enum


class BookingStatus(Enum):
    PENDING = "Pendiente"
    CONFIRMED = "Confirmado"
    CANCELLED = "Cancelado"

    def __str__(self):
        return self.name
