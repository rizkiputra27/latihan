import os

data_gedung = {
    'rpt':{
        'nama':'Gedung rapat',
        'sewa':1000000,
        'jam':200000
    },

    'pns':{
    'nama':'Gedung pentas seni',
    'sewa':1500000,
    'jam':300000
    },
    
    'pnk':{
        'nama':'Gedung pernikahan',
        'sewa':2500000,
        'jam':500000
    }
}


def rupiah(angka):
    return f"{angka:,}".replace(",",".")

def hitung(kGedung,lama,jam):
    if kGedung in data_gedung:
        sewaHari = data_gedung[kGedung]['sewa']
        sewaJam = data_gedung[kGedung]['jam']
        total1 = lama*sewaHari
        total2 = jam*sewaJam
        if lama > 3:
            diskon = total1*0.1
        else:
            diskon = 0
        total3 = total1+total2
        totDis = (total1-diskon)+total2
        return total3,diskon,totDis
    else:
        return 0,0,0
        
        


while True:
    os.system('cls')
    print("="*50)
    print(f"|{'KODE':^5}|{'NAMA':^20}|{'SEWA':^10}|{'JAM':^10}|")
    print("="*50)
    for key,data in data_gedung.items():

        NAMA  = data['nama']
        SEWA = data['sewa']
        JAM = data['jam']

        print(f"|{key:^5}|{NAMA:^20}|{SEWA:^10}|{JAM:^10}|")
    print("="*50)

    print("\n=====Masukkan detail transaksi=====")
    nama=input("Masukkan nama penyewa: ")
    kGedung = input("Masukkan kode gedung: ")
    lama = int(input("Masukkan lama sewa: "))
    jam = int(input("Masukkan kelebihan jam: "))


    total3,diskon,totDis = hitung(kGedung,lama,jam)
    if total3 == 0 and diskon == 0 and totDis == 0:
        print()
        print("=====Kode tidak ditemukan=====")
        print()
        print("="*117)
        print(f"|{"Nama":^25}|{"Nama Gedung":^25}|{"Lama Sewa":^15}|{"Harga awal":^15}|{"Diskon":^15}|{"Total":^15}|")
        print("="*117)
        print(f"|{nama:^25}|{"Gedung belum ada":^25}|{"-":^15}|{rupiah(total3):^15}|{rupiah(diskon):^15}|{rupiah(totDis):^15}|")
        print("="*117)
        input("ENTER...")
    elif isinstance(total3,(int,float)) and isinstance(diskon,(int,float)) and isinstance(totDis,(int,float)):
        print("="*117)
        print(f"|{"Nama":^25}|{"Nama Gedung":^25}|{"Lama Sewa":^15}|{"Harga awal":^15}|{"Diskon":^15}|{"Total":^15}|")
        print("="*117)
        print(f"|{nama:^25}|{data_gedung[kGedung]['nama']:^25}|{lama:^15}|{rupiah(total3):^15}|{rupiah(diskon):^15}|{rupiah(totDis):^15}|")
        print("="*117)
        input("ENTER...")
    else:
        print("Kode tidak ditemukan")
