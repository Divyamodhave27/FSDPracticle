from flask import Flask

app = Flask(__name__)

@app.route('/')
def marks():
    student_marks = [78, 85, 67, 92, 74]

    total = sum(student_marks)
    average = total / len(student_marks)
    highest = max(student_marks)
    lowest = min(student_marks)

    return f"""
    Marks: {student_marks}<br>
    Total: {total}<br>
    Average: {average}<br>
    Highest Marks: {highest}<br>
    Lowest Marks: {lowest}
    """

if __name__ == '__main__':
    app.run(debug=True)
