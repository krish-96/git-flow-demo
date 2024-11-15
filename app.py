from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return "End Point1"


@app.route('/api-1', methods=['GET'])
def end_point1():
    return "End Point1"


@app.route('/api-2', methods=['GET'])
def end_point2():
    return "End Point1"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5115, debug=False, use_reloader=False)
