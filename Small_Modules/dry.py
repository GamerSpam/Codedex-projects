# D.R.Y Lesson from Codedex

import random

randlist = [] # Make the empty list that we will fill with random numbers
inp = 'not a num'

# Make a random list that I will use in a function later
for i in range(1,11):
    randlist.append(random.randint(1, 25))

# input function. This function works by raising an "auditing event" called builtins.input and creats a prompt before it reads any input
# The function will then read a line from the input and convert it to a string and returns that as the output of the function

inp = input('Please enter a number: ') # in short this reads user input

while inp.isnumeric() != True: # handles non-number inputs
    inp = input('Please enter a valid number: ')

# int() function takes the value of the arg and converts it to an integer. If it is a string it will allow only numbers with no spaces, or letters depending on the 'base' being used

num = int(inp)

randlist.append(num) # This is not in the list on the site, but it takes the input value and stores it to the end of the list

# The sum function adds all values starting from the left

total = sum(randlist)

# Print function converts args to string and then if no method is defined uses "sys.stdout"

print(total)

# len() function returns the length of an object (in this case a list)

print(len(randlist))