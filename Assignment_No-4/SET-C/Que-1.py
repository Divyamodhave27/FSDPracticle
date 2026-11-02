from flask import Flask

app=Flask(__name__)

@app.route("/Product/<int:id>")
def Product(id):

    return f" Product ID:{id},Name:Mobile, Price:30000"


if __name__ == '__main__':
    app.run(debug=True)











