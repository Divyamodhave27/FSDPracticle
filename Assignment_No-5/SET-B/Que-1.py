from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        name = request.form['name']
        salary = request.form['salary']
        return "Name: " + name + "<br>Salary: " + salary

    return '''
    <form method="post">
        Name: <input name="name"><br>
        Salary: <input name="salary"><br>
        <input type="submit" value="Submit">
    </form>
    '''

app.run(debug=True)