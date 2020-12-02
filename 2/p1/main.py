f = open('../input', 'r')

lines = []
for line in f.readlines():
    lines.append(line)
f.close()

valid = 0

for entry in lines:
    plpair = entry.split(':')
    policy = plpair[0]
    pwi = plpair[1].strip()
    polinf = policy.split(' ')
    polnums = polinf[0].split('-')
    num1 = int(polnums[0])
    num2 = int(polnums[1])
    polchar = polinf[1]
    charinpw = pwi.count(polchar)
    if num1 > charinpw:
        continue
    if num2 < charinpw:
        continue
    valid += 1
    

print(valid)
