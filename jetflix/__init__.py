from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialization

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.db'
app.config["SECRET_KEY"] = "3a2e90fb987dd93743b5e35d"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginmgr = LoginManager(app)

from jetflix import routes