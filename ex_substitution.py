import substitution
if __name__ == '__main__':
    en = [('WEB DESIGN', 'BROWSER'), ('PUBLIC KEY', 'ASSYMETRIC')]
    de = [('ONCJB DFJPT DCJKN KKQTV TDSXXX', 'CRIPTOGRAFIE'), 
          ('EKBJO DSZAT NCGPF TJJTP YXXXX', 'CRIPTO')]
    for pt in en:
        print substitution.Substitution(pt[1]).encrypt(pt[0])
    for pt in de:
        print substitution.Substitution(pt[1]).decrypt(pt[0])
