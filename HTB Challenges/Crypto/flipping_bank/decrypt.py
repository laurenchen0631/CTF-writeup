from pwnlib.tubes.remote import remote
import sys

username = 'admin'
usernameAlt = 'b' + username[1:]
password = 'g0ld3n_b0y'

[ip, port] = sys.argv[1].split(':')
s = remote(ip, port)
s.sendafter(b'username:', usernameAlt)
s.sendafter(b'password:', password)
s.recvuntil(b"Leaked ciphertext: ")
ciphertext = s.recvline().decode().rstrip()

ciphertext = bytearray.fromhex(ciphertext)
block = ciphertext[:16]
flipped = block[0] ^ ord(username[0]) ^ ord(usernameAlt[0])

target = flipped.to_bytes(1, 'big') + block[1:] + ciphertext[16:]

s.sendafter("enter ciphertext: ", target.hex())
data = s.recvall()
print(data)