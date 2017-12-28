import re

def computeAvg(fhand):
    count = 0.0
    prom = 0.0
    for line in fhand:
        line = line.rstrip()
        val = re.findall('^New Revision: ([0-9]+)', line)
        if len(val) > 0:
            count += 1.0
            prom += float(val[0])
    return prom / count

# Open the file
fileName = 'mbox.txt'
try:
    fhand = open(fileName)
    avg = computeAvg(fhand)
    print (avg)
except:
    print('File not found!')
