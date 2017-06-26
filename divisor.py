



def divisor(number):
    # even number
    if number % 2 == 0:
            while number != 0:
                    return number / 2.
    # odd number
    elif number % 3 == 0:
            while number !=0:
                    return number / 3.
    # prime number
    else:
            return number / number





def main():
        number = float(raw_input("Enter number: "))
        print "The divisors of then number are: %g" % divisor(number)


if __name__ == "__main__":
        main()