from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
CORS(app)

# デフォルト
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

# '/rand'が叩かれた時、乱数を生成
@app.route('/rand')
def random_test():
    response = {
        'randomNum': random.random()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)