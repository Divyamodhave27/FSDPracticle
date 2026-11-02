from flask import Flask

app=Flask(__name__)

@app.route("/Square/<int:num>")
def Square(num):

    return str(num*num)


if __name__ == '__main__':
    app.run(debug=True)











