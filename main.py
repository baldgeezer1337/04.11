import json

try:
    with open('user_data.json', 'r', encoding='utf-8') as file:
        people = json.load(file)
except FileNotFoundError:
    people=[]

while True:
    name=input('Ievadi vardu: ')
    age=input('Ievadi vecumu: ')
    city=input('Ievadi pilsetu: ')

    people.append({
        'name':name,
        'age': age,
        'city':city
    })

    another=input('Vai velies pievienot val vienu cilveku? (ja/ne)').strip().lower()
    if another !='ja':
        break

with open('user_data.json', 'w', encoding='utf-8') as file:
    json.dump(people,file,indent=4)

print('Dati ir saglabati json faila')