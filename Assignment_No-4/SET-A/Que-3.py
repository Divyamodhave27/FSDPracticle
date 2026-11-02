from flask import Flask

app=Flask(__name__)

@app.route("/course/<string:name>")
def course_info(name):

    return f"""
<P>{name}</p>
<p>"Welcome to the course!"</p>
   """

if __name__ == '__main__':
    app.run(debug=True)
