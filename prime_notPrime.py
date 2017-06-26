

number = int(raw_input('Enter a number: '))
possible_divisors = range(1,number+1)


prime = [i for i in possible_divisors if number % i == 0]
print prime
if len(prime) == 2:
        print 'prime number'
else:
    print 'not prime '