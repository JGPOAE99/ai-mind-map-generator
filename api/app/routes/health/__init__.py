from flask import Blueprint

health = Blueprint('health', __name__, url_prefix='/health')

from . import health_route