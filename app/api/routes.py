from flask import Blueprint

api_bp = Blueprint("api", __name__)

@api_bp.route("/report")
def gen_report():
    return "report"