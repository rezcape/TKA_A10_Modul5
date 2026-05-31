from flask import Flask, jsonify
import socket

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 12000000},
    {"id": 2, "name": "Mouse", "price": 150000},
    {"id": 3, "name": "Keyboard", "price": 350000}
]

@app.route('/')
def index():
    hostname = socket.gethostname()
    return jsonify({
        "server": "Server 1 - TokoKita",
        "hostname": hostname,
        "message": "Halo dari Backend 1!"
    })

@app.route('/products')
def products():
    hostname = socket.gethostname()
    return jsonify({
        "server": "Server 1 - TokoKita",
        "hostname": hostname,
        "products": PRODUCTS
    })

@app.route('/catalogue')
def catalogue():
    hostname = socket.gethostname()
    return jsonify({
        "server": "Server 1 - TokoKita",
        "hostname": hostname,
        "products": PRODUCTS
    })

@app.route('/checkout', methods=['POST'])
def checkout():
    import hashlib
    data = b"TokoKitaFlashSaleCheckoutSimulation"
    history = []
    for i in range(1000000):
        data = hashlib.sha256(data).digest()
        if i % 2 == 0:
            history.append(data)
    
    hostname = socket.gethostname()
    return jsonify({
        "server": "Server 1 - TokoKita",
        "hostname": hostname,
        "status": "success",
        "hash": data.hex()
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)