
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/student', methods=['GET'])
def student():
    return jsonify({
        "name": "Rahul",
        "course": "BSc IT"
    })

@app.route('/addstudent', methods=['POST'])
def addstudent():
    data = request.get_json()
    return jsonify({
        "name": data['name'],
        "course": data['course']
    })

if __name__ == '__main__':
    app.run(debug=True)




