def joulukuusi(korkeus):
    for i in range(korkeus):
        print(' ' * (korkeus - i - 1) + '*' * (2 * i + 1))
    print(' ' * (korkeus - 1) + '*')
joulukuusi(6)