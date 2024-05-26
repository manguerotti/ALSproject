import datetime


class CarAndBooking:
    def __init__(self, car_model, car_brand, booking_start_date, booking_end_date, booking_price, booking_id,
                 booking_additional_info):
        self._car_model = car_model
        self._car_brand = car_brand
        self._booking_start_date = booking_start_date
        self._booking_end_date = booking_end_date
        self._total_days = self.calculate_total_days(booking_start_date, booking_end_date)
        self._booking_price = booking_price
        self._booking_id = booking_id
        self._booking_additional_info = booking_additional_info

    @property
    def car_model(self):
        return self._car_model

    @car_model.setter
    def car_model(self, value):
        self._car_model = value

    @property
    def car_brand(self):
        return self._car_brand

    @car_brand.setter
    def car_brand(self, value):
        self._car_brand = value

    @property
    def booking_start_date(self) -> datetime:
        return self._booking_start_date.strftime("%d-%m-%Y")

    @booking_start_date.setter
    def booking_start_date(self, value):
        self._booking_start_date = value

    @property
    def booking_end_date(self) -> datetime:
        return self._booking_end_date.strftime("%d-%m-%Y")

    @booking_end_date.setter
    def booking_end_date(self, value):
        self._booking_end_date = value

    @property
    def booking_price(self):
        return self._booking_price

    @booking_price.setter
    def booking_price(self, value):
        self._booking_price = value

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value

    @property
    def booking_additional_info(self):
        return self._booking_additional_info

    @booking_additional_info.setter
    def booking_additional_info(self, value):
        self._booking_additional_info = value

    @property
    def total_days(self):
        return self._total_days

    @staticmethod
    def calculate_total_days(start_date, end_date):
        return (end_date - start_date).days

