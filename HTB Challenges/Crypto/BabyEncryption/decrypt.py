mapping = {}
for i in range(256):
    mapping[(123 * i + 18) % 256] = i

with open('./msg.enc','r') as f:
    for e in f:
        b = bytearray.fromhex(e)
        chars = []
        for c in b:
            chars.append(chr(mapping[c]))
        print(''.join(chars))