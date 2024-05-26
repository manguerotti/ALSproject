from enum import Enum


class Availability(Enum):
    AVAILABLE = "Disponible"
    BOOKED = "Reservado"
    UNAVAILABLE = "No disponible"

    def __str__(self):
        return self.name
