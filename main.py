from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import imgur
import clarifaiapp
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/scores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, primary_key=False)
    username = db.Column(db.String(80), unique=False)
    score = db.Column(db.Integer, unique=False)

    def __init__(self, rank, username, score):
        self.rank = rank
        self.username = username
        self.score = score
'''
    def __repr__(self):
        return '<Rank {0}   Score {1}'.format(self.rank, self.score)
'''
@app.route('/test')   
def randImage():
    image = imgur.getImages()
    print(image)
    
    i = random.randint(0,10)
    print(image[i])
    tags = clarifaiapp.getTags(str(image[i]))
    print(tags)
    return image[i]


@app.route('/')
def homepage():
    return render_template('home page.html')


@app.route('/scores')
def scores():
    return render_template('scores.html')


@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/highscore', methods=['POST'])
def highscore():
    scores = score.query.all()

    playerScore = int(request.form.getlist('score')[0])
    playerUsername = request.form.getlist('username')[0]
    lastElem = ""

    scoreLength = len(scores)
    for e in reversed(scores):
        lastElem = e
        break

    if lastElem.score > playerScore:
        return 'False'
    else:
        first = True
        for s in scores:
            if s.score <= playerScore:
                if first:
                    highest = s
                    first = False
                else:
                    if s.score > highest.score:
                        highest = s
                s.rank += 1
        player = score((highest.rank - 1), playerUsername, playerScore)
        db.session.add(player)
    db.session.commit()

    return 'True'


if __name__ == '__main__':
    app.run(debug=True)
