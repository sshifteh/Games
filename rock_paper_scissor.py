


import re
import random


def game1():
    player = raw_input("Enter rock, paper or scissor or enter to quit: ")

    player_score = 0
    pc_score = 0
    rounds = 0

    while player != 'enter':
        computer = random.choice(["rock", "paper", "scissor"])
        print "\nComputer: ", computer
        print "You: ", player


        if player == computer:
                player_score +=1
                pc_score += 1
                rounds += 1
                print "Its a draw "


        elif player == 'rock' and computer == 'paper':
                pc_score += 1
                rounds += 1
                print " Computer won, you lost this round"

        elif player == 'paper' and computer == "scissor":
                pc_score +=1
                rounds += 1
                print "Computer won, you lost this round"


        elif player == 'scissor' and computer == "rock":
                pc_score +=1
                rounds += 1
                print " Computer won, you lost this round"


        elif player == 'paper' and computer == 'rock':
                player_score +=1
                rounds += 1
                print " You won, computer lost this round"

        elif player == 'scissor' and computer == 'paper':
                player_score +=1
                rounds += 1
                print " You won, computer lost this round"


        elif player == 'rock' and computer == 'scissor':
                player_score +=1
                rounds += 1
                print " You won, computer lost this round"
        else:
                break
        player = raw_input("\nEnter rock, paper or scissor or enter to quit: ")

    return "You won %g rounds while computer won %g rounds. Out of a total of %g rounds." %(player_score, pc_score, rounds)








def game2():
        player = raw_input("\nEnter rock, paper or scissor or enter to quit: ")

        while player != 'enter':
                computer = random.choice(['rock', 'paper', 'scissor'])
                print 'Computer: ', computer
                print 'You:', player

                if player == computer:
                        print "It's a tie"

                elif player.lower() == 'rock':
                        if computer == 'scissor':
                            print 'player wins'
                        else:
                            print 'computer wins'

                elif player.lower() == 'scissor':
                        if computer == 'rock':
                                print 'computer wins'
                        else:
                                print 'player wins'

                elif player.lower() == 'paper':
                            if computer == 'rock':
                                    print 'player wins'
                            else:
                                    print 'computer wins'

                else:
                        return "Invalid input"
                        sys.exit()

                player = raw_input("\nEnter rock, paper or scissor to play or enter to quit: ")



def game3():

    while True:
            game_points = {'rock': 1, 'scissor':2, 'paper':3}
            computer = random.choice(['rock', 'paper', 'scissor'])
            player = raw_input('\nEnter rock, paper, or scissor: ')

            print '\nComputer:', computer
            print 'You:', player
            # to get the point corresponding to the choice of 'tool' i.e. rock, paper...
            p = game_points.get(player)
            c = game_points.get(computer)
            difference = p - c

            if difference in [-1,2]:
                    print '\nYou won. Computer lost.'
                    keep_going = raw_input('keep going? enter yes or no: ')
                    if keep_going.lower() == 'yes':
                        continue
                    else:
                        print '\nGame over.Bye.'
                        break

            elif difference in [1,-2]:
                    print '\nComputer won. You lost.'
                    keep_going = raw_input('keep going? enter yes or no: ')
                    if keep_going.lower() == 'yes':
                            continue
                    else:
                        print '\nGame over.Bye.\n'
                        break
            else:
                    print 'It is a tie'



def main():

    play = raw_input("\nDo you want to play rock - paper -scissor (yes/no): ")

    if play.lower() == "yes":
            game3()

    if play.lower() == "no":
            print "Bye"

main()