from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    result = ""

    if request.method == "POST":
        name = request.form["name"]
        result = "Search Result: " + name

    return '''
        <h1>Student Search</h1>

        <form method="POST">
            Student Name:
            <input type="text" name="name">
            <input type="submit" value="Search">
        </form>

        <h3>''' + result + '''</h3>
    '''

app.run(debug=True)