from dotenv import load_dotenv
import os
if __name__ == '__main__':
    envs = load_dotenv() if os.path.exists('.env') else None
    if envs:print("env variables loaded from .env 1")


from app import MyApp #custom class on 'app' folder
from flask import Flask



app = Flask(__name__)

myApp = MyApp(app)


myApp.load_blueprints()
myApp.setup_logging()



if __name__ == '__main__':
    myApp.run_app()
    