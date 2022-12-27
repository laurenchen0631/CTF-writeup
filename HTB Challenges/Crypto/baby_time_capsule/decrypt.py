import sys
import socket
import libnum
import json
from Crypto.Util.number import long_to_bytes

n = [0, 0, 0]
c = [0, 0, 0]
e = 5

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    [ip, port] = sys.argv[1].split(':')
    s.connect((ip, int(port)))
    for i in range(3):
        s.recv(4096)
        s.send(b'Y')
        data = s.recv(4096)
        data = json.loads(data.decode('utf-8'))
        n[i] = int(data['pubkey'][0], 16)
        c[i] = int(data['time_capsule'], 16)

print(n)
print(c)

res=libnum.solve_crt(c,n)
print(f"\nWe can solved M^e with CRT to get {res}")
val=libnum.nroot(res,e)

print(f"\nDecipher: {long_to_bytes(val)}")