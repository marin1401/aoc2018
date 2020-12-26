#Day 01

with open('./01.txt') as myinput:
    inputlines = myinput.readlines()

frequencies = [int(i) for i in inputlines]

#Part 1

print(sum(frequencies))

#Part 2

freq_set = set()
i = 0
j = 0
k = 1
freq = 0
while i == len(freq_set):
    freq += frequencies[j]
    freq_set.add(freq)
    i += 1
    if i // k == len(frequencies):
        j = 0
        k += 1
    else:
        j += 1
    if i - 1 == len(freq_set):
        print(freq)