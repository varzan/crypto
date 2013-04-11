import string
class Hill:
    def __init__(self, passkey, leftmul = False, replacespacechar = ' '):
        self.passkey = [ord(c) - ord('A') for c in passkey[:4].upper()]
        self.leftmul = leftmul
        self.replacespacechar = replacespacechar
        self.dekey = [self.passkey[3], -self.passkey[1], -self.passkey[2], 
                      self.passkey[0]]
        det = inv_mod(self.passkey[0] * self.passkey[3] 
                      - self.passkey[2] * self.passkey[1], 26) % 26
        self.dekey = [n * det % 26 for n in self.dekey]
                 
    def _preprocess(self, s):
        return "".join(c if c in string.ascii_uppercase 
                       else self.replacespacechar if str.isspace(c) 
                       else "" for c in s.upper())
                    
    def encrypt_chars(self, ch1, ch2):
        c1 = ord(ch1) - ord('A')
        c2 = ord(ch2) - ord('A')
        if self.leftmul:
            return (chr(ord('A') 
                    + (c1 * self.passkey[0] + c2 * self.passkey[1]) % 26),
                    chr(ord('A') 
                    + (c1 * self.passkey[2] + c2 * self.passkey[3]) % 26))
        else:
            return (chr(ord('A') 
                    + (c1 * self.passkey[0] + c2 * self.passkey[2]) % 26),
                    chr(ord('A') 
                    + (c1 * self.passkey[1] + c2 * self.passkey[3]) % 26))

    def encrypt(self, s):
        s = self._preprocess(s)
        l = len(s)
        return "".join("".join(self.encrypt_chars(s[i], s[i+1]))
                       for i in range(0, l-1, 2))
                       
    def decrypt_chars(self, ch1, ch2):
        c1 = ord(ch1) - ord('A')
        c2 = ord(ch2) - ord('A')
        if self.leftmul:
            return (chr(ord('A') 
                    + (c1 *  self.dekey[0] + c2 *  self.dekey[1]) % 26),
                    chr(ord('A') 
                    + (c1 *  self.dekey[2] + c2 *  self.dekey[3]) % 26))
        else:
            return (chr(ord('A') 
                    + (c1 *  self.dekey[0] + c2 *  self.dekey[2]) % 26),
                    chr(ord('A') 
                    + (c1 *  self.dekey[1] + c2 *  self.dekey[3]) % 26))
            
    def decrypt(self, s):
        s = "".join(c.upper() for c in s if c in string.ascii_letters)
        l = len(s)
        return "".join("".join(self.decrypt_chars(s[i], s[i+1]))
                       for i in range(0, l-1, 2))
                       
def inv_mod(n, p):
    x = 0
    lastx = 1
    y = 1    
    lasty = 0
    while p != 0:
        quotient = n // p
        (n, p) = (p, n % p)
        (x, lastx) = (lastx - quotient*x, x)
        (y, lasty) = (lasty - quotient*y, y)        
    return lastx

