from flask import Flask

app = Flask(__name__)

@app.route('/')
def student():
    s = {
        "Name": "Divya",
        "Roll": 43,
        "Class": "TYBSc IT"
    }

    return f"""
    Name: {s['Name']}<br>
    Roll No: {s['Roll']}<br>
    Class: {s['Class']}
    """

if __name__ == '__main__':
    app.run(debug=True)