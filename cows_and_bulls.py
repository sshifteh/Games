
import random



def cows_bulls_game(input):

    random.seed(1)
    generated_number = random.randint(1000,9999)
    generated = str(generated_number)
    print generated

    while input != generated:
        cows = 0
        bulls = 0
        guess = 0

        if input == generated:
            guess += 1
            cows  += 4
            print "Correct guess, Game over"
            return guess, cows, bulls



        else:
            if input[0] == generated[0] \
                or input[1] == generated[1] \
                or input[2] == generated[2] \
                or input[3] ==generated[3]:
                cows +=1


            elif generated[0] or generated[1] or generated[2] or generated[3] in input:
                bulls +=1
            else:
                pass
            guess += 1

            return guess, cows, bulls

            input = str(raw_input("Enter number: "))


def main():
    print " \n Welcome to the Cows and Bulls Game!"
    input = str(raw_input("Enter a number with 4 digits: "))
    print cows_bulls_game(input)


if __name__ == "__main__":
    main()