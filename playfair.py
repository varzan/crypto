import string
class Playfair:
    def __init__(self, passphrase):
        used = dict([(a, False) for a in string.ascii_uppercase])
        self.table = []
        for i in range(5):
            self.table.append([None for i in range(5)])
        i = 0
        for c in passphrase.upper() + string.ascii_uppercase:
            if c in string.ascii_uppercase:
                if not used[c]:
                   self.table[i//5][i%5] = c
                   used[c] = True
                   if c == 'I':
                       used['J'] = True
                   elif c == 'J':
                       used['I'] = True
                   i = i + 1
               
    def _find(self, c):
        for i in range(5):
            for j in range(5):
                if (self.table[i][j] == c 
                   or (c == 'I' and self.table[i][j] == 'J') 
                   or (c == 'J' and self.table[i][j] == 'I')):
                    return (i, j)
                    
    def _preprocess(self, s):
        s = "".join(c if c in string.ascii_uppercase else "Q" if str.isspace(c) 
                    else "" for c in s.upper())
        l = len(s)
        s = "". join("".join((s[i], "Q", s[i+1])) if s[i] == s[i+1] 
                     else "".join((s[i], s[i+1])) for i in range(0, l-1, 2))
        if len(s) % 2 == 1:
            s += "Q"
        return s
                    
    def encrypt_chars(self, c1, c2):
        (i1, j1) = self._find(c1)
        (i2, j2) = self._find(c2)
        if j1 == j2:
            return self.table[(i1 + 1) % 5][j1], self.table[(i2 + 1) % 5][j2]
        elif i1 == i2:
            return self.table[i1][(j1 + 1) % 5], self.table[i1][(j2 + 1) % 5]
        else:
            return self.table[i1][j2], self.table[i2][j1]

    def encrypt(self, s):
        s = self._preprocess(s)
        l = len(s)
        return "".join("".join(self.encrypt_chars(s[i], s[i+1]))
                       for i in range(0, l-1, 2))
                       
    def decrypt_chars(self, c1, c2):
        (i1, j1) = self._find(c1)
        (i2, j2) = self._find(c2)
        if j1 == j2:
            return self.table[(i1 - 1) % 5][j1], self.table[(i2 - 1) % 5][j2]
        elif i1 == i2:
            return self.table[i1][(j1 - 1) % 5], self.table[i1][(j2 - 1) % 5]
        else:
            return self.table[i1][j2], self.table[i2][j1]
            
    def decrypt(self, s):
        s = "".join(c.upper() for c in s if c in string.ascii_letters)
        l = len(s)
        return "".join("".join(self.decrypt_chars(s[i], s[i+1]))
                       for i in range(0, l-1, 2))
