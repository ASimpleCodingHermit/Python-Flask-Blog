from flask import render_template, url_for, flash, redirect
from pythonblog import app, db, bcrypt
from pythonblog.forms import RegistrationForm, LoginForm
from wtforms.validators import Email
from pythonblog.models import User, Post


posts = [
    {
        'author': 'Joseph Chu',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'January 31, 2020'
    },
    {
        'author': 'Joseph Chu',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'Feburary 15, 2020'
    }
]


@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blogster.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

