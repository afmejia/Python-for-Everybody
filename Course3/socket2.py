import socket

url = input("Enter a URL: ")
try:
    words = url.split('/')
    HOST = (words[2])
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    chars = 0
    while True:
        data = mysock.recv(500)
        chars += len(data)
        if (len(data) < 1):
            break
        if (chars > 3000):
            print("limit reached")
            break
        print(data.decode())
    mysock.close()
except:
    print("Invalid URL")
