from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume(): 
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/scrabble')
def scrabble():
    return render_template('/projects/scrabble.html')

@app.route('/abyss')
def abyss():
    return render_template('projects/abyss.html')

if __name__ == '__main__':
    app.run(debug=True)
