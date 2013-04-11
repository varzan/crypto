import string
class Substitution:

    def __init__(self, password):
        table = []
        used = dict([(c, False) for c in string.ascii_uppercase])
        for c in password.upper() + string.ascii_uppercase:
            if not used[c]:
                table.append(c)
                used[c] = True
        self.table = dict([pair for pair in zip(string.ascii_uppercase, table)])
        self.de_table = dict([(pair[1], pair[0]) 
                             for pair in zip(string.ascii_uppercase, table)])

    def encrypt(self, text, replacespacechar = ' '):
        text.replace(' ', replacespacechar)
        return "".join(self.table[c] for c in text.upper() 
                       if c in string.ascii_uppercase)

    def decrypt(self, text):
        return "".join(self.de_table[c] for c in text.upper() 
                       if c in string.ascii_uppercase)
