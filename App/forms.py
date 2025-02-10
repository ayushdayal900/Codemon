from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from App.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    lname = StringField('Last name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is already taken.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('That email is already taken.')



class LoginForm(FlaskForm):
    email_username = StringField('Email or Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')




class UpdateAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    lname = StringField('Last name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')


    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('That username is already taken.')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('That email is already taken.')


class UpdateForm(FlaskForm):
    # id = IntegerField('Id', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Post')





class Bug_Buster_problems_Form(FlaskForm):
    id = IntegerField('Problem Id', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    buggyCode = StringField('BuggyCode', validators=[DataRequired()])
    correctSolution = StringField('CorrectSolution', validators=[DataRequired()])
    hints = StringField('Hints', validators=[DataRequired()])
    submit = SubmitField('Post')



class Code_Patcher_problems_Form(FlaskForm):
    id = IntegerField('Problem Id', validators=[DataRequired()])
    question = StringField('question', validators=[DataRequired()])
    answer = StringField('answer', validators=[DataRequired()])
    submit = SubmitField('Post')



class Trainer_Test_problems_Form(FlaskForm):
    id = IntegerField('Problem Id', validators=[DataRequired()])
    question = StringField('question', validators=[DataRequired()])
    option1 = StringField('answer', validators=[DataRequired()])
    option2 = StringField('answer', validators=[DataRequired()])
    option3 = StringField('answer', validators=[DataRequired()])
    option4 = StringField('answer', validators=[DataRequired()])
    answer = StringField('answer', validators=[DataRequired()])
    submit = SubmitField('Post')



class Memory_Card_problems_Form(FlaskForm):
    id = IntegerField('Problem Id', validators=[DataRequired()])
    concept = StringField('Concept', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    submit = SubmitField('Post')



