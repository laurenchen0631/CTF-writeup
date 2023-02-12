from Crypto.Util import number

def fastpow(b, p, mod):
    a = 1
    while p:
        p >>= 1
        b = (b*b)%mod
        if p&1:
            a = (a*b)%mod
    return a

print(fastpow(2, (2**3+1), 100000))
print(pow(2, 9))

p = number.getPrime(100)
q = number.getPrime(100)
n = p*q
e = 65537
m = int.from_bytes(b"test", 'big')
c = fastpow(m, e, n)


print("p =", p)
print("q =", q)
print("n =", n)
print("e =", e)
print("c =", c)
print(pow(m, e-1, n))
print(pow(m, e, n))
print((fastpow(m, e, n) * m) % n)
# print("m =", m)