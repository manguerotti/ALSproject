import datetime

import sirope
from sirope import OID

from enums.bookingstatus import BookingStatus
from enums.payment_method import PaymentMethod


class Booking:
    def __init__(self, user_oid: OID, car_oid: OID, start_datetime: datetime, end_datetime: datetime,
                 status: BookingStatus, price: float, payment_method: PaymentMethod, additional_info: str):
        self._booking_id = f"{user_oid}_{car_oid}_{start_datetime.strftime('%Y%m%d%H%M%S')}"
        self._user_oid = user_oid
        self._car_oid = car_oid
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._status = status.value
        self._price = price
        self._payment_method = payment_method.value
        self._additional_info = additional_info

    @property
    def booking_id(self):
        return self._booking_id

    @property
    def user_oid(self) -> OID:
        return self._user_oid

    @property
    def car_oid(self) -> OID:
        return self._car_oid

    @property
    def start_datetime(self) -> datetime:
        return self._start_datetime

    @property
    def end_datetime(self) -> datetime:
        return self._end_datetime

    @property
    def status(self) -> str:
        return self._status

    @property
    def price(self):
        return self._price

    @property
    def payment_method(self) -> str:
        return self._payment_method

    @property
    def additional_info(self) -> str:
        return self._additional_info

    @staticmethod
    def find(db: sirope.Sirope, booking_id):
        return db.find_first(Booking, lambda b: b.booking_id == booking_id)

    def __str__(self):
        return (f"ID de reserva: {self.booking_id}\n"
                f"ID de usuario: {self.user_oid}\n"
                f"ID de coche: {self.car_oid}\n"
                f"Fecha de inicio: {self.start_datetime}\n"
                f"Fecha de fin: {self.end_datetime}\n"
                f"Estado: {self.status}\n"
                f"Precio: {self.price}\n"
                f"Método de pago: {self.payment_method}\n"
                f"Información adicional: {self.additional_info}")


