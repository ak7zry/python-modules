import os

def tambah():
    print("==== PENJUMLAHAN ====")
    print()
    angka1 = int(input("Angka 1: "))
    angka2 = int(input("Angka 2: "))
    hasil = angka1 + angka2
    print("Hasil Penjumlahan", hasil)
    print("==== PROGRAM SELESAI ====")
    
def kurang():
    print("==== PENGURANGAN ====")
    print()
    angka1 = int(input("Angka 1: "))
    angka2 = int(input("Angka 2: "))
    hasil = angka1 - angka2
    print("Hasil Pengurangan", hasil)
    print("==== PROGRAM SELESAI ====")
    
def kali():
    print("==== PERKALIAN ====")
    print()
    angka1 = int(input("Angka 1: "))
    angka2 = int(input("Angka 2: "))
    hasil = angka1 * angka2
    print("Hasil Perklaian", hasil)
    print("==== PROGRAM SELESAI ====")
    
def bagi():
    print("==== PEMBAGIAN ====")
    print()
    angka1 = int(input("Angka 1: "))
    angka2 = int(input("Angka 2: "))
    hasil = angka1 / angka2
    print("Hasil Pembagian", hasil)
    print("==== PROGRAM SELESAI ====")
    
def bersih():
    if os.name == "nt":
        _ = os.system("cls")