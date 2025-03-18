from App import db, login_manager
from datetime import datetime
from flask_login import UserMixin
# from sqlalchemy.orm import Session
# from sqlalchemy import event



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, nullable=False, default=0)
    username = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"User('{self.name}', '{self.lname}', '{self.dob}', '{self.email}')"



class Bug_Buster_problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False, default=0)
    buggyCode = db.Column(db.String(20), nullable=False)
    correctSolution = db.Column(db.String(20), nullable=False)
    hints = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.description}', '{self.buggyCode}', '{self.correctSolution}', '{self.hints}')"


class Code_Patcher_problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), nullable=False, default=0)
    answer = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.question}', '{self.answer}')"


class Trainer_Test_problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), nullable=False, default=0)
    option1 = db.Column(db.String(20), nullable=False)
    option2 = db.Column(db.String(20), nullable=False)
    option3 = db.Column(db.String(20), nullable=False)
    option4 = db.Column(db.String(20), nullable=False)
    answer = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"User('{self.question}', '{self.option1}', '{self.option2}', '{self.option3}', '{self.option4}', '{self.answer}')"



class Memory_Card_problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    concept = db.Column(db.String(1000), nullable=False, default=0)
    description = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"User('{self.question}', '{self.option1}', '{self.option2}', '{self.option3}', '{self.option4}', '{self.answer}')"
