#!/usr/bin/env python3
"""A simple Flask app with internationalization support.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Configuration class for the Flask app.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default language.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure the Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Selects the user's preferred language.

    Returns:
        str: The selected language.
    """
    # Check if 'locale' is in query parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)  # Optional: Print the selected locale to console
        return locale

    # Use request.accept_languages to determine the best match
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
