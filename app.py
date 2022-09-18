from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/error')
def error():
    raise ValueError()

if __name__ == '__main__':
    app.run(debug=True)
