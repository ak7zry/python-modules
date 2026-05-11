#import seluruh isi modules
from module_matematika import *

#jika function/variable sama dengan nama di program utama:
# PEMBUAT = "HAHAH~~"
# maka nilai variable di module akan di ganti dengan nilai variable di program utama

if __name__ == "__main__":
    # menggunakan function dari modules
    hasil1 = tambah(10,5)
    hasil2 = kurang(7,5)

    print("=========================")
    print("  FUNCTION DARI MODULES  ")
    print("=========================")
    print(f"Hasil dari 10 + 5 = {hasil1}")
    print(f"Hasil Dari 7 - 5 = {hasil2}")
    print("=========================")

    # menggunakan variable dari modules
    print("=========================")
    print("  VARIABEL DARI MODULES  ")
    print("=========================")
    print(f"Nilai PI: {PI}") 
    print(f"Dibuat Oleh: {PEMBUAT}")
    print("=========================")