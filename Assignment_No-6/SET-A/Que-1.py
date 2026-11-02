from flask import Flask

app = Flask(__name__)

@app.route('/')
def student():
    name = "Divya"
    marks = [70, 80, 90]

    total = sum(marks)
    average = total / len(marks)

    return f"""
    Student Name: {name}<br>
    Marks: {marks}<br>
    Total: {total}<br>
    Average: {average}
    """

if __name__ == '__main__':
    app.run(debug=True)