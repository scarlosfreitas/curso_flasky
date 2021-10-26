from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World </h1>'

@app.route('/home', methods=['POST','GET'], defaults={'name':'Default'})
@app.route('/home/<string:name>', methods=['POST','GET'])
def home(name):
    return f'<h1>Hello {name}, você está na home </h1>'

@app.route('/json')
def json():
    return jsonify({'key':'value', 'key2':[1,2,3]})

@app.route('/query')
def query():
    return '<h1>Você está na pagina de query</h1>'

if __name__ == '__main__':
    app.run(debug=True)