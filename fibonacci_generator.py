


def fibonacci_sequence_generator(n):
        temp = 0
        b = 1
        for i in range(n):
                ny = temp + b
                print ny
                temp = b
                b = ny

n = int(raw_input("Enter numbers of Fib numbers you want generated: "))
fibonacci_sequence_generator(n)