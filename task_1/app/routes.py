from flask import Flask, request
import json


app = Flask(__name__)

@app.route('/')
def hello():
    return '''
HELLO!
</br><a href = /login/f1lzEr0>Логин</a>
</br><a href = /multiply/4/2>Умножение</a>
</br><a href = /square/6>Квадрат</a>
</br><a href = /json>json приветствие</a>'''

@app.route('/login/<username>')
def personal_hello(username):
    return f"Hello {username}"

@app.route('/square/<int:num>')
def square(num):
    num = int(num)
    return f"{num**2}"

@app.route('/multiply/<a>/<b>', methods = ['GET'])
def get_multiply(a,b):
    a = int(a)
    b = int(b)
    return f"{a*b}"

@app.route('/json', methods = ['POST', 'GET'])
def input_json():
    if request.method == 'POST':
        data = request.get_json()
        name = data['name']
        age = data['age']
        temp = open("data.json", 'w').close
        with open("data.json", "r+", encoding= "UTF-8") as file:
            json.dump(data,file, ensure_ascii=False,indent=4)
        return f'Привет {name}, твой возраст {age}'
    if request.method == 'GET':
        try:
            with open("data.json", encoding= "UTF-8") as file:
                prev_data = json.load(file)
                return f'Предыдущее приветствие: </br>Привет {prev_data['name']}, твой возраст {prev_data['age']}'
        except:
            return 'Для получения информации отправьте post запрос'