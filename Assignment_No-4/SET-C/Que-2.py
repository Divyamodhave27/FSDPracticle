from flask import Flask

app = Flask(__name__)

@app.route('/employee/<name>')
def employee(name):
    return "Welcome " + name

app.run(debug=True)