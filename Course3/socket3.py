import urllib.request

try:
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    chars = 0
    for line in fhand:
        chars += len(line)
        if (chars > 3000):
            break
        print(line.decode().strip())
    print(chars)
except:
    print("Server not found!")
