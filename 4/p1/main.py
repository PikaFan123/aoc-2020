f = open('../input', 'r')

lines = []
for line in f.readlines():
    lines.append(line)
f.close()

passports = []
passportdata = ""

for line in lines:
    if not line.strip():
        passports.append(passportdata)
        passportdata = ""
        continue
    passportdata += line.replace('\n', ' ').replace('\r', '')
    if line == lines[-1]: # ahhhh im stupid
        passports.append(passportdata)
        passportdata = ""


def parseport(passport):
    passdata = passport.strip().split(' ')
    parseddata = {}
    for datapart in passdata:
        dataparts = datapart.split(':')
        parseddata[dataparts[0]] = dataparts[1]
    return parseddata

passdicts = []

for port in passports:
    passdicts.append(parseport(port))

validports = 0

for pport in passdicts:
    print (pport)
    print (pport.keys())
    if len(pport) < 7:
        continue
    if len(pport) < 8 and "cid" in pport:
        continue
    validports += 1


print(validports)