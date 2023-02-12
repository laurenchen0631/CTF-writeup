from Crypto.Util import number

p = 861346721469213227608792923571
q = 1157379696919172022755244871343
n = 996905207436360486995498787817606430974884117659908727125853
e = 65537
c = 375444934674551374382922129125976726571564022585495344128269
# p = 976340182462714588322173446187
# q = 851851978002597927023854617077
# n = 831697315634280793856194185305304934314899397816168350735399
# e = 65537
# c = 478373362728019546768290306750946630927700016844426734475521

phi = (p-1)*(q-1)
d = number.inverse((e-1), phi)
print(((e-1)*d)%phi)
print(d)

def fastpow(b, p, mod):
    a = 1
    while p:
        p >>= 1
        b = (b*b)%mod
        if p&1:
            a = (a*b)%mod
    return a


code = number.long_to_bytes(pow(c, d, n))
print(code)
for m in range(1, n):
    k = m + 1
print("end")

# m = pow(c, d, n)
# print(fastpow(m, e, n))
# print(fastpow(m, e, n))