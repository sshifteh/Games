import json


birthday_dict = {
    'Shifteh': '02/10/1989',
    'Sima': '06/04/1959'
}
with open('birthdays.json', 'w') as file:
        json.dump(birthday_dict, file)

with open('birthdays.json', 'r') as file:
        dates = json.load(file)


dict = {'Shifteh': {'day': 02, 'month':10, 'year': 1989}, 'Sima': {'day': 02, 'month':10, 'year': 1989}}

