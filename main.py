from flask import Flask, render_template
app = Flask(__name__)
import imgur
import clarafai
@app.route('/')
def hello_world():
    image = randImage()
    return render_template('base.html', image=image )
    
def randImage():
    URLArray = imgur.getImages()
    imageURL = URLArray[0]
    return imageURL

if __name__ == '__main__':
    app.run()
