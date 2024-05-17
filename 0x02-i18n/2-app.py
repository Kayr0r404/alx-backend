#!/usr/bin/env python3
"""task 1"""

from flask import Flask, request, render_template


from flask_babel import Babel

from flask import Flask
from flask_babel import Babel


class Config:
    "configuration for babel"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """get local language"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", strict_slashes=False)
def index():
    """index rendering a page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
