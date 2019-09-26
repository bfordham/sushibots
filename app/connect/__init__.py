from flask import Blueprint

bp = Blueprint('connect', __name__)

from app.connect import routes