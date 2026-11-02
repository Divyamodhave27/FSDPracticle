from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def add():
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return "Addition = " + str(a + b)

app.run(debug=True)
