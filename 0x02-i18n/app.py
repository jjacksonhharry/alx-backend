#!/usr/bin/env python3
"""
basic flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    # 1. Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass

    # 2. Timezone from user settings
    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            try:
                return pytz.timezone(timezone).zone
            except UnknownTimeZoneError:
                pass

    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    current_time = None
    if get_timezone():
        try:
            current_time = datetime.now(pytz.timezone(get_timezone()))
        except UnknownTimeZoneError:
            pass
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
