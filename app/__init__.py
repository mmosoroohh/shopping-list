from flask import Flask

app = Flask(__name__, instance_relative_config=True, static_path='', static_folder='static')

from app import views

app.secret_key='secret254'