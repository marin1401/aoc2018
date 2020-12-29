#Day 01

with open('./01.txt') as myinput:
    inputlines = myinput.readlines()

frequencies = [int(i) for i in inputlines]

#Part 1

print(sum(frequencies))

#Part 2

freq_set = set()
len_frequencies = len(frequencies)
i, j, k, freq = 0, 0, 1, 0
while i == len(freq_set):
    freq += frequencies[j]
    freq_set.add(freq)
    i += 1
    if i // k == len_frequencies:
        j = 0
        k += 1
    else:
        j += 1
    if i - 1 == len(freq_set):
        print(freq)
