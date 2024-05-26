from enum import Enum


class TransmissionType(Enum):
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"
    DEFAULT = "Default"

    def __str__(self):
        return self.name



