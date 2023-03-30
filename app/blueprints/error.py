from flask import Blueprint, render_template, send_from_directory
import os
import config

template_dir = os.path.join(config.template_dir, 'error')
errors_bp = Blueprint('errors',
                      __name__,
                      template_folder=template_dir,
                      static_folder=config.static_dir,
                      static_url_path='/public')


@errors_bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@errors_bp.app_errorhandler(401)
def unauthorized_error(error):
    return render_template('401.html'), 401


@errors_bp.app_errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
