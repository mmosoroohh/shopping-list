from flask import Flask, render_template, url_for, session, request, redirect, flash
from app import app,user

from functools import wraps
import uuid

shopping_list = user.shopping_list
User = user.User
type_of_list = user.type_of_list

user_list =[]
current_user = {}

# Checks if the user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if bool(current_user) is False:           
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
    

#Home
@app.route('/')
def home():
    session['show'] = True
    return render_template("home.html")
#login   
@app.route('/login', methods=['GET', 'POST'])
def login():
    session['show'] = False
    message = None

    if request.method == 'POST':
        if request.form['email'] == '' or request.form['password'] == '' or request.form['email'].isspace() or request.form['password'].isspace():
            message = "Email and Password Fields Required!"
            return render_template("login.html", message = message)
        elif not check_mail(request.form['email']):
            message = "Enter a valid email address!"
            return render_template("login.html", message = message)
        else:
            if len(user_list) > 0:
                for user in user_list:
                    if user.email == request.form['email'] and user.password == request.form['password']:
                        session['logged_in'] = True
                        current_user['email'] = user.email
                        current_user['dashboard'] = user.dashboard
                        current_user['edit'] = user.edit
                        current_user['view'] = user.view
                        current_user['add_list'] = user.add_list
                        return redirect(url_for('home'))

                    message = "Username and Password incorrect!"
                session['logged_in'] = False
                return render_template("login.html", message = message)
            else:
                message = "User not available! Please register..."
                return render_template("register.html", message = message)

    return render_template("login.html")
#logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out')
    return redirect(url_for('login'))
#register
@app.route('/register', methods=['GET', 'POST'])
def register():
    session['show'] = False
    message = None

    if request.method == 'POST':
        if not request.form['password'] or request.form['password'] == "" or request.form['password'].isspace():
            message = "Password is Required!"
        elif request.form['name'] == "" or request.form['name'].isspace():
            message = "Name cannot be an empty field!"
        elif not check_mail(request.form['email']) or request.form['email'] == "":
            message = "Email provided is not correct!"
        else:
            for user in user_list:
                if user.email == request.form['email']:
                    message = "User with provided email already exists!"
                    return render_template("register.html", error=message)

                new_user = User(request.form['name'], request.form['email'], request.form['password'])
                user_list.append(new_user)

                if new_user:
                    return redirect(url_for('login'))
                else:
                    return render_template("register.html", error=message)
                    
    return render_template("register.html")
 
#dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")


#Add shopping list
@app.route('/add_list')
@login_required
def add_list():
   return render_template("add_list.html")


@app.route('/view')
@login_required
def view():
    return render_template("view.html")

@app.route('/edit')
@login_required
def edit():
    return render_template("edit.html")

@app.route('/delete')
@login_required
def delete():
    return redirect(url_for("dashboard"))


def check_mail(user_email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', user_email)

    if match == None:
        return False
    else:
        return True