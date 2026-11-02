from flask import Flask, request, render_template, redirect, url_for
import psycopg2
app = Flask(__name__)
def db_connect():
    return psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="divu",
        host="localhost",
        port="5432"
    )
def create_table():
    con = db_connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100) NOT NULL,
            Course VARCHAR(100) NOT NULL,
            Age INTEGER
        )
    """)
    con.commit()
    cur.close()
    con.close()
@app.route("/", methods=["GET", "POST"])
def index():
    con = db_connect()
    cur = con.cursor()
    if request.method == "POST":
        name = request.form.get("Name")
        course = request.form.get("Course")
        age = request.form.get("Age")
        cur.execute(
            "INSERT INTO Student (Name, Course, Age) VALUES (%s, %s, %s)",
            (name, course, age)
        )
        con.commit()
        cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()
    cur.close()
    con.close()
    return render_template("index.html", students=students)
@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit(student_id):
    con = db_connect()
    cur = con.cursor()
    if request.method == "POST":
        name = request.form.get("Name")
        course = request.form.get("Course")
        age = request.form.get("Age")
        cur.execute("""
            UPDATE Student
            SET Name = %s, Course = %s, Age = %s
            WHERE Student_ID = %s
        """, (name, course, age, student_id))
        con.commit()
        cur.close()
        con.close()
        return redirect(url_for("index"))
    cur.execute(
        "SELECT * FROM Student WHERE Student_ID = %s",
        (student_id,)
    )
    student = cur.fetchone()
    cur.close()
    con.close()
    if student is None:
        return "Student not found", 404
    return render_template("edit.html", student=student)
@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id):
    con = db_connect()
    cur = con.cursor()
    cur.execute(
        "DELETE FROM Student WHERE Student_ID = %s",
        (student_id,)
    )
    con.commit()
    cur.close()
    con.close()
    return redirect(url_for("index"))
if __name__ == "__main__":
    create_table()
    app.run(debug=True)
