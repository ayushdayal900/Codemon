import os
from operator import or_
import sqlite3
from flask import abort, jsonify, render_template, request, redirect, url_for, flash
from App.models import Bug_Buster_problems, Code_Patcher_problems, Memory_Card_problems, Trainer_Test_problems, User
from App.forms import Bug_Buster_problems_Form, Code_Patcher_problems_Form, Memory_Card_problems_Form, RegistrationForm, LoginForm, Trainer_Test_problems_Form, UpdateAccountForm, UpdateForm
from App import app, db, bcrypt
from flask_login import login_user, current_user, login_required, logout_user 
import secrets
from PIL import Image
from flask_cors import CORS




# Enable CORS with credentials support
CORS(app, supports_credentials=True)
DB_NAME = "db.db"  




@app.route('/')
@app.route('/starts',methods = ['GET','POST'])
def starts():
    return render_template('./home1.html', title = 'Starting Page')


@app.route('/home',methods = ['GET','POST'])
def home():
    return render_template('./home.html', title = 'Home')




@app.route('/home1',methods = ['GET','POST'])
def home1():
    return render_template('./home1.html', title = 'Starting Page')




def save_pucture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


@app.route('/account',methods = ['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_pucture(form.picture.data)
            current_user.image_file = picture_file

        current_user.name = form.name.data
        current_user.lname = form.lname.data
        current_user.username = form.username.data
        current_user.dob = form.dob.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your Account has been updated", 'success')
        return redirect(url_for('account'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.name.data = current_user.name 
        form.lname.data = current_user.lname 
        form.dob.data = current_user.dob 
        form.email.data = current_user.email 

    image_file = url_for('static',filename="images/" + current_user.image_file)
    return render_template('account.html', title= "Account", image_file=image_file, form = form)








@app.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home1'))   
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
                    name = form.name.data,
                    lname = form.lname.data,
                    dob = form.dob.data,
                    username = form.username.data,
                    email = form.email.data,
                    password = hashed_password,
                    )

        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('login'))
    return render_template('register.html',form = form, title = 'Register')



    

@app.route('/login',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(
        or_(User.username == form.email_username.data,
            User.email == form.email_username.data
            )
        ).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember= form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('router'))
        else:
            flash(f'Login Unsuccessful. Please check your credientials.','danger')
    return render_template('login.html',form = form, title = 'Login')






@app.route('/logout',methods = ['GET','POST'])
def logout():
    
    logout_user()
    return redirect(url_for('home1'))




@app.route('/router',methods = ['GET','POST'])
def router():
    return render_template('./Landing_page.html', title = 'Home')


@app.route('/powerbi',methods = ['GET','POST'])
def powerbi():
    return render_template('./powerbi.html', title = 'Home')




@app.route('/lessons',methods = ['GET','POST'])
def lessons():
    return render_template('./lessons.html', title = 'Home')



@app.route('/beg_lessons',methods = ['GET','POST'])
def beg_lessons():
    return render_template('beg_lesson.html' )


@app.route('/int_lessons',methods = ['GET','POST'])
def int_lessons():
    return render_template('int_lesson.html')



@app.route('/adv_lessons',methods = ['GET','POST'])
def adv_lessons():
    return render_template('adv_lessons.html' )





@app.route('/users_list', methods = ['GET', 'POST'])
@login_required
def users_list():
    users = User.query.all()
    return render_template('users_list.html',  title = 'Users', users = users) 
        






@app.route('/leaderboard', methods=['GET','POST'])
@login_required
def leaderboard():
    # users = User.query.with_entities(User.username, User.points).order_by(User.points.desc()).all()
    return render_template('leaderboard.html')


@app.route('/minigame_memory_card', methods=['GET','POST'])
@login_required
def memory_card():
    return render_template('./minigame_memory_card.html')

@app.route('/game', methods=['GET','POST'])
@login_required
def game():
    return render_template('./game.html')



@app.route('/codedex', methods=['GET','POST'])
@login_required
def codedex():
    return render_template('codedex.html')


@app.route('/trainer_profile', methods=['GET','POST'])
@login_required
def trainer_profile():
    return render_template('trainer_profile.html')



@app.route('/trainer_test', methods=['GET','POST'])
@login_required
def trainer_test():
    return render_template('trainer_test.html')



@app.route('/flashcard1', methods=['GET','POST'])
@login_required
def flashcard1():
    return render_template('flash_card1.html')


@app.route('/flashcard2', methods=['GET','POST'])
@login_required
def flashcard2():
    return render_template('flash_card2.html')


@app.route('/about_us', methods=['GET','POST'])
@login_required
def about_us():
    return render_template('about_us.html')




@app.route('/backpack', methods=['GET','POST'])
@login_required
def backpack():
    return render_template('backpack.html')



@app.route('/minigame_bug_buster', methods=['GET','POST'])
@login_required
def minigame_bug_buster():
    return render_template('minigame_bug_buster.html')



@app.route('/terminal', methods=['GET','POST'])
@login_required
def terminal():
    return render_template('terminal.html')




@app.route('/minigame_code_patcher', methods=['GET','POST'])
@login_required
def minigame_code_patcher():
    return render_template('minigame_code_patcher.html')





@app.route('/settings', methods=['GET','POST'])
@login_required
def settings():
    return render_template('settings.html')








@app.route('/landing_page', methods=['GET','POST'])
@login_required
def landing_page():
    return render_template("landing_page.html")







@app.route('/add_bb_problem', methods=['GET','POST'])
@login_required
def add_bb_problem():
    form = Bug_Buster_problems_Form()
    if form.validate_on_submit():
        problem = Bug_Buster_problems(id = form.id.data, description = form.description.data, buggyCode = form.buggyCode.data, correctSolution = form.correctSolution.data,  hints = form.hints.data)
        db.session.add(problem)
        db.session.commit()

        flash('New Problem Created..!', 'success')
        return redirect(url_for('home'))
    return render_template('add_bb_problem.html', title='New Subject', form = form, legend='New Subject')



@app.route('/add_cp_problem', methods=['GET','POST'])
@login_required
def add_cp_problem():
    form = Code_Patcher_problems_Form()
    if form.validate_on_submit():
        problem = Code_Patcher_problems(id = form.id.data, question = form.question.data, answer = form.answer.data)
        db.session.add(problem)
        db.session.commit()

        flash('New Problem Created..!', 'success')
        return redirect(url_for('home'))
    return render_template('add_cp_problem.html', title='New Subject', form = form, legend='New Subject')





@app.route('/add_tt_problem', methods=['GET','POST'])
@login_required
def add_tt_problem():
    form = Trainer_Test_problems_Form()
    if form.validate_on_submit():
        problem = Trainer_Test_problems(id = form.id.data, question = form.question.data, option1 = form.option1.data, option2 = form.option2.data, option3 = form.option3.data, option4 = form.option4.data, answer = form.answer.data)
        db.session.add(problem)
        db.session.commit()
        flash('New Problem Created..!', 'success')
        return redirect(url_for('home'))
    return render_template('add_tt_problem.html', title='New Subject', form = form, legend='New Subject')



@app.route('/add_mc_problem', methods=['GET','POST'])
@login_required
def add_mc_problem():
    form = Memory_Card_problems_Form()
    if form.validate_on_submit():
        problem = Memory_Card_problems(id = form.id.data, concept = form.concept.data, description = form.description.data)
        db.session.add(problem)
        db.session.commit()
        flash('New Problem Created..!', 'success')
        return redirect(url_for('add_mc_problem'))
    return render_template('add_mc_problem.html', title='New Subject', form = form, legend='New Subject')






# ........................................... sql -----------------------------------------------------



# @app.route('/bb_data', methods=['GET'])
# def get_bb_data():
#     conn = sqlite3.connect("instance/db.db")  
#     conn.row_factory = sqlite3.Row
    
#     rows = conn.execute('SELECT * FROM bug__buster_problems').fetchall()
#     conn.close()
    
#     data = [dict(row) for row in rows]
#     return jsonify(data)


def get_bb_data():
    if not current_user.is_authenticated:
        return {"error": "User not authenticated"}, 401  # Return an unauthorized response
    conn = sqlite3.connect("instance/db.db")  # Connect to the database
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM user WHERE username = ?", (current_user.username,))  
    rows = cursor.fetchall()
    conn.close()  
    data = [{"username": row[2], "points": row[1]} for row in rows]
    return data


@app.route("/get_users", methods=["GET"])
def get_users():
    result = get_bb_data()
    if isinstance(result, tuple):
        data, status = result
        return jsonify(data), status
    return jsonify(result)





@app.route('/mc_data', methods=['GET'])
def get_data():
    conn = sqlite3.connect("instance/db.db")  # Connect to the database
    conn.row_factory = sqlite3.Row
    # For example, read all rows from a table called 'pairs'
    rows = conn.execute('SELECT * FROM memory__card_problems').fetchall()
    conn.close()
    # Convert the rows to a list of dictionaries.
    data = [dict(row) for row in rows]
    return jsonify(data)


@app.route('/tt_data', methods=['GET'])
def get_tt_data():
    conn = sqlite3.connect("instance/db.db")  # Connect to the database
    conn.row_factory = sqlite3.Row
    # For example, read all rows from a table called 'pairs'
    rows = conn.execute('SELECT * FROM trainer__test_problems').fetchall()
    conn.close()
    # Convert the rows to a list of dictionaries.
    data = [dict(row) for row in rows]
    return jsonify(data)


@app.route('/cp_data', methods=['GET'])
def get_cp_data():
    conn = sqlite3.connect("instance/db.db")  
    conn.row_factory = sqlite3.Row
    
    rows = conn.execute('SELECT * FROM code__patcher_problems').fetchall()
    conn.close()
    
    data = [dict(row) for row in rows]
    return jsonify(data)












# @app.route('/submit_solution', methods=['POST'])
# def submit_solution():
#     data = request.get_json()
#     problem_id = data.get('problem_id')
#     user_code = data.get('user_code', '').strip()

#     # Fetch the correct solution from the database
#     cur = get_db().execute("SELECT correctsolution FROM problems WHERE id = ?", (problem_id,))
#     row = cur.fetchone()
#     cur.close()

#     if row is None:
#         return jsonify({'correct': False, 'message': 'Problem not found!'}), 404

#     correct_solution = row[0].strip()

#     # Compare the submitted code with the correct solution
#     if user_code == correct_solution:
#         return jsonify({'correct': True, 'message': 'Correct solution!'})
#     else:
#         return jsonify({'correct': False, 'message': 'Incorrect solution!'})



















@app.route("/users/<string:username>", methods=["PUT"])
def update_user(username):
    data = request.json  
    new_point = data.get("points")  

    # Ensure points is provided and a valid number
    if new_point is None or not isinstance(new_point, (int, float)):
        return jsonify({"error": "Invalid or missing 'points' field"}), 400  

    conn = sqlite3.connect("instance/db.db")
    cursor = conn.cursor()

    # Check if the user exists
    cursor.execute("SELECT points FROM user WHERE username = ?", (username,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return jsonify({"error": f"User '{username}' not found"}), 404  

    # Update the user's points
    cursor.execute("UPDATE user SET points = ? WHERE username = ?", (new_point, username))
    conn.commit()

    if cursor.rowcount == 0:  # No rows updated
        conn.close()
        return jsonify({"error": "Failed to update points"}), 400  

    conn.close()
    return jsonify({"message": f"Updated {username}'s points to {new_point}"}), 200










if __name__ == "__main__":
    app.run(debug=True)
