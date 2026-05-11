#==========================================================================
#                        APLIKASI UJIAN SEKOLAH
#==========================================================================
#--------------------------------------------------------------------------
#                                  RULE
#--------------------------------------------------------------------------
# ^^ MEMBACA SOAL DARI FILE
# ^^ MENGACAK SOAL UJIAN
# ^^ MENAGCAK POSISI JAWABAN
# ^^ TAMPIL HASIL SCORE
#--------------------------------------------------------------------------

#-------------------------------------------
# menampilkan soal di file bank_soal.txt
#-------------------------------------------
# file = open("bank_soal.txt", "r")

# soal_asli =[]
# for line in file:
#     soal_asli.append(line.strip())
#     print(line.strip())   
#-------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
# MATEMATIKA
#----------------------------------------------------------------------------------------------------------------------------------------------
         
from ujian_sekolah import app     

    
if __name__ == "__main__" :         
    def ujian():
        print("==================================================")
        print("                  SOAL MATEMATIKA                 ")
        print("==================================================")
        soal_ujian = app.buat_soal("soal_matematika.txt")
        opsi = ["A", "B", "C", "D"]   # membuat pilihan ganda >> index 0,1,2,3
        
        # variable untuk menyimpan inputan user
        jawaban_benar = 0
        jawaban_salah = 0
        
        for i in range(len(soal_ujian)):
            soal = soal_ujian[i]
            print("pertanyaan", i + 1, ":", soal["pertanyaan"])
            print("jawaban:")
            
            
            for j in range(len(soal["jawaban"])):
                jawaban = soal["jawaban"][j]
                print(opsi[j], ".",jawaban )
            
            try:
                jawaban_user = input("Pilih Jawaban (A/B/C/D): ").upper()
                jawaban_user_index = opsi.index(jawaban_user)   # mencari tahu jawaban user index ke berapa
                jawaban_asli_user = soal["jawaban"][jawaban_user_index]
            except:
                print("Input Tidak Sesuai!!, Silahkan Input Ulang Sesuai Format [A/B/C/D]")
                break
            else:   
                if jawaban_asli_user == soal["jawaban_benar"]:
                    print("Jawaban Benar")
                    jawaban_benar += 1
                else:
                    print("Jawaban Salah")
                    jawaban_salah += 1 
                    
        print("==================================================")
        print("                    Hasil Ujian                   ")
        print("==================================================")
        print("Jawaban Benar:", jawaban_benar)
        print("Jawaban Salah:", jawaban_salah)
        print("Hasil Ujian:", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")
        print("==================================================")
        print(input("Silahkan Tekan Enter Untuk Kembali Ke Menu: "))
    # ujian()
    #----------------------------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------------------------
    # BAHASA INDONESIA
    #----------------------------------------------------------------------------------------------------------------------------------------------

    def ujian_indo():
        print("==================================================")
        print("              SOAL BAHASA INDONESIA               ")
        print("==================================================")
        print()
        soal_ujian_indo = app.buat_soal_indo("soal_indo.txt")
        opsi = ["A", "B", "C", "D"]
        
        #variabel untuk simpan input user
        jawaban_benar = 0
        jawaban_salah = 0
        
        for a in range(len(soal_ujian_indo)):
            soal = soal_ujian_indo[a]
            print("pertanyaan", a + 1, ":", soal["pertanyaan"])
            print("jawaban:")
            
            for b in range(len(soal["jawaban"])):
                jawaban = soal["jawaban"][b]
                print(opsi[b], "." ,jawaban)
                
            try:
                jawaban_user = input("Pilih Jawaban (A/B/C/D): ").upper()
                jawaban_user_index = opsi.index(jawaban_user)
                jawaban_asli_user = soal["jawaban"][jawaban_user_index]
            except:
                print("Input Tidak Sesuai!!, Silahkan Input Ulang Sesuai Format [A/B/C/D]")
                break
            else:
                if jawaban_asli_user == soal["jawaban_benar"]:
                    print("Jawaban Benar")
                    jawaban_benar += 1
                else:
                    print("Jawaban Salah")
                    jawaban_salah += 1
        print("==================================================")
        print("                    Hasil Ujian                   ")
        print("==================================================")
        print("Jawaban Benar:", jawaban_benar)
        print("Jawaban Salah:", jawaban_salah)
        print("Hasil Ujian:", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")
        print("==================================================")
        print(input("Silahkan Tekan Enter Untuk Kembali Ke Menu: "))
    #----------------------------------------------------------------------------------------------------------------------------------------------


    #----------------------------------------------------------------------------------------------------------------------------------------------
    # PKN / KEWARGANEGARAAN
    #----------------------------------------------------------------------------------------------------------------------------------------------

    def ujian_pkn():
        print("==================================================")
        print("              SOAL KEWARGANEGARAAN                ")
        print("==================================================")
        print()
        soal_ujian_pkn = app.buat_soal_pkn("soal_pkn.txt")
        opsi = ["A", "B", "C", "D"]
        
        #variabel untuk simpan input user
        jawaban_benar = 0
        jawaban_salah = 0
        
        for a in range(len(soal_ujian_pkn)):
            soal = soal_ujian_pkn[a]
            print("pertanyaan", a + 1, ":", soal["pertanyaan"])
            print("jawaban:")
            
            for b in range(len(soal["jawaban"])):
                jawaban = soal["jawaban"][b]
                print(opsi[b], "." ,jawaban)
                
            try:
                jawaban_user = input("Pilih Jawaban (A/B/C/D): ").upper()
                jawaban_user_index = opsi.index(jawaban_user)
                jawaban_asli_user = soal["jawaban"][jawaban_user_index]
            except:
                print("Input Tidak Sesuai!!, Silahkan Input Ulang Sesuai Format [A/B/C/D]")
                break
            else:
                if jawaban_asli_user == soal["jawaban_benar"]:
                    print("Jawaban Benar")
                    jawaban_benar += 1
                else:
                    print("Jawaban Salah")
                    jawaban_salah += 1
        print("==================================================")
        print("                    Hasil Ujian                   ")
        print("==================================================")
        print("Jawaban Benar:", jawaban_benar)
        print("Jawaban Salah:", jawaban_salah)
        print("Hasil Ujian:", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")
        print("==================================================")
        print(input("Silahkan Tekan Enter Untuk Kembali Ke Menu: "))
    #----------------------------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------------------------
    # BAHASA INGGRIS
    #----------------------------------------------------------------------------------------------------------------------------------------------
    def ujian_ingris():
        print("==================================================")
        print("              SOAL BAHASA INGGRIS                 ")
        print("==================================================")
        print()
        soal_ujian_ingris = app.buat_soal_ingris("soal_inggris.txt")
        opsi = ["A", "B", "C", "D"]
        
        #variabel untuk simpan input user
        jawaban_benar = 0
        jawaban_salah = 0
        
        for a in range(len(soal_ujian_ingris)):
            soal = soal_ujian_ingris[a]
            print("pertanyaan", a + 1, ":", soal["pertanyaan"])
            print("jawaban:")
            
            for b in range(len(soal["jawaban"])):
                jawaban = soal["jawaban"][b]
                print(opsi[b], "." ,jawaban)
                
            try:
                jawaban_user = input("Pilih Jawaban (A/B/C/D): ").upper()
                jawaban_user_index = opsi.index(jawaban_user)
                jawaban_asli_user = soal["jawaban"][jawaban_user_index]
            except:
                print("Input Tidak Sesuai!!, Silahkan Input Ulang Sesuai Format [A/B/C/D]")
                break
            else:
                if jawaban_asli_user == soal["jawaban_benar"]:
                    print("Jawaban Benar")
                    jawaban_benar += 1
                else:
                    print("Jawaban Salah")
                    jawaban_salah += 1
        print("==================================================")
        print("                    Hasil Ujian                   ")
        print("==================================================")
        print("Jawaban Benar:", jawaban_benar)
        print("Jawaban Salah:", jawaban_salah)
        print("Hasil Ujian:", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")
        print("==================================================")
        print(input("Silahkan Tekan Enter Untuk Kembali Ke Menu: "))
    #----------------------------------------------------------------------------------------------------------------------------------------------


    def menu():
        print()
    while True:
        print("============================================================================================")
        print("                                     UJIAN SEKOLAH DASAR                                    ")
        print("============================================================================================")
        print()
        print("--------------------------------------------------------------------------------------------")
        print("                                          Peraturan                                         ")
        print("--------------------------------------------------------------------------------------------")
        print("A. Sebelum Melakukan Ujian Sekolah Dasar, Peserta Harap Memilih Ujian Yang Akan Dilakukan")
        print("B. Peserta Memilih Ujian Pada Menu Ujian Sekolah Dasar")
        print("C. Hasil Ujian Akan Langsung Keluar Ketika Peserta Selesai Mengerjakan Soal")
        print("D. Soal Ujian Merupakan Pilihan Ganda")
        print("E. Soal Ujian Tiap Peserta Bersifat Acak")
        print("--------------------------------------------------------------------------------------------")
        print()
        print("==========================================")
        print("           Materi Ujian Sekolah           ")
        print("==========================================")
        print("1. Matematika")
        print("2. Bahasa Indonesian")
        print("3. Kewarganegaraan")
        print("4. Bahasa Inggris")
        print("5. Keluar")
        print("==========================================")
        print(" Silahkan Pilih Menu Ujian Dari No 1 - 5  ")
        print("==========================================")
    
        try:
            pilihan = int(input("Silahkan Pilih Menu: "))
        except ValueError:
            print("Kesalahan Input, Input Hanya Angka")
            print("==================================")
            menu()
        else:
            if pilihan == 1:
                ujian()
            elif pilihan == 2:
                ujian_indo()
            elif pilihan == 3:
                ujian_pkn()
            elif pilihan == 4:
                ujian_ingris()
            elif pilihan == 5:
                pilih = input("Apakah Akan Keluar Dari Aplikasi Ujian Sekolah (y/n) ? ")
                if pilih == "y":
                    exit()
                else:
                    menu()
            else:
                print("Kesalahan Input, Input Terdiri No 1 - 5")
                print("=======================================")
                menu()
        menu()
    
        