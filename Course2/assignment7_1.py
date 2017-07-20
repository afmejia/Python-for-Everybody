try:
    # Prompt file name
    fileName = input('Enter the file name: ')

    # Open the file
    fhandle = open(fileName)

    # Print uppercased lines
    for line in fhandle:
        line = line.rstrip().upper()
        print(line)
except:
    print('Impossible my friend')
