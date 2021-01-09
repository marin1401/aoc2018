#Day 05

import string

with open('./05.txt') as myinput:
    polymer = myinput.read()

def reactions(polymer):
    resulting_polymer = ['_', polymer[0]]
    for unit in polymer[1:]:
        if resulting_polymer[-1] != unit and resulting_polymer[-1].lower() == unit.lower():
            resulting_polymer.pop()
        else:
            resulting_polymer.append(unit)
    return len(resulting_polymer) - 1

#Part 1

print(reactions(polymer))

#Part 2

print(min(reactions(polymer.replace(letter, '').replace(letter.upper(), '')) for letter in string.ascii_lowercase))
