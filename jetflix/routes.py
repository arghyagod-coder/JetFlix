from flask import redirect, url_for, flash
from jetflix import app, render_template, db, bcrypt
from flask_login import login_user, logout_user, login_required
from jetflix.forms import RegisterForm, LoginForm
from jetflix.models import User
from jetflix.tmdb import MvFm

@app.route("/")
def landing_page():
    return render_template('landing.html')

@app.route('/home')
def home_page():
    return render_template('home.html', mvfm=MvFm())

@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(form.data)
        password_hash = bcrypt.generate_password_hash(form.password1.data).decode("utf-8")
        usertc = User(
            username=form.username.data,
            email_address=form.email.data,
            password_hash=password_hash
            )
        db.session.add(usertc)
        db.session.commit()
        login_user(usertc)
        flash(f'Your account was successfully registered. You are now logged in as {usertc.username}', 'success')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error creating user:{err_msg}", category="danger")

    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f"Success!! You are logged in as: {attempted_user.username}", category="success")
            return redirect(url_for('home_page'))
        else:
            flash("Username or Password Invalid. Access Denied", category="danger")
    return render_template('login.html', form=form)