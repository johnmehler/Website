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

@app.route('/Temp')
def Temp():
    return render_template('Temp.html')

if __name__ == '__main__':
    app.run(debug=True)
