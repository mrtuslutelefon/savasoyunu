import time
import random
import sys

print("Ahmet olarak, Mehmet ile savaşıyorsunuz.",
      "Hasar değeri, her 5'in katına ulaştığında 1 can kaybedersiniz.",
      "Oyunu oynamak için aşağıdaki bilgilere göre hamle yapın.", sep="\n")

class Savas():
    def __init__(self, isim, can=1, enerji=100):
        self.isim = isim
        self.can = can
        self.enerji = enerji
        self.hasar = 0

    def mevcutdurum(self):
        print("Can: ", self.can)
        print("Enerji: ", self.enerji)
        print("Hasar: ", self.hasar)

    def saldirisonucu(self):
        return random.randint(0,1)

    def saldir(self,rakip):
        print("Bir saldırı gerçekleştirdiniz.")
        print("Saldırı sürüyor, bekleyin.")
        for i in range(0,5):
            time.sleep(.3)
            print(".",end="",flush=True)

        sonuc = self.saldirisonucu()
        if sonuc == 0:
            print("\nRakibinize hasar verdiniz!")
            rakip.hasaral()
        if sonuc == 1:
            print("\nRakibinizden hasar aldınız.")
            self.hasaral()

    def kacmasonucu(self):
        return random.randint(0,1)

    def kac(self):
        print("Rakipten kaçmaya çalışıyorsunuz.")
        for i in range(0,5):
            time.sleep(.3)
            print(".",end="",flush=True)
        kacis = self.kacmasonucu()
        if kacis == 0:
            print("\nRakibiniz sizi yakaladı.")
            self.hasaral()
        if kacis == 1:
            print("\nRakibinizden kaçtınız.")

    def hasaral(self):
        self.hasar += 1
        self.enerji -= 5
        if (self.hasar % 5) == 0:
            self.can -= 1
    @classmethod
    def cik(cls):
        print("Oyundan çıkılıyor...")
        time.sleep(0.5)
        sys.exit()

# Oyun Başlangıcı

siz = Savas("Ahmet")
rakip = Savas("Mehmet")

while siz.can and rakip.can >= 1:
    print("\nRakibinizle karşı karşıyasınız. Yapmak istediğiniz hamleyi seçin:",
          "Saldır : s",
          "Kaç    : k",
          "Çık    : q", sep="\n")

    def durumgoruntule():
        print("\nRakibinizin durumu:")
        rakip.mevcutdurum()

        print("\nSizin durumunuz:")
        siz.mevcutdurum()

    hamle = input(">>>")

    if hamle == "s":
        siz.saldir(rakip)
        durumgoruntule()

    elif hamle == "k":
        siz.kac()
        durumgoruntule()

    elif hamle == "q":
        siz.cik()

    else:
        print("Geçersiz değer.")

def oyundancik():
    cevap = input("\nOyundan çıkmak için 'q' yazın: ")
    if cevap == "q":
        Savas.cik()
    else:
        print("Geçersiz değer.")

if siz.can == 0:
    print("\nOyunu",rakip.isim,"kazandı!")
    oyundancik()

if rakip.can == 0:
    print("\nOyunu",siz.isim,"kazandı!")
    oyundancik()