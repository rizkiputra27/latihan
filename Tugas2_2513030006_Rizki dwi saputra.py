# 1.Denah Tempat Duduk
import math

print("DENAH TEMPAT DUDUK BIS UNP KEDIRI")
print("Kapasitas kursi BUS: 5")
print("="*35)
jumlah = int(input("Masukkan jumlah Mahasiswa: "))
bus = math.ceil(jumlah/5)# .ceil untuk pembulatan keatas
kapasitas = 0

for i in range(bus):
    print(f"\n=====BUS {i+1}=====")
    for j in range(5):
        if kapasitas < jumlah:
            print("MASUKKAN NAMA: ")
            nama = input()
            print(f"{nama} duduk di kursi ke-{j+1}")
            kapasitas += 1
        else:
            break

# 2.parkir

parkir_rusak = int(input("Masukkan parkir Nonaktif: "))
kendaraan_masuk = int(input("Masukkan jumlah kendaraan: "))
uang_masuk = 0

for i in range(kendaraan_masuk):
    print(f"MASUKKAN PLAT KENDARAAN ke-{i+1}:")
    plat = int(input("(Contoh: 001): "))
    
    if parkir_rusak != 1 and plat % 7 == 0:
        print("PARKIR LANTAI 1")
        uang_masuk += 20000
    elif parkir_rusak != 2 and plat % 2 == 0:
        print("PARKIR LANTAI 2")
        uang_masuk += 10000
    elif parkir_rusak != 3 and plat % 2 != 0:
        print("PARKIR LANTAI 3")
        uang_masuk += 10000
    elif parkir_rusak != 4 and plat % 2 == 0:
        print("PARKIR LANTAI 4")
        uang_masuk += 10000
    else:
        print("TIDAK DAPAT PARKIR!")

print(f"Pendapatan: Rp.{uang_masuk}")