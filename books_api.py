from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/books')
def get_books():
    return jsonify([
        {"id": 1, "title": "1984", "author": "George Orwell"},
        {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"},
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
