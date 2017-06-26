



birthday_dictionary = {'Sima': '02/05/1959', 'Pedram': '22/10/1992', 'Reza': '1959', 'Lars': '29/03/1989'}

print '\nWelcome to the birthday dicitonary! We know the birthdays of'
for keys in birthday_dictionary.keys():
        print keys
print ''
key = raw_input('Whose birthday do you want to look up: ')
print '%s has birthday %s' %( key, birthday_dictionary[key])