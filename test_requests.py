import json
import requests

url = "http://127.0.0.1:5000/json"

print('''Желаете ли вы поменять информацию?
      1 - да
      0 - нет''')
choose = int(input())

if choose == 1:
    name = input("Введите ваше имя:")
    age = int(input("Введите ваш возраст:"))
    new_data = {"name":name, "age":age}
    temp = open('name.json', 'w').close 
    with open('name.json', 'r+', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False,indent=4)

with open('name.json', 'r', encoding='utf-8') as f:
    file_data = json.load(f)
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, json=file_data, headers=headers)
print(response.text)