# Komplek pergudangan
import os

dataGudang = {
    'elk':'Gudang Elektronik',
    'bgn':'Gudang Bangunan',
    'mbl':'Gudang Mebeler'
}

def rupiah(angka):
    return f"Rp. {angka:,}".replace(",",".")

def hitung(lama,sewaAwal,sewaNormal):
    biaya = 0
    for i in range(0,lama,1):
        if i == 0:
            biaya = biaya + sewaAwal
        else:
            biaya = biaya + sewaNormal
    return biaya


while True:
    os.system('cls')
    print("="*30)
    print(f"|{'KODE':^7}|{'NAMA GUDANG':^20}|")
    print("="*30)
    for key,value in dataGudang.items():
        print(f"|{key:<7}|{value:<20}|")
    print("="*30)

    nama = input("Masukkan nama penyewa: ")
    lama = int(input("Masukkan lama sewa: "))
    kGudang = input("Masukkan kode Gudang: ")

    if kGudang == "elk":
        sewaAwal = 12000000
        sewaNormal = 10000000
    elif kGudang == "bgn":
        sewaAwal = 15000000
        sewaNormal = 12000000
    elif kGudang == "mbl":
        sewaAwal = 17500000
        sewaNormal = 14000000
    else:
        print("Kode tidak valid...")
        input("Tekan enter untuk kembali...")
        continue
    
    
    totalBiaya = hitung(lama,sewaAwal,sewaNormal)
    print()
    print("="*70)
    print(f"|{"NAMA":^20}|{"NAMA GUDANG":^20}|{"LAMA SEWA":<10}|{"TOTAL":^15}|")
    print("="*70)
    print(f"|{nama:^20}|{dataGudang[kGudang]:^20}|{lama:^10}|{rupiah(totalBiaya):^15}|")
    print("="*70)

    input("Tekan ENTER untuk kembali...")        