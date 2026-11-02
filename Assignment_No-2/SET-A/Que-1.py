from flask import Flask, request
app=Flask(__name__)

@app.route("/Student",methods=["GET"])
def student():
    return "Student details received using GET request."

if __name__ =="__main__":
    app.run(debug=True)