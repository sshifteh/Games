


def divisor(number):
        divisors = []
        numbers = range(1,number+1)
        number = float(number)
        for i in numbers:
                if number % i == 0:
                        divisors.append(i)

        return divisors

def prime(number,divisors):
    if len(divisors) == 2:
            return "prime"
    else:
            return "not prime"

def main():
        number = raw_input("\n Enter a number: ")
        divisors = divisor(int(number))
        print prime(number, divisors)


if __name__ == "__main__":
        main()