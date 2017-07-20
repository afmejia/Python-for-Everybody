try:
    filename = input('Enter a file name: ')
    fhandler = open(filename)

    # Count interesting lines and add the value associated
    total = 0
    count = 0
    for line in fhandler:
        if line.startswith('X-DSPAM-Confidence:'):
            pos = line.find(': ')
            value = float(line[pos + 2:])
            count += 1
            total += value
    av = total / count
    print('Average spam confidence:', av)
except:
    print('Impossible my friend')
