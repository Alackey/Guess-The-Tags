from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class score(db.Model):
    rank = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)
    score = db.Column(db.Integer, unique=False)

    def __init__(self, rank, username, score):
        self.rank = rank
        self.username = username
        self.score = score


@app.route('/')
def homepage():
    return render_template('base.html')


@app.route('/highscore')
def highscores():
    print("true/false")
    print(request.form)


if __name__ == '__main__':
    app.run()
