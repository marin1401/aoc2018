#Day 09

from collections import deque

with open('./09.txt') as my_input:
    players, marbles = map(int, my_input.read().split()[0::6])

def marble_game(players, marbles):
    scores = {k: 0 for k in range(1, players + 1)}
    circle = deque([0])
    for marble in range(1, marbles + 1):
        current_player = (marble - 1) % players + 1
        if marble % 23:
            circle.rotate(-1)
            circle.append(marble)
        else:
            circle.rotate(7)
            scores[current_player] += marble + circle.pop()
            circle.rotate(-1)
    return max(scores.values())

#Part 1

print(marble_game(players, marbles))

#Part 2

print(marble_game(players, marbles*100))
