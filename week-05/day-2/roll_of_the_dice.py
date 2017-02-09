#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import random

min = 1
max = 6

yes = 'y'
no = 'n'

dice = random.randint(min, max)

user_input = input('Welcome to Hell! Press Y to roll, or N to leave!')

while user_input != no:
    if user_input == yes:
        dice = random.randint(min, max)
    print('You rolled', dice)
    user_input = input('Roll again?')
    if user_input == no:
        print ('Satan bless you!') and exit
