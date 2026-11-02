from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def area():
    if request.method == 'POST':
        l = int(request.form['length'])
        b = int(request.form['breadth'])
        return "Area = " + str(l * b)

    return '''
    <form method="post">
        Length: <input name="length"><br>
        Breadth: <input name="breadth"><br>
        <input type="submit" value="Calculate">
    </form>
    '''

app.run(debug=True)