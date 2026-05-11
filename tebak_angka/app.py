#================================
#     PERMAINAN TEBAK ANGKA
#================================
import random

def tebak_angka():
    acak = random.randint(1,10)
    maks = 3
    tebakan = 0
    
    while tebakan < maks:
        tebakan +=1
        angka_user = int(input("MAsukkan Angka: "))
        if angka_user > acak:
            print("Angka Terlalu Besar")
        elif angka_user < acak:
            print("Angka Terlalu Kecil")   
        else:
            print("Selamat angka benar")
            break
    else:
        print("Sudah melebihi batas percobaan")
        print("Angka Acak:", acak)   
             