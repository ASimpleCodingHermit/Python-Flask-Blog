from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from wtforms.validators import Email
app = Flask(__name__)

app.config['SECRET_KEY'] = '1b259870436a179cf073be94cfb612f5'

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
        flash('Account created!', 'success')
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


if __name__ == '__main__':
    app.run(debug=True)
