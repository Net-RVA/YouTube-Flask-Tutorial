from flask import Flask
from app_blueprint import app_blueprint

app = Flask(__name__,static_folder="./images")
app.register_blueprint(app_blueprint)

