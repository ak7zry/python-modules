#import modules
import module_matematika

if __name__ == "__main__":
    # menggunakan function dari modules
    hasil1 = module_matematika.tambah(10,5)
    hasil2 = module_matematika.kurang(7,5)

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
    print("Nilai PI:", module_matematika.PI)
    print("Dibuat Oleh:", module_matematika.PEMBUAT)
    print("=========================")