import math
import random
global prime, root

def secretnumber ():
    secret = int(random.randint(0,100))
    return secret

prime = 17
print("The prime is ",prime, "\n")
root = 3
print("The root is",root, "\n")

alicesecret = secretnumber()
print("Alice chooses a secret number",alicesecret)

bobsecret = secretnumber()
print("Bob chooses a secret number", bobsecret, "\n")

alicepublic = (root ** alicesecret) % prime
print("Alice's public key is",alicepublic, "\n")
bobpublic = (root ** bobsecret) % prime
print("Bob's public key is", bobpublic, "\n")

alicekey = (bobpublic ** alicesecret) % prime
bobkey = (alicepublic ** bobsecret) % prime
print("Alice calculates the shared key and gets", alicekey)
print("Bob calculates the shared key and gets", bobkey, "\n")

