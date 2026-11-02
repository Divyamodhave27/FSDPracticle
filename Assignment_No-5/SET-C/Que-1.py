from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        if name == 'Divya':
            return "Login Successful"
        else:
            return "Invalid Username"

    return '''
    <form method="post">
        Username: <input name="username">
        <input type="submit" value="Login">
    </form>
    '''

app.run(debug=True)

