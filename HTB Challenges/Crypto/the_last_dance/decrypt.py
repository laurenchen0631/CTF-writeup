""" 
https://loup-vaillant.fr/tutorials/chacha20-design
https://www.javainterviewpoint.com/chacha20-poly1305-encryption-and-decryption/
https://www.nwcodex.com/one-time-pads-and-stream-cipher-vulnerabilities
"""

iv = bytes.fromhex("c4a66edfe80227b4fa24d431")

e = bytes.fromhex("7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990")

m = "Our counter agencies have intercepted your messages and a lot of your agent's identities have been exposed. In a matter of days all of them will be captured"

flag_e = bytes.fromhex("7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7")

def xor(a, b, c):
    return bytes([_a ^ _b ^ _c for _a, _b, _c in zip(a, b, c)])

print(xor(flag_e, e[:len(flag_e)], m.encode('utf-8')[:len(flag_e)]))
