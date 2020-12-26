from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL = os.getenv("URL")

db = SQLAlchemy(app)
engine = db.engine
Base = db.Model