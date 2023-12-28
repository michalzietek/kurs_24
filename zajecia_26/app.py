from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
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
    # michal = User(name="Michal", surname="Zietkowski")
    # adam = User(name="Adam", surname="Bąk")
    # konrad = User(name="Konrad", surname="Wawszczyk")
    # db.session.add_all([michal, adam, konrad])
    # db.session.commit()
    # michal_2 = User(name="Michal", surname="Kowalski")
    # db.session.add(michal_2)
    # db.session.commit()
    # users = db.session.query(User).all()
    # michal_users = db.session.query(User).filter(User.name=="Michal").all()
    # michal_user = db.session.query(User).filter(User.name=="Michal").first()
    # # michal_user.name = "Andrzej"
    # # db.session.add(michal_user)
    # # db.session.commit()
    # andrzej_users = db.session.query(User).filter(User.name=="Andrzej").delete()
    # account_for_adam = Account(account_number="123434545", user_id=2)
    # db.session.add(account_for_adam)
    # db.session.commit()

    # print(users)
    # print(michal_user)


if __name__ == "__main__":
    app.run(debug=True)