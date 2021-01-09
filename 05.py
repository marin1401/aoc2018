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

polymer_lengths = set()
for letter in string.ascii_lowercase:
    polymer_lengths.add(reactions(polymer.replace(letter, '').replace(letter.upper(), '')))

print(min(polymer_lengths))