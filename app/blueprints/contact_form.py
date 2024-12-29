from email.mime.text import MIMEText
from flask import Blueprint, render_template, jsonify, request
import config
import re
import requests
import os

def SendEmail(name,lastname, email, message, subject,email_to):
   
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            color: #333;
        }}
        p {{
            font-size: 16px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Thank you for contacting us!</h1>
        <p>Dear {name},</p>
        <p>We have received your message and will get back to you shortly.</p>
        <p>Here is a copy of your message:</p>
        <p><strong>First Name:</strong> {name}</p>
        <p><strong>Last Name:</strong> {lastname}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Message:</strong> {message}</p>
        <p>Best regards,</p>
        <p>Muhammad Moosa</p>
    </div>
</body>
</html>"""

    # Send email via SendGrid
    headers = {
        "Authorization": f"Bearer {os.getenv("SENDGRID_API_KEY")}",
        "Content-Type": "application/json",
    }

    json_data = {
        "personalizations": [{"to": [{"email": email_to}]}],
        "from": {
            "email": os.getenv("EMAIL_SENDER"),
            "name": "Muhammad Moosa",
        },
        "subject": subject,
        "content": [{"type": "text/html", "value": html_content}],
    }

    # Send the request
    response = requests.post(
        "https://api.sendgrid.com/v3/mail/send", headers=headers, json=json_data
    )

    return response.status_code




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
            code1 = SendEmail(name,lastname, email, message, "Someone Sent a Message","muhammadmoosa.7782@gmail.com")
            code2 = SendEmail(name,lastname, email, message, "Message Recieved, Thank You",email)

            if code1 != 202 or code2 != 202:
                return jsonify({"error": "Failed to send message"})
            else:
                return jsonify({"success": "Message Sent Successfully"})

    return render_template("contact.html")