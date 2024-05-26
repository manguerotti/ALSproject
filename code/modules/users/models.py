import flask_login
import sirope
import werkzeug.security as safe


class User(flask_login.UserMixin):
    def __init__(self, username: str, password: str, email: str, full_name: str):
        self._username = username
        self._password = safe.generate_password_hash(password)
        self._email = email
        self._full_name = full_name

    def get_id(self):
        return self._username

    @property
    def username(self) -> str:
        return self._username

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def email(self) -> str:
        return self._email

    def chk_password(self, pwd):
        return safe.check_password_hash(self._password, pwd)

    @staticmethod
    def current_user():
        usr = flask_login.current_user

        if usr.is_anonymous:
            flask_login.logout_user()
            usr = None

        return usr

    @staticmethod
    def find(db: sirope.Sirope, username):
        return db.find_first(User, lambda u: u.username == username)

    def __str__(self):
        return (f"Nombre completo de usuario: {self.full_name}\n"
                f"Nombre de usuario: {self.username}\n"
                f"Correo electrónico: {self.email}")
