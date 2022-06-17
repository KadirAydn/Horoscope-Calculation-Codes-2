from ast import Break
from traceback import print_tb
from PIL import Image


print("BURÇ HESAPLAMA UYGULAMASINA HOŞGELDİNİZ! \n")


try:
    ay = int(input("Kaçıncı ayda doğdun: "))
except ValueError:
    print("HATA - BİR SAYI GİRMELİSİNİZ")
    quit()

if ay == 1:
    print("Demek Ocak ayında doğdun")
    try:
        gun = int(input("Ocak ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 21:                                        # OCAK AYI #
        print("OĞLAK BURCUSUN")
        Image.open("oglak.jpg").show()
    elif 20 < gun < 32:
        print("KOVA BURCUSUN")
        Image.open("kova.jpg").show()



elif ay == 2:
    print("Demek Şubat ayında doğdun")
    try:
        gun = int(input("Şubat ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 29:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 20:                                        # ŞUBAT AYI #
        print("KOVA BURCUSUN")
        Image.open("kova.jpg").show()
    elif 19 < gun < 30:
        print("BALIK BURCUSUN")
        Image.open("balik.jpg").show()



elif ay == 3:
    print("Demek Mart ayında doğdun")
    try:
        gun = int(input("Mart ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 21:                                        # MART AYI #
        print("BALIK BURCUSUN")
        Image.open("balik.jpg").show()
    elif 20 < gun < 32:
        print("KOÇ BURCUSUN")
        Image.open("koc.jpg").show()



elif ay == 4:
    print("Demek Nisan ayında doğdun")
    try:
        gun = int(input("Nisan ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 30:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 21:                                        # NİSAN AYI #
        print("KOÇ BURCUSUN")
        Image.open("koc.jpg").show()
    elif 20 < gun < 31:
        print("BOĞA BURCUSUN")
        Image.open("boga.jpg").show()



elif ay == 5:
    print("Demek Mayıs ayında doğdun")
    try:
        gun = int(input("Mayıs ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 21:                                        # MAYIS AYI #
        print("BOĞA BURCUSUN")
        Image.open("boga.jpg").show()
    elif 20 < gun < 32:
        print("İKİZLER BURCUSUN")
        Image.open("ikizler.jpg").show()



elif ay == 6:
    print("Demek Haziran ayında doğdun")
    try:
        gun = int(input("Haziran ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 30:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 22:                                        # HAZİRAN AYI #
        print("İKİZLER BURCUSUN")
        Image.open("ikizler.jpg").show()
    elif 21 < gun < 31:
        print("YENGEÇ BURCUSUN")
        Image.open("yengec.jpg").show()




elif ay == 7:
    print("Demek Temmuz ayında doğdun")
    try:
        gun = int(input("Temmuz ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 23:                                        # TEMMUZ AYI #
        print("YENGEÇ BURCUSUN")
        Image.open("yengec.jpg").show()
    elif 22 < gun < 32:
        print("ASLAN BURCUSUN")
        Image.open("aslan.jpg").show()




elif ay == 8:
    print("Demek Ağustos ayında doğdun")
    try:
        gun = int(input("Ağustos ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 24:                                        # AĞUSTOS AYI #
        print("ASLAN BURCUSUN")
        Image.open("aslan.jpg").show()
    elif 23 < gun < 32:
        print("BAŞAK BURCUSUN")
        Image.open("basak.jpg").show()





elif ay == 9:
    print("Demek Eylül ayında doğdun")
    try:
        gun = int(input("Eylül ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 30:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 24:                                        # EYLÜL AYI #
        print("BAŞAK BURCUSUN")
        Image.open("basak.jpg").show()
    elif 23 < gun < 31:
        print("TERAZİ BURCUSUN")
        Image.open("terazi.jpg").show()




elif ay == 10:
    print("Demek Ekim ayında doğdun")
    try:
        gun = int(input("Ekim ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 24:                                        # EKİM AYI #
        print("TERAZİ BURCUSUN")
        Image.open("terazi.jpg").show()
    elif 23 < gun < 32:
        print("AKREP BURCUSUN")
        Image.open("akrep.jpg").show()





elif ay == 11:
    print("Demek Kasım ayında doğdun")
    try:
        gun = int(input("Kasım ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 30:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 23:                                        # KASIM AYI #
        print("AKREP BURCUSUN")
        Image.open("akrep.jpg").show()
    elif 22 < gun < 31:
        print("YAY BURCUSUN")
        Image.open("yay.jpg").show()





elif ay == 12:
    print("Demek Aralık ayında doğdun")
    try:
        gun = int(input("Aralık ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 22:                                        # ARALIK AYI #
        print("YAY BURCUSUN")
        Image.open("yay.jpg").show()
    elif 21 < gun < 32:
        print("OĞLAK BURCUSUN")
        Image.open("oglak.jpg").show()





else:
    print(ay,"yazdınız.Lütfen tekrar deneyin ve 1-12 aralığında sayı girin")
    exit()

# coded by Kadir Aydın #
# insta: _kadiraydnn_
