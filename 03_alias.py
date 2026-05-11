#import modules alias math
import module_matematika as math

if __name__ == "__main__":
    # menggunakan function dari modules
    hasil1 = math.tambah(10,5)
    hasil2 = math.kurang(7,5)

    print("=========================")
    print("  FUNCTION DARI MODULES  ")
    print("=========================")
    print("Hasil dari 10 + 5 =", hasil1)
    print("Hasil Dari 7 - 5 =", hasil1)
    print("=========================")

    # menggunakan variable dari modules
    print("=========================")
    print("  VARIABEL DARI MODULES  ")
    print("=========================")
    print("Nilai PI:", math.PI)
    print("Dibuat Oleh:", math.PEMBUAT)
    print("=========================")