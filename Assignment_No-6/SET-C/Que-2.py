from flask import Flask

app = Flask(__name__)

@app.route('/')
def students():
    marks = {
        "Divya": 80,
        "Bhumika": 55,
        "Joya": 75,
        "Anisha": 45,
        "Vaiju": 90
    }

    result = "<h2>Students Scoring Above 60</h2>"

    for name, mark in marks.items():
        if mark > 60:
            result += f"{name} : {mark}<br>"

    return result

if __name__ == '__main__':
    app.run(debug=True)