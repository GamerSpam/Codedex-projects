# Forty Two lesson from Codedex

import wikipedia as wiki

reslist = wiki.search(input('What do you want to search for?\n'), results = 10, suggestion = False)

print()

for i in reslist:
    print(i)

print()