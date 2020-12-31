#Day 03

with open('./03.txt') as myinput:
    inputlines = myinput.readlines()

claims = [list(map(int, i.strip().replace('#', '').replace('@ ', '').replace(',', ' ').replace(':', '').replace('x', ' ').split())) for i in inputlines]

fabric = [[0 for i in range(1000)] for j in range(1000)]

#Part 1

counter = 0
for claim in claims:
    for i in range(claim[2], claim[2] + claim[4]):
        for j in range(claim[1], claim[1] + claim[3]):
            if fabric[i][j] == 0:
                fabric[i][j] = claim[0]
            elif fabric[i][j] != 'X':
                fabric[i][j] = 'X'
                counter += 1

print(counter)

#Part 2

for claim in claims:
    check = set()
    for i in range(claim[2], claim[2] + claim[4]):
        for j in range(claim[1], claim[1] + claim[3]):
            if fabric[i][j] == claim[0]:
                check.add(1)
            else:
                check.add(0)
    if check == {1}:
        print(claim[0])
        break