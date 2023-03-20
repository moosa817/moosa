from flask import Blueprint

index_page = Blueprint('index',__name__,template_folder='templates')


@index_page.route("/")
def index():
    return 'hey lol'