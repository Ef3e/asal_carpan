import os
while True:
    sayi1 = int(input("sayi gir = "))
    def myfunc(deger = [u for u in range(1,sayi1+1)]):
        sonuc = 0
        for a in deger:
            sonuc = sonuc + a
        return sonuc
    def carpan_ayir(sayi = myfunc()):
        bolum = 1
        carpanlar = []
        while True:
            if sayi % bolum == 0:
                carpanlar.append(bolum)
            bolum += 1
            if bolum > sayi:
                break
        return carpanlar
    print("[1] sayinizin carpanlarini gor")
    print("[2] 1 den sayiniza kadar olan sayilarin toplaminin carpalnarini gor")
    gor = input()
    if gor == "1":
        ayir = carpan_ayir(sayi = sayi1)
        os.system("cls")
        print(ayir)
    if gor == "2":
        fuc = myfunc()
        os.system("cls")
        print(f"1 den {sayi1} ya kadar olan sayilarin toplami {fuc}")
        ayir = carpan_ayir()
        print(ayir)
    if gor == "9":
        exit()
