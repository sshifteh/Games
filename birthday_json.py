import json


birthday_dict = {
    'Shifteh': '12/11/1990',
    'Sarah': '06/04/1965'
}
with open('birthdays.json', 'w') as file:
        json.dump(birthday_dict, file)

with open('birthdays.json', 'r') as file:
        dates = json.load(file)


dict = {'Shifteh': {'day': 12, 'month':11, 'year': 1990}, 'Sarah': {'day': 06, 'month':04, 'year': 1965}}

