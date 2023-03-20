from app import MyApp #custom class on 'app' folder
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    envs = load_dotenv() if os.path.exists('.env') else None
    if envs:print("env variables loaded from .env 1")


myApp = MyApp('config.py')


myApp.load_blueprints()
myApp.setup_logging()
myApp.run_app()
