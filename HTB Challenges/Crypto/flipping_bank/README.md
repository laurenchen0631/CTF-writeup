1. The challenge gave us the host and its source code. 

```
$ nc 167.172.55.94 30332
username: aaa
aaa's password: aaa
########################################################################
#                  Welcome to the Bank of the World                    #
#             All connections are monitored and recorded               #
#      Disconnect IMMEDIATELY if you are not an authorized user!       #
########################################################################
Leaked ciphertext: 917d6131089b4e5ed8d91b85f211293c4eb5337655d2b56f811ddcfa61676dedb76b3f269ee9eac77462884a525df6d3
enter ciphertext:
```

2. We analyzed and discovered that we need to provide plaintext `admin&password=g0ld3n_b0y` that is encrypted using its secret key.

```python

key = get_random_bytes(16)
iv = get_random_bytes(16)

def decrypt_data(encryptedParams):
	cipher = AES.new(key, AES.MODE_CBC,iv)
	paddedParams = cipher.decrypt( unhexlify(encryptedParams))
	print(paddedParams)
	if b'admin&password=g0ld3n_b0y' in unpad(paddedParams,16,style='pkcs7'):
		return 1
	else:
		return 0


def main():
    # SNIP
	msg = 'logged_username=' + user +'&password=' + passwd
	send_msg(s, "Leaked ciphertext: " + encrypt_data(msg)+'\n')
	send_msg(s,"enter ciphertext: ")

	enc_msg = s.recv(4096).decode().strip()
	
	try:
		check = decrypt_data(enc_msg)
```

3. After studying AES CBC mode, an exploit exists called [CBC byte flipping attack](https://resources.infosecinstitute.com/topic/cbc-byte-flipping-attack-101-approach/).

4. Its block size is 16 bytes; thus, the plaintext is divided as `logged_username=`, `admin&password=g`, and `0ld3n_b0y`.

5. We can change any character in the `admin&password=g` to avoid detection. Also, to use flipping attack, we change the $b_j'[i] = b_{j-1}[i] \oplus m_j[i] \oplus m_j'[i]$ where $b_j$ is $j^{th}$ cipher block and $m_j$ is $j^{th}$ plaintext block.