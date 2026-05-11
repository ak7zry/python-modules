#===========================================
#        APLIKASI KALKUKATOR SEDERHANA
#===========================================
    
from kalkulator import operasi 
    
if __name__ == "__main__":
    def menu():
        operasi.bersih 
        print("======================================")
        print("     APLIKASI KALKULATOR SEDERHANA    ")
        print("======================================")
        while True:
            print("1. Penjumlahan")
            print("2. Pengurangan")
            print("3. Perkalian")
            print("4. Pembagian")
            print("5. Keluar")
            
            try:
                pilih = int(input("Silahkan pilih Nomor diatas: "))
            except ValueError:
                print("Input hanya Angka!!") 
                menu()
            else:
                if pilih == 1:
                    operasi.tambah()
                    pilihan = input("Kembali Ke Menu (y/n) ?")
                    if pilihan == "y":
                        menu()
                    else:
                        exit()
                elif pilih == 2:
                    operasi.kurang()
                    pilihan = input("Kembali Ke Menu (y/n) ?")
                    if pilihan == "y":
                        menu()
                    else:
                        exit()
                elif pilih == 3:
                    operasi.kali()
                    pilihan = input("Kembali Ke Menu (y/n) ?")
                    if pilihan == "y":
                        menu()
                    else:
                        exit()
                elif pilih == 4:
                    operasi.bagi()
                    pilihan = input("Kembali Ke Menu (y/n) ?")
                    if pilihan == "y":
                        menu()
                    else:
                        exit()
                elif pilih == 5:
                    jawab = input("Apakah Anda akan keluar aplikasi (y/n?")
                    if jawab == "y":
                        exit()
                    else:
                        menu()
                else:
                    print("Pilihan hanya 1-5, input ulang pilihan anda!!")
                    break 
    menu()
        