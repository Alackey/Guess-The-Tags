from flask import Flask, render_template
app = Flask(__name__)
import imgur
import random

@app.route('/')
def hello_world():
    image = randImage()
    return render_template('base.html', image=image )
@app.route("/test")   
def randImage():
    image = imgur.getImages()
    print(image)
    i = random.randint(0,10)
    return image[i]
    #return "http://i.imgur.com/Pt6BQNv.png"

if __name__ == '__main__':
    app.run()
