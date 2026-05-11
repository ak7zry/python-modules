from tebak_angka import app

if __name__ == "__main__":
    def menu():
        
        while True:
            print("==========================")
            print("        TEBAK ANGKA       ")
            print("==========================")
            print()
            print("1. Tebak Angka")
            print("2. Keluar")
            print("==========================")
            
            try:
                pilih = int(input("Silahkan Pilih: "))
            except ValueError:
                print("Input Hanya Angka!!")
                menu()
            
            if pilih == 1:
                app.tebak_angka()
            elif pilih == 2:
                jawab = input("Yakin Ingin Keluar Permainan (y/n) ?").lower()
                if jawab == "y":
                    exit()
                else:
                    menu()
            else:
                print("Pilihan Hanya Tersedia 1-2 !!")
    menu()