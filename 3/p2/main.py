f = open('../input', 'r')

lines = []
for line in f.readlines():
    lines.append(line)
f.close()

def runslope (r, d):
    right = 0 - r
    trees = 0
    for line in lines[::d]: # i didnt know :: existed, very cool!
        right += r
        if line[right % 31] == '#':
            trees += 1
        print (right)
        print (line[right % 31])
    return trees
    # input()

totrees = runslope(1, 1) * runslope(3, 1) * runslope (5, 1) * runslope(7, 1)  * runslope(1, 2)

print(totrees)