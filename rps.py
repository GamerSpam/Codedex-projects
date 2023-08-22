import random as r
from termcolor import colored as c #Adds the ability to change the color of a line

play = True
player = 0

while play == True: #handles playing again
    inv = 1

    while player == 0: #handles bad input
        print('')
        print('=================================')
        print(c("Rock Paper Scissors Lizzard Spock", 'blue'))
        print(c('=================================', 'blue'))
        print('1) ✊')
        print('2) 🤚')
        print('3) ✌️')
        print('4) 🦎')
        print('5) 🖖')

        player = int(input('Pick a number: '))

        print('') #add buffer space
            
        if player > 5 or player < 1: #redirects to top if player inputs invalid input
            print('')
            print(c('Invalid Input', 'red'))
            print('')
            player = 0
        elif player == 1:
            print('You chose ✊')
        elif player == 2:
            print('You chose: 🤚')
        elif player == 3:
            print('You chose: ✌️')
        elif player == 4:
            print('You chose: 🦎')
        else:
            print('You chose: 🖖')
        
        cpu = r.randint(1, 5) #CPU input

        if cpu == 1:
            print('CPU chose: ✊')
        elif cpu == 2:
            print('CPU chose: 🤚')
        elif cpu == 3:
            print('CPU chose: ✌️')
        elif cpu == 4:
            print('CPU chose: 🦎')
        else:
            print('cpu chose: 🖖')

        if player == cpu:
            win = 0 # ties are 0, wins are 1, and losses are 2
        elif player == 1:
            if cpu == 2:
                win = 2 
            elif cpu == 3:
                win = 1
            elif cpu == 4:
                win = 1
            else:
                win = 2
        elif player == 2:
            if cpu == 1:
                win = 1
            elif cpu == 3:
                win = 2
            elif cpu == 4:
                win = 2
            else:
                win = 1
        elif player == 3:
            if cpu == 1:
                win = 2
            elif cpu == 2:
                win = 1
            elif cpu == 4:
                win = 1
            else:
                win = 2
        elif player == 4:
            if cpu == 1:
                win = 2
            elif cpu == 2:
                win = 1
            elif cpu == 3:
                win = 2
            else:
                win = 1
        else:
            if cpu == 1:
                win = 1
            elif cpu == 2:
                win = 2
            elif cpu == 3:
                win = 1
            else:
                win = 2
        
        if win == 1:
            print(c('The player wins!', 'green'))
        elif win == 2:
            print(c('The player loses!', 'red'))
        else:
            print(c("It's a tie", 'blue'))

        print('')


    while inv == 1:
        print('Would you like to play again?')
        print('0) No')
        print('1) Yes')
        usin = int(input())
        if usin != 1 and usin != 0:
            print('')
            print(c('invalid input', 'red'))
            print('')
        else:
            play = bool(usin)
            inv = 0
            player = 0