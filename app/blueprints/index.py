from flask import Blueprint, render_template
import config
import os

template_dir = os.path.abspath('app/templates/')
static_dir = os.path.abspath('app/static/')

index_page = Blueprint('index',
                       __name__,
                       template_folder=template_dir,
                       static_folder=static_dir)


@index_page.route("/")
def index():
    return render_template("index.html")


@index_page.route("/projects")
def projects():
    return render_template("projects.html")