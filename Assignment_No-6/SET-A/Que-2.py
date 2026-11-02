from flask import Flask

app = Flask(__name__)

@app.route('/')
def students():
    names = ["Divya", "Bhumika", "Joya", "Anisha", "Vaiju"]

    result = "<h2>Student Names</h2>"
    for name in names:
        result += name + "<br>"

    return result

if __name__ == '__main__':
    app.run(debug=True)