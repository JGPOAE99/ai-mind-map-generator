from flask import Flask
from .config import Config
from .routes.health import health


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(health)
    return app


if __name__ == "__main__":
    create_app()
