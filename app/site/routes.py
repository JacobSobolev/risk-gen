from flask import Blueprint

site_bp = Blueprint("site", __name__)

@site_bp.route("/")
def index():
    return "server up"