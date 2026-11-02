from flask import Flask

app = Flask(__name__)

@app.route('/')
def employee():
    employees = [
        "Divya",
        "Bhumika",
        "Joya",
        "Anisha",
        "Vaiju"
    ]

    result = "<h2>Employee List</h2>"

    for emp in employees:
        result += emp + "<br>"

    return result

if __name__ == '__main__':
    app.run(debug=True)