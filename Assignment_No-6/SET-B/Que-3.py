from flask import Flask

app = Flask(__name__)

@app.route('/')
def product():
    products = {
        "Laptop": 75000,
        "Mobile": 30000,
        "Tablet": 27000,
        "TV": 63000
    }

    expensive = max(products, key=products.get)

    return f"""
    Most Expensive Product: {expensive}<br>
    Price: {products[expensive]}
    """

if __name__ == '__main__':
    app.run(debug=True)