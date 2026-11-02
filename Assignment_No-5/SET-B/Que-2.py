from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        return request.form['name'] + "<br>" + request.form['rating'] + "<br>" + request.form['comments']

    return '''
    <form method="post">
        Name: <input name="name"><br>
        Rating: <input name="rating"><br>
        Comments: <input name="comments"><br>
        <input type="submit">
    </form>
    '''

app.run(debug=True)