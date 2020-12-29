#Day 02

with open('./02.txt') as myinput:
    inputlines = myinput.readlines()

boxes = [i.strip() for i in inputlines]

#Part 1

twice = 0
thrice = 0
for box in boxes:
    appearances = {i: box.count(i) for i in set(box)}
    if 2 in appearances.values():
        twice += 1
    if 3 in appearances.values():
        thrice += 1
        
print(twice * thrice)

#Part 2

def get_common_letters(boxes, len_box):
    common_letters = ''
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            for k in range(len_box):
                if boxes[i][k] == boxes[j][k]:
                    common_letters += boxes[i][k]
            if len(common_letters) + 1 == len_box:
                return common_letters
            else:
                common_letters = ''

print(get_common_letters(boxes, len(boxes[0])))
