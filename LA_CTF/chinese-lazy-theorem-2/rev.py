import libnum
from Crypto.Util.number import long_to_bytes
from pwnlib.tubes.remote import remote


n = [0, 0] #p, q
c = [0, 0]

s = remote('lac.tf', '31111')
n[0] = int(s.recvline())
n[1] = int(s.recvline())

# if p > q:
#     p, q = q, p
print(s.recvuntil(b'>> '))
print(s.sendline(b'1'))
print(s.recvuntil(b': '))
s.sendline(str(n[0]).encode())
c[0] = int(s.recvline())
print(s.recvuntil(b'>> '))
print(s.sendline(b'1'))
print(s.recvuntil(b': '))
s.sendline(str(n[1]).encode())
c[1] = int(s.recvline())

print(s.recvuntil(b'>> '))
print(s.sendline(b'2'))
x = libnum.solve_crt(c, n)
for i in range(30):
    print(s.recvuntil(b': '))
    z = i * n[0] * n[1] + x
    s.sendline(str(z).encode())
    print(s.recvline())

# s.sendafter('>> ', '1', 2000)