#!/usr/bin/env python3
"""
function to parametrize your templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Instantiate the Babel object
babel = Babel(app)


# Create a Config class
class Config:
    """
    class that has a LANGUAGES class attribute equal
    to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Use Config for Flask app configuration
app.config.from_object(Config)


# Define get_locale function
@babel.localeselector
def get_locale():
    """
    accept language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    return template
    """
    return render_template(
            '3-index.html',
            title=_("home_title"),
            header=_("home_header"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
