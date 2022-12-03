from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes, inverse, GCD
from secret import FLAG, KEY

WELCOME = """
************** Welcome to the Gringatts Bank. **************
*                                                          *
*                  Fortius Quo Fidelius                    *
*                                                          *
************************************************************
"""


class RSA():

    def __init__(self, key_length):
        self.e = 0x10001
        phi = 0
        prime_length = key_length // 2

        while GCD(self.e, phi) != 1:
            self.p, self.q = getPrime(prime_length), getPrime(prime_length)
            phi = (self.p - 1) * (self.q - 1)
            self.n = self.p * self.q

        self.d = inverse(self.e, phi)

    def encrypt(self, message):
        message = bytes_to_long(message)
        return pow(message, self.e, self.n)

    def decrypt(self, encrypted_message):
        message = pow(encrypted_message, self.d, self.n)
        return long_to_bytes(message)


class Bank:

    def __init__(self, rsa):
        self.options = "[1] Get public certificate.\n[2] Calculate Hint.\n[3] Unlock Vault.\n"
        self.shift = 256
        self.vaults = {
            f"vault_{i}": [b"passphrase", b"empty"]
            for i in range(100)
        }
        self.rsa = rsa

    def initializeVault(self, name, passphrase, data):
        self.vaults[name][0] = passphrase
        self.vaults[name][1] = data

    def calculateHint(self):
        return (self.rsa.p >> self.shift) << self.shift

    def enterVault(self, vault, passphrase):
        vault = self.vaults[vault]
        if passphrase.encode() == vault[0]:
            return vault[1].decode()
        else:
            print("\nFailed to open the vault!\n")
            exit(1)


if __name__ == "__main__":
    rsa = RSA(2048)
    bank = Bank(rsa)

    vault = "vault_68"
    passphrase = KEY
    bank.initializeVault(vault, passphrase, FLAG)

    encrypted_passphrase = rsa.encrypt(bank.vaults[vault][0])
    print(f"You managed to retrieve: {hex(encrypted_passphrase)[2:]}")
    # 16559a1288afcc48755430c72e11562155e1a01fe0b40894a3f6de14c9edff7a13f4192ff0cc1c3211003b44a63fc15c6ead2f49e9f335010c71a0104d84ac573e841e6685e46f83d7db2cdd8b439e591f09edaad3b3a197ba53828a4597ceefa32eaa6f6c93e7942900d05c5bd8a21c6a0739254d8822eb0c420d8bc9a954951b3bde9d9f45912f8fe95345524885c9f96f1dfeb1b6f0689888324b394b2529877489e4c07577b09740b4d122a20c628288b07467ac330ce7880e52613c6d85b3c5f97133a5605f3c1337220c9c684dbb669731497110ebb5871903920b6acade317f5d7eebfe4dde75a3bbacf6bab498c44b7c2a6c0c23975037e2a7339d61
    print("\nNow you are ready to enter the bank.")
    print(WELCOME)

    while True:
        try:
            print("Hello, what would you like to do?\n")
            print(bank.options)
            option = int(input("> "))

            if option == 1:
                print(f"\n{bank.rsa.n}\n{bank.rsa.e}\n")
                # 13258200037146541578777382994807135588092270979839328834179371681773708925649488450091320658866807482676102522929123623038769000214680135919460039438011181220646490624858448438841514674320962038540823302903534366988234790290711869967851629217247537335417814963195259508815122566430073116982358886635883966899180671697437611285632497457177043315735605316620572808625114688688404461355803835486745468339584859216457386370210431853397282503913785705356406382580459322754739780639274092893454103326649722350996510410384656147385033394912563242169131362090752024022971626467075875368177117191575570341773878202154814213359
                # 65537
            elif option == 2:
                print(f"\n{bank.calculateHint()}\n")
                # 94303238807078624351059462268606939274716005109151528982400767351457356281411095668273701259184321689060702461809491889186586907555385256323179913717632670161826710307472178446654204530704977832057498594007992003133275923688633364820006216827084038244871963525694941336481742359500955893309252941502763499520
            elif option == 3:
                vault = input("\nWhich vault would you like to open: ")
                passphrase = input("Enter the passphrase: ")
                print(f"\n{bank.enterVault(vault, passphrase)}\n")
            else:
                "Abort mission!"
                exit(1)
        except KeyboardInterrupt:
            print("Exiting")
            exit(1)
        except Exception as e:
            print(f"An error occurred while processing data: {e}")
            exit(1)
