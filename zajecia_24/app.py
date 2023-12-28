from flask import Flask
from routes import paths
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.register_blueprint(paths)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zajecia_26.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True, default="default_email@gmail.com")


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String, nullable=False)
    money = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, unique=True)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)