import os
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin123",
    database="gudang",
    port=3307

)

cursor = db.cursor()

def tambah():
    kode = input("Masukkan kode gudang: ")
    nama = input("Masukkan nama gudang: ")
    sAwal = int(input("Masukkan biaya sewa awal: "))
    sNormal = int(input("Masukkan biaya sewa normal: "))

    query = """
    INSERT INTO datagudang
    (kode,nama,sAwal,sNormal)
    VALUES (%s,%s,%s,%s)
    """
    values = kode,nama,sAwal,sNormal
    cursor.execute(query,values)
    db.commit()

def hapus():
    kode = input("Masukkan kode: ")
    query = "SELECT * FROM datagudang WHERE = %s"
    cursor.execute(query,(kode,))
    hasil = cursor.fetchone()

    if hasil is None:
        print(f"{kode} tidak ditemukan")
    else:
        query = """
        DELETE FROM datagudang
        WHERE kode = %s
        """
        cursor.execute(query,(kode,))
        db.commit()
        input("Enter untuk lanjutkan...")

def update():
    kode = input("Masukkan kode: ")
    query = "SELECT * FROM datagudang WHERE kode = %s"
    cursor.execute(query,(kode,))
    hasil = cursor.fetchone()

    if hasil is None:
        print(f"{kode} tidak ditemukan")
    else:
        print("OPSI UPDATE")
        print("1. UPDATE nama")
        print("2. UPDATE Sewa Awal")
        print("3. UPDATE Sewa Normal")
        pilih = input("Ingin update apa? ")

        if pilih == "1":
            namaBaru = input("Masukkan nama baru: ")
            query = """
            UPDATE datagudang
            SET nama = %s
            WHERE kode = %s
            """
            cursor.execute(query,(namaBaru,kode))
            db.commit()
        elif pilih == "2":
            sAbaru = int(input("Masukkan sewa Awal baru: "))
            query = """
            UPDATE datagudang
            SET sAwal = %s
            WHERE kode = %s
            """
            cursor.execute(query,(sAbaru,kode))
            db.commit()
        elif pilih == "3":
            sNbaru = int(input("Masukkan sewa Normal baru: "))
            query = """
            UPDATE datagudang
            SET sNormal = %s
            WHERE kode = %s
            """
            cursor.execute(query,(sNbaru,kode))
            db.commit()
        else:
            print(f"{kode} tidak valid")
tambah()