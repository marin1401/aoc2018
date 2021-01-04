#Day 04

with open('./04.txt') as myinput:
    inputlines = myinput.readlines()

sorted_inputlines = sorted(inputlines)

sleep_records = {}
for current_line, next_line in zip(sorted_inputlines[:-1], sorted_inputlines[1:]):
    current_line = current_line.split()
    next_line = next_line.split()
    if current_line[2] == 'Guard':
        key = (next_line[0][-5:], int(current_line[3][1:]))
        sleep_records[key] = [0 for i in range(60)]
        continue
    if current_line[2] == 'falls':
        for i in range(int(current_line[1][-3:-1]), int(next_line[1][-3:-1])):
            sleep_records[key][i] = 1

sleep_sum = {}
for k, v in sleep_records.items():
    if k[1] not in sleep_sum.keys():
        sleep_sum[k[1]] = v
    else:
        for i in range(60):
            sleep_sum[k[1]][i] += v[i]

sleep_highscore = {k: (sum(v), v.index(max(v))) for k, v in sleep_sum.items()}

#Part 1

print(next(k * v[1] for k, v in sleep_highscore.items() if v[0] == max(sleep_highscore.values())[0]))

#Part 2

print(next(k * v.index(max(v)) for k, v in sleep_sum.items() if max(max(i) for i in sleep_sum.values()) in v))
