import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'mysql://student:yiJmf7G9kiQ7Vth**@10.57.10.25:3306/mikrotik'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.models import Dispatcher,Inputs
from app.views import input_view, system_view

app.register_blueprint(input_view.input_blueprint)


