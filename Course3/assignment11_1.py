import re

def searchRegExp(regExp, fhand):
    count = 0
    for line in fhand:
        line = line.rstrip()
        if re.search(regExp, line):
            count += 1
    return count

# Get a regular expression from user
regExp = input('Enter a regular expression: ')

try:
    # Open the file
    fileName = 'mbox.txt'
    fhand = open(fileName)
    times = searchRegExp(regExp, fhand)
    print(fileName, "had", times, "lines that matched", regExp)
except:
    print('File not found')
