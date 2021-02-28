from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/payment', methods=['POST'])
def payment():
    return jsonify({'orderID': 'orderID'})


if __name__ == '__main__':
    app.run(debug=True)
