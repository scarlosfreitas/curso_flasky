from flask import Flask, jsonify, request

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

# http://127.0.0.1:5000/query?name=Carlos&location=Macap%C3%A1
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    
    return f'<h1> Hi {name} você é de {location}. Está na pagina de query</h1>'

@app.route('/theform', methods=['GET','POST'])
def theform():
    if request.method == 'GET':
        return '''<form method="POST" action="/theform">
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="Submit"> 
                </form>
                '''
    else:
        name = request.form['name']
        location = request.form['location']
    
        return f'<h1> Hello {name} você é de {location}. Você submeteu um formulário com sucesso!</h1>'
    
# @app.route('/theform')
# def theform():
#     return '''<form method="POST" action="/process">
#               <input type="text" name="name">
#               <input type="text" name="location">
#               <input type="submit" value="Submit"> 
#               </form>
#               '''

# @app.route('/process', methods=['POST'])
# def process():
    # name = request.form['name']
    # location = request.form['location']
    
#     return f'<h1> Hello {name} você é de {location}. Você submeteu um formulário com sucesso!</h1>'
   
@app.route('/processjson',methods=['POST'])
def processjson():
    
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    
    return jsonify({'result':'Sucess', 'name': name, 'location': location, 'randomkeyinlist':randomlist[1]})
    
if __name__ == '__main__':
    app.run(debug=True)