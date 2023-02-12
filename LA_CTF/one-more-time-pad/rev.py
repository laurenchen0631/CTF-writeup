pt = "200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e"

plaintext = b"Long ago, the four nations lived together in harmony ..."

for i in range(0, len(pt), 2):
    cypher = int(pt[i:i+2], 16)
    print(chr(cypher ^ plaintext[i//2]), end="")