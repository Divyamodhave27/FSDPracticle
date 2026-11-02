from flask import Flask

app = Flask(__name__)

@app.route('/')
def employee():
    employees = [
        ["101", "Divya", "Manager"],
        ["102", "Bhumika", "HR"],
        ["103", "Joya", "Developer"]
    ]

    result = "<h2>Employee Details</h2>"

    for emp in employees:
        result += f"ID: {emp[0]}, Name: {emp[1]}, Designation: {emp[2]}<br>"

    return result

if __name__ == '__main__':
    app.run(debug=True)