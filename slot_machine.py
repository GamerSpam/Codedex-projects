# Slot Machine lesson form Codedex

import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
    results = random.choices(symbols, k = 3)

    print(f'{results[0]}  | {results[1]}  | {results[2]}')

    if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
        print(f'\u001b[32mJackpot 💰')

    while True:
        try:
            pa = input(f'\u001b[37mKeep Playing? (Y/N)\n')
            if pa.upper() == 'Y':
                play()
            elif pa.upper() == 'N':
                print(f'\u001b[37mThanks for playing')
                exit()
            else:
                raise ValueError
        except ValueError:
            print(f'\u001b[31mInvalid Input\u001b[37m')
play()