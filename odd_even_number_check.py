


def odd_even(number):
    if number % 2 == 0:
        print  '%g is a even number' %number
        if number % 4 == 0:
                print  '%g also a multiple of 4 ' %number
    else:
        print 'odd '



def number_check(number, check):
        if number % check == 0 :
                print  'you number is evenly dived by your check'

        else:
                pass

number = int(raw_input('Enter integer: '))
check =  int(raw_input('Enter check: '))

number_check(number,check)