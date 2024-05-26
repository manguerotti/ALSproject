import json
from datetime import datetime

import flask
import flask_login.login_manager
import sirope
from flask import Flask, render_template, request, redirect, url_for, session

from enums.bookingstatus import BookingStatus
from enums.payment_method import PaymentMethod
from modules.bookings.models import Booking
from modules.carbookings.car_bookings import CarAndBooking
from modules.cars.models import Car
from modules.users.models import User
from utils.constants import REGISTER_HTML, SEARCH_RESULTS_HTML
from utils.utils import create_user, set_up, calculate_price_booking


def create_app():
    lmanager = flask_login.LoginManager()
    fapp = flask.Flask(__name__)
    srp = sirope.Sirope()

    fapp.config.from_file("config.json", load=json.load)
    fapp.secret_key = fapp.config['SECRET_KEY']
    lmanager.init_app(fapp)
    lmanager.login_view = 'login'

    return fapp, lmanager, srp


app, lm, db = create_app()


@lm.user_loader
def user_loader(username):
    return User.find(db, username)


@lm.unauthorized_handler
def unauthorized_handler():
    flask.flash("No autorizado. Por favor, inicia sesión.")
    return redirect(url_for('login'))


@app.route('/')
def index():
    logged = flask_login.current_user.is_authenticated
    return flask.render_template('index.html', logged_user=logged)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']

        if not username:
            flask.flash("¿Y el nombre de usuario?")
            return flask.redirect(url_for('login'))

        if not password:
            flask.flash("¿Y la contraseña?")
            return flask.redirect(url_for('login'))

        usr = User.find(db, username)
        if not usr or not usr.chk_password(password):
            flask.flash("Usuario o contraseña incorrectos")
            return flask.redirect(url_for('login'))

        flask_login.login_user(usr)
        return flask.redirect(url_for('index'))

    if request.method == 'GET':
        return flask.render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password-repeat']
        email = request.form['email']
        full_name = request.form['full_name']

        if not full_name:
            flask.flash("¿Y el nombre completo?")
            return flask.render_template(REGISTER_HTML)

        if not email:
            flask.flash("¿Y el email?")
            return flask.render_template(REGISTER_HTML)

        if not password:
            flask.flash("¿Y las contraseña?")
            return flask.render_template(REGISTER_HTML)

        if not username:
            flask.flash("¿Y el nombre de usuario?")
            return flask.render_template(REGISTER_HTML)

        if password != password2:
            flask.flash("Las contraseñas no coinciden")
            return flask.render_template(REGISTER_HTML)

        usr = user_loader(username)
        if not usr:
            db.save(User(username, password, email, full_name))
        else:
            flask.flash("Este nombre de usuario ya existe inténtelo de nuevo")
            return flask.render_template(REGISTER_HTML)

        return flask.redirect(url_for('index'))

    if request.method == 'GET':
        return flask.render_template(REGISTER_HTML)


@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return flask.redirect(url_for('index'))


@app.route('/my_account/' + str(flask_login.current_user))
@flask_login.login_required
def my_account():
    usr = flask_login.current_user
    bookings = db.enumerate(Booking)
    user_bookings = []
    for booking in bookings:
        if booking.user_oid == usr.__oid__:
            car = db.load(booking.car_oid)
            user_bookings.append(CarAndBooking(car.model, car.brand, booking.start_datetime, booking.end_datetime,
                                               booking.price, booking.booking_id, booking.additional_info))

    return flask.render_template('my_account.html', user=usr, user_bookings=user_bookings)


@app.route('/search_results', methods=['GET', 'POST'])
@flask_login.login_required
def search_results():
    if request.method == 'POST':
        start_date = datetime.strptime(request.form['start'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end'], '%Y-%m-%d')
        session['start_date'] = start_date.strftime('%Y-%m-%d')
        session['end_date'] = end_date.strftime('%Y-%m-%d')

        if not start_date or not end_date:
            flask.flash("Por favor, seleccione una fecha de inicio y una fecha de fin")
            return flask.redirect(url_for('index'))

        if start_date < datetime.now():
            flask.flash("La fecha de inicio no puede ser anterior a la fecha actual")
            return flask.redirect(url_for('index'))

        if end_date < start_date:
            flask.flash("La fecha de fin no puede ser anterior a la fecha de inicio")
            return flask.redirect(url_for('index'))

        if start_date == end_date:
            flask.flash("La fecha de inicio y la fecha de fin no pueden ser iguales")
            return flask.redirect(url_for('index'))

        if start_date > end_date:
            flask.flash("La fecha de inicio no puede ser posterior a la fecha de fin")
            return flask.redirect(url_for('index'))

        cars = get_cars_search_results(start_date, end_date)

        if not cars:
            flask.flash("No hay coches disponibles para las fechas seleccionadas")
            return flask.redirect(url_for('index'))

        return flask.render_template(SEARCH_RESULTS_HTML, cars=cars)

    if request.method == 'GET':
        cars = db.enumerate(Car)
        return flask.render_template(SEARCH_RESULTS_HTML, cars=cars)


@app.route('/car_details/<car_id>', methods=['GET'])
def car_details(car_id):
    start_date = datetime.strptime(session['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(session['end_date'], '%Y-%m-%d')
    car = Car.find(db, car_id)
    total_price = calculate_price_booking(start_date, end_date, car.daily_price)
    return flask.render_template('car_details.html', car=car, start_date=start_date,
                                 end_date=end_date, total_price=total_price)


@app.route('/create_booking/<car_id>', methods=['GET', 'POST'])
def create_booking(car_id):
    if request.method == 'POST':
        car = Car.find(db, car_id)
        car_oid = car.__oid__
        start_date = datetime.strptime(session['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(session['end_date'], '%Y-%m-%d')
        user_oid = flask_login.current_user.__oid__
        price = calculate_price_booking(start_date, end_date, car.daily_price)
        additional_info = request.form['additional_info']
        booking = Booking(user_oid, car_oid, start_date, end_date, BookingStatus.CONFIRMED, price,
                          PaymentMethod.BITCOIN, additional_info)
        db.save(booking)
        return flask.redirect(url_for('my_account'))


@app.route('/delete_user')
def delete_user():
    bookings = db.enumerate(Booking)
    if bookings is not None:
        for booking in bookings:
            if booking.user_oid == flask_login.current_user.__oid__:
                db.delete(booking.__oid__)
    db.delete(flask_login.current_user.__oid__)
    return flask.redirect(url_for('index'))


@app.route('/cancel_booking/<booking_id>')
def cancel_booking(booking_id):
    booking = Booking.find(db, booking_id)
    db.delete(booking.__oid__)
    return flask.redirect(url_for('my_account'))


def get_cars_search_results(start_date: datetime, end_date: datetime):
    cars = list(db.enumerate(Car))
    bookings = db.enumerate(Booking)
    for booking in bookings:
        if start_date <= booking.end_datetime or end_date >= booking.start_datetime:
            car_to_remove_id = db.load(booking.car_oid).car_id
            for car in cars:
                if car.car_id == car_to_remove_id:
                    cars.remove(car)
    return cars


if __name__ == '__main__':
    set_up(db)
    app.run(debug=True)
