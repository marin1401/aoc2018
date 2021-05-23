#Day 08

with open('./08.txt') as myinput:
    tree = list(map(int, myinput.read().split()))

#Part 1

def get_i_and_append_node_meta(i, level):
    for _ in range(nodes[level][-1][2]):
        nodes[level][-1].append(tree[i])
        i += 1
    return i

nodes = {}
i, j, level = 0, 0, 0
while i < len(tree):
    j += 1
    child, meta = tree[i], tree[i+1]
    if level in nodes:
        nodes[level].append([str(j), child, meta])
    else:
        nodes[level] = [[str(j), child, meta]]
    i += 2
    if child:
        level += 1
    else:
        i = get_i_and_append_node_meta(i, level)
        while sum(n[1] for n in nodes[level - 1]) == len(nodes[level]):
            level -= 1
            i = get_i_and_append_node_meta(i, level)
            if level == 0:
                break

print(sum(sum(sum(node[3:]) for node in level_nodes) for level_nodes in nodes.values()))

#Part 2

for level in nodes.keys():
    i = -1
    for node in nodes[level]:
        i += 1
        if not node[1]:
            nodes[level][i] = sum(node[3:])

for level in reversed(list(nodes.keys())):
    i = -1
    offset = 0
    for node in nodes[level]:
        i += 1
        if isinstance(node, list):
            value = 0
            for child in node[3:]:
                if 0 < child <= node[1]:
                    value += nodes[level+1][child+offset-1]
            offset += nodes[level][i][1]
            nodes[level][i] = value

print(nodes[0][0])