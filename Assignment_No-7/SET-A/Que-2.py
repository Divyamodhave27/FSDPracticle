
from flask import Flask, request, jsonify

app = Flask(__name__)

# GET API
@app.route('/employee', methods=['GET'])
def employee():
    return jsonify({
        "name": "Divya",
        "department": "IT"
    })

# POST API
@app.route('/addemployee', methods=['POST'])
def addemployee():
    data = request.get_json()

    return jsonify({
        "name": data['name'],
        "department": data['department']
    })

if __name__ == '__main__':
    app.run(debug=True)


