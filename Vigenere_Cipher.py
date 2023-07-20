#program on vigenere cipher
string=input("Enter the string (i.e upper case String) of your wish to to encrypt:-")
key=input("Enter the key(upper case) of your wish:-")
cyclickey=""+key
k1=len(key)
s1=len(string)
if(k1==s1):
    key=key
else:
    for i in range(0,s1-k1,1):
        cyclickey = cyclickey + key[i % k1]
print(f"The cyclickey of given key {key} is:-",cyclickey)

encryptedtext=""
for i in range(0,s1,1):
    encryptedtext=encryptedtext+chr(((ord(string[i]) + ord(cyclickey[i])) % 26)+65)
print(f"Encrypted Text of {string} is:-",encryptedtext)
decryptedtext=''
for i in range(s1):
    decryptedtext=decryptedtext+chr(((ord(encryptedtext[i])-ord(cyclickey[i])+26)%26)+65)
print(f"Decrypted text of {encryptedtext} is:-",decryptedtext)