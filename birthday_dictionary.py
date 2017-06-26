



birthday_dictionary = {'Sara': '7/10/1959', 'Petter': '13/10/1992', 'Per': '1959', 'ola': '1/1/1989'}

print '\nWelcome to the birthday dicitonary! We know the birthdays of'
for keys in birthday_dictionary.keys():
        print keys
print ''
key = raw_input('Whose birthday do you want to look up: ')
print '%s has birthday %s' %( key, birthday_dictionary[key])
