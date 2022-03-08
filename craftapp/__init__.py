from flask_sqlalchemy import SQLAlchemy
from flask import Flask


server = Flask(__name__)
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Local Server DB
# server.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:BlackHeist197@localhost/craftDB"

# for your live Heroku PostgreSQL database
username = 'vhqehuwdwfuyyl'
password = '45b56a2442d08dddebcd39177a2048da8054b203ad75e1916fca9cf16980a05b'
host = 'ec2-3-248-87-6.eu-west-1.compute.amazonaws.com'
port = 5432
dbname = 'ddncsklomh2hu2'
server.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"
# server.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://gehhvfyrvfuptd:4376c3e910f1b958715a4828aa0d2628c02223b6e5e10000610de23f2226eeab@ec2-54-74-14-109.eu-west-1.compute.amazonaws.com:5432/ddmgclh4fpen7r"

db = SQLAlchemy(server)

from craftapp import routes