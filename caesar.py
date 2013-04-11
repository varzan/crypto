import string
def encrypt(s, k):
    return "".join(chr((ord(c) - ord('A') + k) % 26 + ord('A')) 
                   for c in s.upper() if c in string.ascii_letters)
                   
def decrypt(s, k):
    return "".join(chr((ord(c) - ord('A') - k) % 26 + ord('A'))
                   for c in s.upper() if c in string.ascii_letters)
                   
def try_decrypt(s):
    return [decrypt(s, k) for k in range(0, 26)]
