#!/usr/bin/env python3
"""
function with the babel.localeselector decorator.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate the Babel object
babel = Babel(app)


# Create a Config class
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Use Config for Flask app configuration
app.config.from_object(Config)


# Define get_locale function
@babel.localeselector
def get_locale():
    # Use request.accept_languages to determine the best match
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
