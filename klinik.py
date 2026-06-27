import subprocess
from prettytable import PrettyTable
import time

idDokter = ("001","002","003")
namaDokter = ("drg. Riskiyana","dr. Rizkilia","dr. Alhimni Rusdi")
spesialis = ("Spesialis Gigi","Spesialis Syaraf","Spesialis Jantung")

antrian = []

data_rm = {}

detailPasien = {}

def tabelDokter():
    tabel = PrettyTable()
    tabel.field_names = ["ID","NAMA","SPESIALIS"]

    for k,j,l in zip(idDokter,namaDokter,spesialis):
        tabel.add_row([k,j,l])

    print(tabel)

def antrian_pasien():
    rm = input("Masukkan No. Rekam Medis: ")

    if rm not in data_rm:
        print("No.RM belum terdaftar. Anda akan diarahkan ke lama registrasi.")
        time.sleep(0.8)
        regis_rm()
    else:
        print("\nNo.RM sudah terdaftar.")
        nama = data_rm[rm]["nama"]
        print(f"\nNama:{nama}")

        if len(antrian) == 0:
            id_kujungan = 1
        else:
            id_kujungan = len(antrian)+1

        antrian.append(id_kujungan)

        keluhan = input("Masukkan keluhan: ")
        id_dokter = input("Masukkan id Dokter: ")

        indeks = idDokter.index(id_dokter)
        nama_dokter = namaDokter[indeks]

        detailPasien[id_kujungan] = {
            "rm":rm,
            "nama":nama,
            "keluhan":keluhan,
            "dokter":nama_dokter
        }

def regis_rm():
    subprocess.run('cls', shell=True)
    print("REGISTRASI NO REKAM MEDIS ( WAJIB )\n")
    rm_baru = input("Masukkan No.RM: ")
    nama_baru = input("Masukkan nama: ")

    data_rm[rm_baru] = {
        "nama":nama_baru
    }
    print("\nNo.RM berhasil di registrasi.")
    time.sleep(0.6)
    menu()

def cari_nama():
    rm = input("\nMasukkan No.RM: ")
    nama = data_rm[rm]["nama"]
    print(f"\nNo.{rm}: {nama}")

    lihat = input("Ingin melihat Riwayat kunjungan (y/t): ").lower()
    if lihat == "y":
        riwayat(nama)
        input()
    else:
        menu()

def rekap():
    tabel = PrettyTable()

    tabel.field_names = ["ID","No.RM","NAMA","KELUHAN","DOKTER"]

    for id, nilai in detailPasien.items():
        tabel.add_row([
            id,
            nilai['rm'],
            nilai['nama'],
            nilai['keluhan'],
            nilai['dokter']
        ])

    print(tabel)

def riwayat(nama):
    tabel = PrettyTable()

    tabel.field_names = ["ID","No.RM","NAMA","KELUHAN","DOKTER"]

    for id, nilai in detailPasien.items():
        if nama == nilai['nama']:
            tabel.add_row([
                id,
                nilai['rm'],
                nilai['nama'],
                nilai['keluhan'],
                nilai['dokter']
            ])
    print(tabel)


def menu():
    while True:
        subprocess.run("cls", shell=True)
        print(f"{'SELAMAT DATANG DI KLINIK SEHAT MEDIKA':^100}\n")
        print("1.Transaksi KLINIK")
        print("2.Rekap Transaksi")
        print("3.Cari Nama(RM)")
        print("4.keluar")

        pilih = input("Masukkan menu: ")

        if pilih == "1":
            tabelDokter()
            print()
            antrian_pasien()
        elif pilih == "2":
            rekap()
            input("ENTER...")
        elif pilih == "3":
            cari_nama()
        elif pilih == "4":
            break
        else:
            print("Masukkan sesuai menu.")


menu()