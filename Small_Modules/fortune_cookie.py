# Fortune Cookie lesson from Codedex

import random

fortunes = [
    "Don't pursue happiness - create it.",
    "All things are difficult  before they are easy.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "If you eat something and nobody sees you eat it, it has no calories.",
    "Someone in your life needs a letter from you.",
    "Don't just think. Act!",
    "Your heart will skip a beat.",
    "The fortune you search for is in another cookie.",
    "Help! I'm being held prisoner in a Chinese bakery!"
]

def fortune():
    print('') # Blank Space for readability
    print(fortunes[random.randint(0, len(fortunes) - 1)]) # take a random number between 0 and the len of the list - 1 and use it to print the coresponding result

for i in range(0, 3): # runs the function 3 times
    fortune()