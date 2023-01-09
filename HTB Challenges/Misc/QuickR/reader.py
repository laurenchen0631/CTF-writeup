from pwnlib.tubes.remote import remote
import sys
from PIL import ImageGrab, Image
from pyzbar.pyzbar import decode

[ip, port] = sys.argv[1].split(':')
s = remote(ip, port)

s.recvuntil(b'you got only 3 seconds')
data = s.recvuntil(b'\t\n').decode()
print(data)

screenshot = ImageGrab.grab()
screenshot.save('qrcode.bmp', 'bmp')
qrcode = decode(Image.open('qrcode.bmp'))
expr = qrcode[0].data.decode()
expr = expr.replace('x', '*').replace('=', '')

v = str(eval(expr))

data = s.recvline()
print(data)
data = s.recvline()
print(data)
s.sendline(str(v).encode())
data = s.recvall()
print(data)

