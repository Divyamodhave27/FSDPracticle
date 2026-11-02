
from flask import Flask, jsonify

app = Flask(__name__)

# GET API
@app.route('/product', methods=['GET'])
def product():
    return jsonify({
        "name": "Laptop",
        "price": 50000,
        "category": "Electronics"
    })

if __name__ == '__main__':
    app.run(debug=True)



    
