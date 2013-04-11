import caesar
if __name__ == '__main__':
    en = [('MIRACLE', 3), ('CALCULATOR', 11), ('ELECTRONIC MAIL', 5), 
          ('DIGITAL SIGNATURE', 2)]
    de = ['IGQTI GYCUJ KPIVQ PXXXX', 'UIPNB TKFGG FSTPO', 
          'AREYY KYYOS VYUTM XGTZ', 'CDTC JCON KPEQ NP', 'ECFDEPO ALCEJ']
    for pt in en:
        print caesar.encrypt(pt[0], pt[1])
    for pt in de:
        print "----------------------------------------"
        print pt
        for (k, s) in enumerate(caesar.try_decrypt(pt)):
            print "%s k=%d" % (s, k)
        print "----------------------------------------"
