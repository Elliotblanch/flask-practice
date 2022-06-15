from flask import Flask
from flask_sqlalchemy import SQLAlchxemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)
