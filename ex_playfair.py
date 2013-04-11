import playfair
if __name__ == '__main__':
    en = [('SI IN CRIPTOGRAFIE TACEREA ESTE AUR', 'CRIPTOGRAFIE'), 
          ('SECURITY IS CHANGING FIELD', 'CHANNEL'), 
          ('AUTONOMOUS ATTACK AGENTS', 'MALICIOUS'),
          ('VALUABLE SOURCE OF REFERENCE', 'INSTITUTE'), 
          ('THE CIRCLE', 'ALBUM')]
    de = [('UFRIL ERGPC RQAW', 'CRIPTOGRAFIE'), 
          ('KDDPM RUBVR PTSFU HPEBV', 'PASSWORD'), 
          ('KDPEK DOSTF RDRXB NBBBB', 'PASSWORD'),
          ('KDPEK DKBDC RDQOP MTKDC XPNS', 'PASSWORD'), 
          ('GBQY YAAO RNBM', 'TEST'), ('PIGOY CLETY AEYLQ VSFWN', 'CRYPTOOL')]
    for pt in en:
        print playfair.Playfair(pt[1]).encrypt(pt[0])
    for ct in de:
        print playfair.Playfair(ct[1]).decrypt(ct[0])
    
