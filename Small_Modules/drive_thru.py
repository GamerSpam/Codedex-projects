# Drive-Thru lesson from Codedex

from termcolor import colored as c

item = [ # list of items on the menu
    '🍔 Cheeseburger',
    '🍟 Fries',
    '🥤 Soda',
    '🍦 Ice Cream',
    '🍪 Cookie',
    '🥡 End Order'
]

order = [] # make an empty list to append the order to

def get_item(a): # pulls the item from the list and returns it's value
    return item[a - 1]

def welcome(): # prints out the menu options
    print(c('Welcome to the drive thru', 'yellow'))
    print(c('The menu options are:\n', 'yellow'))
    n = 0
    for i in item:
        n += 1
        print(c(f'{n}) {i}', 'blue'))
    print()

def end_order(): # prints out what was orderd and wishes the user a nice day.
    if order:
        print(c('\nYou ordered:', 'blue'))
        for i in order:
            print(c(i, 'green'))
    else:
        print(c('You orderd nothing.', 'red'))
    print(c('Have a great day!', 'green'))
    exit()

def main(): # Takes in the input an passes it to get_item() and appends the results to the list.
    while True: # retry input until user makes a proper selection
        try:
            inp = int(input("Make a selection (1-6): "))
            if inp >= 1 and inp <= 5:
                order.append(get_item(inp))
                break
            elif inp == 6:
                break
            else:
                raise ValueError # calls error if input is out of range
        except ValueError:
            print(c('Invalid Input\nPlease enter a number (1-6)', 'red'))
    if inp != 6:
        print(c(f'You selected: {get_item(inp)}', 'green'))
        main() # Loops back to main()
    else:
        end_order()

welcome()
main()
