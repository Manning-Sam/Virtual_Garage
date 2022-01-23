from flask import Blueprint, redirect, render_template, request,url_for,flash,session
from .forms import LoginForm, UserInfoForm
from car_inventory.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user


from car_inventory.authentication.forms import UserInfoForm


authentication = Blueprint('authentication', __name__, template_folder = 'auth_templates')

@authentication.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User(username,email,password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('site.profile'))
    return render_template('signup.html', form = form)

@authentication.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = LoginForm()
    try:
        if request.method == 'POST' and form.validate():
            email = form.email.data
            password = form.password.data
            session["email"] = form.email.data


            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('Login successful!', 'auth-success')
                return redirect(url_for('site.profile'))

            else:
                flash('your username and/or password is incorrect', 'auth-failed')
                return redirect(url_for('authentication.login'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form.')

        user = User(email,password)
        
        return redirect(url_for('site.profile'))
    return render_template('signin.html', form = form)