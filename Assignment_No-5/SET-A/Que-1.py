from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def student():
    name = request.args.get('name')
    return "Student Name: " + name

app.run(debug=True)