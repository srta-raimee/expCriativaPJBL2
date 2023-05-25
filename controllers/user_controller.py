import flask as fk
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from models import User

user = fk.Blueprint("user", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@user.route("/login")
def login():
    return redirect(url_for('render.pag_log'))

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@user.route('/login_post', methods=['POST'])
def login_post():
    # login code goes here
    login_info = request.form.get('email')
    password = request.form.get('senha')

    user = User.check_login(login_info)

    if user and user.check_password(password):
        login_user(user)
        return redirect(url_for('render.ret_home'))

    flash('Invalid username or password')
    return redirect(url_for('render.pag_log'))


@user.route('/register_post', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    username = request.form.get("nome", None)
    email = request.form.get("email", None)
    password = request.form.get("senha", None)
    cpf = request.form.get("cpf", None)
    id_role = request.form.get("id_role", None)
    #user = User()
    user = User.check_login2(username, email)
    if user is not None:
        flash('Username or email already used')
    else:
        User.save_user(username, email, password, cpf, id_role)
        flash('Account created successfully!')
    

    return redirect(url_for('render.pag_log'))