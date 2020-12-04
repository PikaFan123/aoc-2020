import re

f = open('../input', 'r')

lines = []
for line in f.readlines():
    lines.append(line)
f.close()

passports = []
passportdata = ""

regexes = {
    'byr': re.compile(r'[0-9]{4}'),
    'iyr': re.compile(r'[0-9]{4}'),
    'eyr': re.compile(r'[0-9]{4}'),
    'hgt': re.compile(r'[0-9]*(cm|in)'),
    'hcl': re.compile(r'#[0-9a-f]{6}'),
    'ecl': re.compile(r'amb|blu|brn|gry|grn|hzl|oth')
}

for line in lines:
    if not line.strip():
        passports.append(passportdata)
        passportdata = ""
        continue
    passportdata += line.replace('\n', ' ').replace('\r', '')
    if line == lines[-1]: 
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

def validate(port): # this is not elegant at all, so many nested ifs, but it works! i guess
    for key, value in port.items():
        if key == 'cid':
            continue
        if key == 'byr':
            if regexes[key].match(value) is not None:
                if not 1920 <= int(value) <= 2002:
                    return False
            else:
                return False
        if key == 'iyr':
            if regexes[key].match(value) is not None:
                if not 2010 <= int(value) <= 2020:
                    return False
            else:
                return False
        if key == 'eyr':
            if regexes[key].match(value) is not None:
                if not 2020 <= int(value) <= 2030:
                    return False
            else:
                return False
        if key == 'hgt':
            if regexes[key].match(value) is not None:
                if 'in' in value:
                    if not 59 <= int(value[:-2]) <= 76:
                        return False
                if 'cm' in value:
                    if not 150 <= int(value[:-2]) <= 193:
                        return False
            else:
                return False
        if key == 'hcl':
            if regexes[key].match(value) is None:
                return False
        if key == 'ecl':
            if regexes[key].match(value) is None:
                return False
        if key == 'pid':
            if len(value) is not 9:
                return False
    return True

for pport in passdicts:
    print (pport)
    print (pport.keys())
    if len(pport) < 7:
        continue
    if len(pport) < 8 and "cid" in pport:
        continue
    if not validate(pport):
        continue
    validports += 1

print(validports)