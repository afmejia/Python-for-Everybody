# get handler
fhand = open('mbox.txt')

# Print interesting lines without newline char
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
