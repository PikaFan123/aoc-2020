f = open('../input', 'r')

lines = []
for line in f.readlines():
    lines.append(line)
f.close()

right = -3 # this confused me massively
trees = 0
for line in lines:
    right += 3
    if line[right % 31] == '#':
        trees += 1
        
print(trees)
