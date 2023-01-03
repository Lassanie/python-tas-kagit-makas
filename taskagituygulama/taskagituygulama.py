import random, sys

#Taş kağıt makas oyunu

print('Taş, Kağıt, Makas!')

yenme = 0
yenilme = 0
berabere = 0

while True: # Ana döngü
    print('%s kez kazandın, %s kez kaybettin, %s kez berabere oldu.' % (yenme, yenilme, berabere))
    while True: # Kullanıcı girisi döngüsü
        print('Hamleni yap: (t)aş, (k)ağıt, (m)akas ya da (v)azgeç.')
        oyuncuHamle = input()
        if oyuncuHamle == 'v':
            sys.exit() # Oyundan çık.
        if oyuncuHamle == 't' or oyuncuHamle == 'k' or oyuncuHamle == 'm':
            break # Kullanıcı girisi döngüsünden çık
        print('t, k, m ya da v yaz.')

    # Oyuncunun girisini göster
    if oyuncuHamle == 't':
        print('Taşa karşı...')
    elif oyuncuHamle == 'k':
        print('Kağıda karşı...')
    elif oyuncuHamle == 'm':
        print('Makasa karşı...')

    # Bilgisayarın seçimini göster
    rastgeleNumara = random.randint(1,3)
    if rastgeleNumara == 1:
        bilgisayarHamle = 't'
        print('taş')
    elif rastgeleNumara == 2:
        bilgisayarHamle = 'k'
        print('kağıt')
    elif rastgeleNumara == 3:
        bilgisayarHamle = 'm'
        print('makas')

    # Yenme/yenilme/berabere vaziyetini göster
    if oyuncuHamle == bilgisayarHamle:
        print('Berabere')
        berabere= berabere + 1
    elif oyuncuHamle == 't' and bilgisayarHamle == 'm':
        print('Kazandın')
        yenme = yenme + 1
    elif oyuncuHamle == 'k' and bilgisayarHamle == 't':
        print('Kazandın')
        yenme = yenme + 1
    elif oyuncuHamle == 'm' and bilgisayarHamle == 'k':
        print('Kazandın')
        yenme = yenme + 1
    elif oyuncuHamle == 't' and bilgisayarHamle == 'k':
        print('Kaybettin')
        yenilme = yenilme + 1
    elif oyuncuHamle == 'k' and bilgisayarHamle == 'm':
        print('Kaybettin')
        yenilme = yenilme + 1
    elif oyuncuHamle == 'm' and bilgisayarHamle == 't':
        print('Kaybettin')
        yenilme = yenilme + 1
        