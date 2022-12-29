from Crypto.Util.number import inverse, long_to_bytes, GCD
import socket
import sys

pk = [
    
]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    [ip, port] = sys.argv[1].split(':')
    s.connect((ip, int(port)))
    s.recv(4096)
    s.recv(4096)
    s.send(b'4')
    data = s.recv(65535)
    data= data.decode('utf-8').split('\n')
    pk.append(int(data[0].split(':')[1]))
    s.recv(4096)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    [ip, port] = sys.argv[1].split(':')
    s.connect((ip, int(port)))
    s.recv(4096)
    s.recv(4096)
    s.send(b'4')
    data = s.recv(65535)
    data= data.decode('utf-8').split('\n')
    pk.append(int(data[0].split(':')[1]))
    s.recv(4096)

    c = int(data[1].split(':')[1])
    p = GCD(pk[0], pk[1])
    q = pk[1] // p
    n = pk[1]
    phi = (p - 1) * (q - 1)
    e = 65537
    d = inverse(e, phi)
    code = long_to_bytes(pow(c, d, n))
    s.send(code)
    data = s.recv(4096)
    print(data)