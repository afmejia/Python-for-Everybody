import socket

url = input("Enter a URL: ")

try:
    words = url.split('/')
    HOST = (words[2])
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    flag = False

    while True:
        data = mysock.recv(512)
        posDoubLine = data.decode().find('\n\n')
        if (len(data) < 1):
            break
        if (not flag and posDoubLine != -1):
            flag = True
            print(data.decode()[posDoubLine + 2:])
        else:
            print(data.decode())
    mysock.close()
except:
    print("Invalid URL")
