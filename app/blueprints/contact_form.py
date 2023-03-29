from email.mime.text import MIMEText
from flask import Blueprint, render_template, jsonify, request
import config
import re
import smtplib


def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = config.email_sender

    s = smtplib.SMTP(config.mail_server, config.mail_port)
    s.starttls()
    s.login(config.mail_user, config.mail_passwd)
    s.send_message(msg)
    s.quit()


contact_page = Blueprint('contact',
                         __name__,
                         template_folder=config.template_dir,
                         static_folder=config.static_dir)


@contact_page.route("/contact", methods=["POST", "GET"])
def contact():
    if request.form.get("email"):
        email = request.form.get("email")
        name = request.form.get("name")
        lastname = request.form.get("lastname")
        message = request.form.get("message")

        emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not (email and name and lastname and message):
            return jsonify({"error": "All Fields are required"})
        elif not re.match(emailRegex, email):
            return jsonify({"error": "Please Enter a valid email"})
        else:
            message = f"""
                First Name : {name}
                Last Name: {lastname}
                Email: {email}
                message: {message}
            """
            send_email(config.mail_email_reciever, "Message", message)
            return jsonify({"success": "Message Sent Successfully"})

    return render_template("contact.html")