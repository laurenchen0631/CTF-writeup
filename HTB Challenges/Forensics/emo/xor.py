
data = [
   182, 187, 229, 146, 231, 177, 151, 149, 166, 186, 141, 228, 182, 177, 171, 229, 236, 239, 239, 239, 228, 181, 182, 171, 229, 234, 239, 239, 228, 185, 179, 190, 184, 229, 151, 139, 157, 164, 235, 177, 239, 171, 183, 236, 141, 128, 187, 235, 134, 128, 158, 177, 176, 139, 183, 154, 173, 128, 175, 151, 238, 140, 183, 162, 228, 170, 173, 179, 229
]

for c in data:
    print(chr(c ^ 0xdf), end='')
    