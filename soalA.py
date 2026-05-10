#Manajemen persewaan gedung
import os
import sys

#Data nama gedung
data_gedung = {
    'rpt':'Gedung Rapat',
    'ps':'Gedung Pentas Seni',
    'pnk':'Gedung Pernikahan'
}

#Format rupiah
def rupiah(angka):
    return f"Rp {angka:,}".replace(",", ".")


def sewa(nama,kGedung,lama,jam):
    if kGedung == "rpt":
        sewa = 1000000
        total1 = sewa*lama
        if jam >= 1:
            total2 = jam*200000
        else:
            print("Tidak ada jam tambahan")
            total2 = 0
        total3 = total1+total2
        if lama > 3:
            diskon = 0.1*total1
        else:
            diskon = 0*total1
        hartot = total3 - diskon
        print("="*117)
        print(f"|{"Nama":^25}|{"Nama Gedung":^25}|{"Lama Sewa":^15}|{"Harga awal":^15}|{"Diskon":^15}|{"Total":^15}|")
        print("="*117)
        print(f"|{nama:^25}|{data_gedung[kGedung]:^25}|{lama:^15}|{rupiah(total3):^15}|{rupiah(diskon):^15}|{rupiah(hartot):^15}|")
        print("="*117)
    elif kGedung == "ps":
        sewa = 1500000
        total1 = sewa*lama
        if jam >= 1:
            total2 = jam*300000
        else:
            print("Tidak ada jam tambahan")
            total2 = 0
        total3 = total1+total2
        if lama > 3:
            diskon = 0.1*total1
        else:
            diskon = 0*total1
        hartot = total3 - diskon
        print("="*117)
        print(f"|{"Nama":^25}|{"Nama Gedung":^25}|{"Lama Sewa":^15}|{"Harga awal":^15}|{"Diskon":^15}|{"Total":^15}|")
        print("="*117)
        print(f"|{nama:^25}|{data_gedung[kGedung]:^25}|{lama:^15}|{rupiah(total3):^15}|{rupiah(diskon):^15}|{rupiah(hartot):^15}|")
        print("="*117)
    elif kGedung == "pnk":
        sewa = 2500000
        total1 = sewa*lama
        if jam >= 1:
            total2 = jam*500000
        else:
            print("Tidak ada jam tambahan")
            total2 = 0
        total3 = total1+total2
        if lama > 3:
            diskon = 0.1*total1
        else:
            diskon = 0*total1
        hartot = total3 - diskon
        print("="*117)
        print(f"|{"Nama":^25}|{"Nama Gedung":^25}|{"Lama Sewa":^15}|{"Harga awal":^15}|{"Diskon":^15}|{"Total":^15}|")
        print("="*117)
        print(f"|{nama:^25}|{data_gedung[kGedung]:^25}|{lama:^15}|{rupiah(total3):^15}|{rupiah(diskon):^15}|{rupiah(hartot):^15}|")
        print("="*117)
    else:
        print("\n=====Kode tidak valid!=====")


while True:
    os.system('cls')

    print("="*28)
    print(f"|{"Kode":^5}|{"Nama Gedung":^20}|")
    print("="*28)

    for nama,value in data_gedung.items():
        print(f"|{nama:<5}|{value:<20}|")
    print("="*28)

    print("\nMasukkan detail transaksi:")
    nama=input("Masukkan nama penyewa: ")
    kGedung = input("Masukkan kode gedung: ")
    lama = int(input("Masukkan lama sewa: "))
    jam = int(input("Masukkan kelebihan jam: "))

    sewa(nama,kGedung,lama,jam)
    input("Tekan enter untuk kembali...")