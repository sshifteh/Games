
import random


random.seed(2)
computer = str(random.randint(1000,9999))
player = raw_input('\nEnter a 4-digit number: ')

guesses = 0

while player != 'exit':

    cows = 0
    bulls = 0

    for i in range(len(computer)):
        if player[i] == computer[i]:
            cows +=1
        elif player[i] in computer:
            bulls +=1
        else:
            pass


    if cows == 4:
        print 'Correct.'
        break

    guesses +=1
    print 'cows: %g, bulls: %g, total number of guesses: %g' %(cows, bulls,guesses)

    player = raw_input('\nGuess a 4-digit number or type exit to quit: ')


