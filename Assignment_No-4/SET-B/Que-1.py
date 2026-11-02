from flask import Flask

app=Flask(__name__)

@app.route("/Student/<name>")
def Student(name):

    return "Student Name:"+"Divya Rajendra Modhave"


if __name__ == '__main__':
    app.run(debug=True)
