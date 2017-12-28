import re

def sumNumber(fhand):
    total = 0
    for line in fhand:
        line = line.rstrip()
        x = re.findall('[0-9]+', line)
        if len(x) > 0:
            for number in x:
                total += int(number)
    return total

fileName = 'regex_sum_2558.txt'
try:
    fhan = open(fileName)
    sumN = sumNumber(fhan)
    print(sumN)
except:
    print("File not found!")
