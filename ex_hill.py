import hill
if __name__ == '__main__':
    en = [('BLAZE OF GLORY', 'jbvi', True), 
          ('COMPLETE AND PROPER PACKAGE', 'NTCR', True),
          ('ESOTERIC TOPIC OF RESEARCH', 'BYGP', False)]
    de = [('JESHB JJAZM TANCF VBJXX', 'HUDF', False), 
          ('ZKNAW NIOZO BRXSW QNNXX', 'BEVH', False),
          ('ZPXUB IRHNU VXWSP DJTNN', 'JDXC', False),
          ('NYNAF JUWBL ZXANM NGLEI JQWF', 'JSWV', False),
          ('NKTNM QZQEY WVDIA CIGMG', 'DIKB', False)]
    for pt in en:
        print hill.Hill(pt[1], pt[2], '').encrypt(pt[0])
    for ct in de:
        print hill.Hill(ct[1], ct[2], '').decrypt(ct[0])
