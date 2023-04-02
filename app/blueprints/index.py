from flask import Blueprint, render_template, jsonify
import config
import os
import time

index_page = Blueprint('index',
                       __name__,
                       template_folder=config.template_dir,
                       static_folder=config.static_dir)


@index_page.route("/")
def index():
    return render_template("index.html")


@index_page.route("/projects")
def projects():
    # time.sleep(3)
    projects_html_dir = os.path.join(config.template_dir, "projects.html")
    with open(projects_html_dir, 'r') as file:
        data = file.read()
    html_content = data
    data = {"data": html_content}
    return jsonify(data)


@index_page.route("/index")
def index_file():
    #     {% include 'pages/home.html' %}

    # {% include 'pages/about.html' %}

    # {% include 'pages/skills.html' %}

    # {% include 'pages/contact.html' %}

    home_html_dir = os.path.join(config.template_dir, "pages/home.html")
    about_html_dir = os.path.join(config.template_dir, "pages/about.html")
    skills_html_dir = os.path.join(config.template_dir, "pages/skills.html")
    contact_html_dir = os.path.join(config.template_dir, "pages/contact.html")

    file_names = [
        home_html_dir, about_html_dir, skills_html_dir, contact_html_dir
    ]
    content = ""

    for file_name in file_names:
        with open(file_name, 'r') as file:
            content += file.read()

    html_content = content
    data = {"data": html_content}
    return jsonify(data)
