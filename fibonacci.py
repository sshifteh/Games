
def fibonacci(numbers):
    numbers = int(numbers)
    a = 0 # initial condition
    b = 1 # initial condition

    clist = []
    for i in range(numbers+1):
        c = a+b
        clist.append(c)

        a = b
        b = c
    return clist

numbers = raw_input('Enter how many Fibonacci numbers you want generated: ')

print fibonacci(numbers)