import sirope

from enums.availability import Availability
from enums.transmission_types import TransmissionType
from utils.constants import IMAGE_BASE_URL


class Car:
    def __init__(self, brand: str, model: str, year: int, color: str, num_doors: int,
                 transmission_type: TransmissionType, daily_price: float, availability: Availability,
                 additional_info: str):
        self._car_id = f"{brand}_{model}_{year}"
        self._brand = brand
        self._model = model
        self._year = year
        self._color = color
        self._num_doors = num_doors
        self._transmission_type = transmission_type.value
        self._daily_price = daily_price
        self._availability = availability.value
        self._additional_info = additional_info
        self._img = IMAGE_BASE_URL + model.lower() + '.jpg'

    @property
    def car_id(self):
        return self._car_id

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @property
    def color(self) -> str:
        return self._color

    @property
    def num_doors(self) -> int:
        return self._num_doors

    @property
    def transmission_type(self) -> str:
        return self._transmission_type

    @property
    def availability(self) -> str:
        return self._availability

    @property
    def daily_price(self) -> float:
        return self._daily_price

    @property
    def additional_info(self) -> str:
        return self._additional_info

    @property
    def img(self) -> str:
        return self._img

    @staticmethod
    def find(db: sirope.Sirope, car_id):
        return db.find_first(Car, lambda c: c.car_id == car_id)

    def __str__(self):
        return (f"Marca: {self.brand}\n"
                f"Modelo: {self.model}\n"
                f"Año: {self.year}\n"
                f"Color: {self.color}\n"
                f"Número de puertas: {self.num_doors}\n"
                f"Tipo de transmisión: {self.transmission_type}\n"
                f"Precio diario: {self.daily_price}\n"
                f"Disponibilidad: {self.availability}\n"
                f"Información adicional: {self.additional_info}\n"
                f"Imagen: {self.img}")
