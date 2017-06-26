

number = int(raw_input('Enter number: '))

possible_divisor = range(1,number+1)
# divisors divide evenly into a number
divisors = []
for i in possible_divisor:
        if number % i == 0:
             divisors.append(i)

print divisors