import os
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gedung"
)

cursor = db.cursor()

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
    return f"Rp.{angka:,}".replace(",",".")

def tambah():
    kode = input("Masukkan kode: ")
    nama = input("Masukkan nama gedung: ")
    sewa = int(input("Masukkan sewa/Hari: "))
    jam = int(input("Masukkan sewa/Jam: "))

    query = """
    INSERT INTO datagedung
    (kode, nama, sewa, jam)
    VALUES (%s,%s,%s,%s)
    """

    value = (kode,nama,sewa,jam)

    cursor.execute(query, value)
    db.commit()

    print(f"{nama} berhasil ditambahan ke Database")

def hapus():
    kode = input("Masukkan kode Gedung: ")

    query = "SELECT * FROM datagedung WHERE kode=%s"
    cursor.execute(query,(kode,))
    hasil = cursor.fetchone()

    if hasil is None:
        print("Data tidak ditemukan")
    else:
        query = """
        DELETE FROM datagedung
        WHERE kode = %s
        """
        cursor.execute(query,(kode,))
        db.commit
        input()

def update():
    kode = input("Masukkan kode: ")
    query = "SELECT * FROM datagedung WHERE kode = %s"
    cursor.execute(query, (kode,))
    hasil = cursor.fetchone()
    if hasil is None:
        print('Kode tidak ditemukan')
    else:
        print("Ingin update yang mana (nama/sewa/jam)?")
        baru = input()
        if baru == "nama":
            namaBaru=input("Masukkan Nama baru: ")

            query = """
            UPDATE datagedung
            SET nama = %s
            WHERE kode = %s
            """

            cursor.execute(query, (namaBaru,kode))

        elif baru == "sewa":
            sewaBaru = int(input("Masukkan biaya sewa baru: "))

            query = """
            UPDATE datagedung
            SET sewa = %s
            WHERE kode = %s
            """

            cursor.execute(query, (sewaBaru,kode))

        elif baru == "jam":
            jamBaru = int(input("Masukkan biaya sewa jam: "))
            
            query = """
            UPDATE datagedung
            SET jam = %s
            WHERE kode = %s
            """
            cursor.execute(query, (jamBaru,kode))
        else:
            print("Pilihan tidak tersedia")
        
        db.commit()


def tampil2():
        print("="*50)
        print(f"|{'KODE':^5}|{'NAMA':^20}|{'SEWA':^10}|{'JAM':^10}|")
        print("="*50)
        for key,data in data_gedung.items():

            NAMA  = data['nama']
            SEWA = data['sewa']
            JAM = data['jam']

            print(f"|{key:^5}|{NAMA:^20}|{SEWA:^10}|{JAM:^10}|")
        print("="*50)


def tampil():
    cursor.execute("SELECT * FROM datagedung")

    hasil = cursor.fetchall()
    print("="*65)
    print(f"|{'KODE':^5}|{'NAMA':^20}|{'SEWA':^20}|{'JAM':^15}|")
    print("="*65)
    for kode,nama,sewa,jam in hasil:
        print(f"|{kode:<5}|{nama:<20}|{rupiah(sewa):<20}|{rupiah(jam):<15}|")
    print("="*65)   

def hitung(kGedung,lama,jam):
    query = "SELECT * FROM datagedung WHERE kode = %s"
    cursor.execute(query, (kGedung,))
    hasil = cursor.fetchone()

    if hasil is not None:
        sewaHari = hasil[2]
        sewaJam = hasil[3]
        total1 = lama*sewaHari
        total2 = jam*sewaJam
        if lama > 3:
            diskon = total1*0.1
        else:
            diskon = 0
        total3 = total1+total2
        totDis = (total1-diskon)+total2
        return total3,diskon,totDis,hasil[1]
    else:
        return 0,0,0,""
        
        


while True:
    os.system('cls')

    print("\n===== MENU TRANSAKSI=====")
    print("1. TRANSAKSI GEDUNG")
    print("2. TAMBAH GEDUNG")
    print("3. HAPUS GEDUNG")
    print("4. TAMPILKAN GEDUNG")
    print("5. UPDATE GEDUNG")
    print("6. KELUAR")

    pilih = int(input("Masukkan menu: "))
    print()
    if pilih == 1:
        tampil()
        print("\n===== MENU TRANSAKSI =====")
        nama=input("Masukkan nama penyewa: ")
        kGedung = input("Masukkan kode gedung: ")
        lama = int(input("Masukkan lama sewa: "))
        jam = int(input("Masukkan kelebihan jam: "))

        total3,diskon,totDis,namaGedung = hitung(kGedung,lama,jam)
        if total3 == 0 and diskon == 0 and totDis == 0 and namaGedung == "":
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
            print(f"|{nama:^25}|{namaGedung:^25}|{lama:^15}|{rupiah(total3):^15}|{rupiah(diskon):^15}|{rupiah(totDis):^15}|")
            print("="*117)
            input("ENTER...")
        else:
            print("Kode tidak ditemukan")
    elif pilih == 2:
        print(f"{'>><<===> TAMBAH GEDUNG <===>><<':^50}")
        tambah()
        input()
    elif pilih == 3:
        hapus()
    elif pilih == 4:
        tampil()
        input()
    elif pilih == 5:
        update()
        input()
    elif pilih == 6:
        break
    else:
        print("Pilihan tidak valid")


