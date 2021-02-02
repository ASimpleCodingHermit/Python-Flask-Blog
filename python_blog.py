from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
