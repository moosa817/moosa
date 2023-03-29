from dotenv import load_dotenv
import os
import config

if __name__ == '__main__':
    envs = load_dotenv() if os.path.exists('.env') else None
    if envs: print("env variables loaded from .env 1")

from app import MyApp  #custom class on 'app' folder
from flask import Flask

app = Flask(__name__)

myApp = MyApp(app)

myApp.load_blueprints()

if __name__ == '__main__':
    debug_mode = True if str(config.debug_mode) == 'True' else False
    app.run(host='0.0.0.0', debug=debug_mode)

