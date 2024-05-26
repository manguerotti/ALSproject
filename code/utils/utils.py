import json
from datetime import datetime

import flask
import flask_login
import sirope

from enums.availability import Availability
from enums.bookingstatus import BookingStatus
from enums.payment_method import PaymentMethod
from enums.transmission_types import TransmissionType
from modules.bookings.models import Booking
from modules.cars.models import Car
from modules.users.models import User


def create_user() -> User:
    return User('1234', '1234', 'email', 'full_name')


def calculate_price_booking(start_date: datetime, end_date: datetime, daily_price: float) -> float:
    days = (end_date - start_date).days
    return round(days * daily_price, 2)


def set_up(db: sirope.Sirope()):
    db._redis.flushdb()
    save_cars(db)
    save_users(db)
    save_booking(db)


def save_users(db: sirope.Sirope()):
    db.save(create_user())


def save_booking(db: sirope.Sirope()):
    car_iterator = db.load_all_keys(Car)
    user_iterator = db.load_all_keys(User)
    car_oid = next(car_iterator, None)
    user_oid = next(user_iterator, None)
    start_date = datetime(2024, 6, 11)
    end_date = datetime(2024, 6, 15)
    daily_price = db.load(car_oid).daily_price
    price = calculate_price_booking(start_date, end_date, daily_price)
    booking = Booking(user_oid, car_oid, start_date, end_date, BookingStatus.CONFIRMED, price, PaymentMethod.BITCOIN,
                      'additional_info')
    db.save(booking)


def save_cars(db: sirope.Sirope()):
    car_1 = Car("Toyota", "Corolla", 2018, "Blue", 4, TransmissionType.AUTOMATIC, 50.0, Availability.AVAILABLE,
                "Excelente estado", )
    car_2 = Car("Honda", "Accord", 2019, "Red", 4, TransmissionType.AUTOMATIC, 55.0, Availability.AVAILABLE,
                "Perfecto para viajes largos")
    car_3 = Car("Ford", "F-150", 2020, "Black", 4, TransmissionType.AUTOMATIC, 80.0, Availability.AVAILABLE,
                "Potente y resistente")
    car_4 = Car("Chevrolet", "Camaro", 2017, "Yellow", 2, TransmissionType.MANUAL, 100.0, Availability.AVAILABLE,
                "Deportivo y elegante")
    car_5 = Car("Nissan", "Altima", 2016, "White", 4, TransmissionType.AUTOMATIC, 45.0, Availability.AVAILABLE,
                "Confortable y eficiente")
    car_6 = Car("Toyota", "Camry", 2021, "Silver", 4, TransmissionType.AUTOMATIC, 60.0, Availability.AVAILABLE,
                "Tecnología avanzada")
    car_7 = Car("Honda", "Civic", 2015, "Gray", 4, TransmissionType.AUTOMATIC, 40.0, Availability.AVAILABLE,
                "Fiable y económico")
    car_8 = Car("Ford", "Mustang", 2022, "Red", 2, TransmissionType.MANUAL, 120.0, Availability.AVAILABLE,
                "Icono americano")
    car_9 = Car("Chevrolet", "Silverado", 2019, "Blue", 4, TransmissionType.AUTOMATIC, 90.0, Availability.AVAILABLE,
                "Ideal para carga")
    car_10 = Car("Nissan", "Sentra", 2018, "Black", 4, TransmissionType.AUTOMATIC, 50.0, Availability.AVAILABLE,
                 "Compacto y ágil")
    car_11 = Car("Toyota", "Rav4", 2020, "White", 4, TransmissionType.AUTOMATIC, 70.0, Availability.AVAILABLE,
                 "SUV versátil")
    car_12 = Car("Honda", "Pilot", 2019, "Silver", 4, TransmissionType.AUTOMATIC, 85.0, Availability.AVAILABLE,
                 "Gran espacio interior")
    car_13 = Car("Ford", "Escape", 2017, "Blue", 4, TransmissionType.AUTOMATIC, 55.0, Availability.AVAILABLE,
                 "Eficiente en combustible")
    car_14 = Car("Chevrolet", "Equinox", 2018, "Red", 4, TransmissionType.AUTOMATIC, 60.0, Availability.AVAILABLE,
                 "Confortable y seguro")
    car_15 = Car("Nissan", "Rogue", 2021, "Black", 4, TransmissionType.AUTOMATIC, 75.0, Availability.AVAILABLE,
                 "Estilo moderno")
    car_16 = Car("Toyota", "Highlander", 2019, "Gray", 4, TransmissionType.AUTOMATIC, 90.0, Availability.AVAILABLE,
                 "Potente y espacioso")
    car_17 = Car("Honda", "HR-V", 2020, "Blue", 4, TransmissionType.AUTOMATIC, 65.0, Availability.AVAILABLE,
                 "Compacto y ágil")
    car_18 = Car("Ford", "Explorer", 2016, "White", 4, TransmissionType.AUTOMATIC, 80.0, Availability.AVAILABLE,
                 "Familiar y seguro")
    car_19 = Car("Chevrolet", "Tahoe", 2018, "Black", 4, TransmissionType.AUTOMATIC, 100.0, Availability.AVAILABLE,
                 "Todo terreno")
    car_20 = Car("Nissan", "Pathfinder", 2017, "Red", 4, TransmissionType.AUTOMATIC, 85.0, Availability.AVAILABLE,
                 "Potencia y comodidad")
    car_21 = Car("Toyota", "Sienna", 2022, "Gray", 4, TransmissionType.AUTOMATIC, 110.0, Availability.AVAILABLE,
                 "Familiar y versátil")
    car_22 = Car("Honda", "Odyssey", 2019, "White", 4, TransmissionType.AUTOMATIC, 95.0, Availability.AVAILABLE,
                 "Espacioso y cómodo")
    car_23 = Car("Ford", "Expedition", 2018, "Blue", 4, TransmissionType.AUTOMATIC, 120.0, Availability.AVAILABLE,
                 "Gran capacidad de carga")
    car_24 = Car("Chevrolet", "Suburban", 2020, "Black", 4, TransmissionType.AUTOMATIC, 130.0, Availability.AVAILABLE,
                 "Lujo y espacio")
    car_25 = Car("Nissan", "Armada", 2019, "Silver", 4, TransmissionType.AUTOMATIC, 140.0, Availability.AVAILABLE,
                 "Potencia y elegancia")
    car_26 = Car("Toyota", "Land Cruiser", 2021, "White", 4, TransmissionType.AUTOMATIC, 150.0,
                 Availability.AVAILABLE, "Todo terreno de lujo")
    car_27 = Car("Honda", "Civic Type R", 2020, "Blue", 4, TransmissionType.MANUAL, 160.0, Availability.AVAILABLE,
                 "Deportividad extrema")
    car_28 = Car("Ford", "Focus RS", 2018, "Black", 4, TransmissionType.MANUAL, 170.0, Availability.AVAILABLE,
                 "Hot hatch poderoso")
    car_29 = Car("Chevrolet", "Camaro ZL1", 2022, "Red", 2, TransmissionType.AUTOMATIC, 180.0, Availability.AVAILABLE,
                 "Músculo americano")
    car_30 = Car("Nissan", "GT-R", 2021, "Silver", 2, TransmissionType.AUTOMATIC, 190.0, Availability.AVAILABLE,
                 "Supercar japonés")
    car_31 = Car("Toyota", "Supra", 2022, "White", 2, TransmissionType.AUTOMATIC, 200.0, Availability.AVAILABLE,
                 "Leyenda resucitada")
    car_32 = Car("Honda", "NSX", 2020, "Blue", 2, TransmissionType.AUTOMATIC, 210.0, Availability.AVAILABLE,
                 "Híbrido de alto rendimiento")
    car_33 = Car("Ford", "Mustang Shelby GT500", 2021, "Black", 2, TransmissionType.MANUAL, 220.0,
                 Availability.AVAILABLE, "Máquina de carreras")
    car_34 = Car("Chevrolet", "Corvette Stingray", 2020, "Red", 2, TransmissionType.AUTOMATIC, 230.0,
                 Availability.AVAILABLE, "Ícono americano")
    car_35 = Car("Nissan", "370Z", 2019, "Silver", 2, TransmissionType.MANUAL, 240.0, Availability.AVAILABLE,
                 "Deportivo japonés")
    car_36 = Car("Toyota", "GR Supra", 2022, "White", 2, TransmissionType.AUTOMATIC, 250.0, Availability.AVAILABLE,
                 "Resucitando una leyenda")
    car_37 = Car("Honda", "Civic Si", 2021, "Blue", 4, TransmissionType.MANUAL, 260.0, Availability.AVAILABLE,
                 "Deportividad asequible")
    car_38 = Car("Ford", "Focus ST", 2020, "Black", 4, TransmissionType.MANUAL, 270.0, Availability.AVAILABLE,
                 "Divertido y práctico")
    car_39 = Car("Chevrolet", "Camaro SS", 2019, "Red", 2, TransmissionType.AUTOMATIC, 280.0, Availability.AVAILABLE,
                 "Músculo americano")
    car_40 = Car("Nissan", "370Z Nismo", 2018, "Silver", 2, TransmissionType.MANUAL, 290.0, Availability.AVAILABLE,
                 "Deportividad extrema")

    cars = [car_1, car_2, car_3, car_4, car_5, car_6, car_7, car_8, car_9, car_10, car_11, car_12, car_13, car_14,
            car_15, car_16, car_17, car_18, car_19, car_20, car_21, car_22, car_23, car_24, car_25, car_26, car_27,
            car_28, car_29, car_30, car_31, car_32, car_33, car_34, car_35, car_36, car_37, car_38, car_39, car_40]

    for car in cars:
        db.save(car)
