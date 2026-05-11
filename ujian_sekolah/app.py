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
         
def ambil_soal(lokasi_file):
    soal_asli = []
    with open(lokasi_file, "r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli
#----------------------------------------------------------------------------------------
#Tampilkan soal : diambil dari ambil_soal() disimpan variabel soal_asli
# soal_asli = ambil_soal()
# print(soal_asli)
#----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#  menampilkan soal + jawaban benar dalam bentuk list >> nantinny akan di modif dalam bentuk def buat_soal()
#------------------------------------------------------------------------------------------------------------
# soal_asli = ambil_soal()
#     # print(soal_asli) >> tampil soal di bank_soal.txt
# for soal in soal_asli:
#         data = soal.split("|")
#         pertanyaan = data[0]
#         semua_jawaban = data[1]
#         jawaban = semua_jawaban.split(",")
#         jawaban_benar = jawaban[0]
        
#         #tampikan soal + jawaban benar
#         print("Pertanyaan", pertanyaan)
#         print("Jawaban", semua_jawaban)
#         print("jawaban benar", jawaban_benar)
#---------------------------------------------------------------------------------------------------------------------
def buat_soal(lokasi_file):
    soal_asli = ambil_soal(lokasi_file)
    # acak soal yg sudah dalam bentuk list
    import random
    random.shuffle(soal_asli) #shuffle untuk acak data dalam list
    
    soal_ujian = []
    for i in range(10):
        soal = soal_asli[i]        # ambil soal >> pertanyaan|jawaban1, jawaban2, jawaban3,jawaban4
        data = soal.split("|")     # list >> [pertanyaan, "jawaban1,jawaban2,jawaban3,jawaban4"]
             
        pertanyaan = data[0]       # pertanyaan
        semua_jawaban = data[1]    # string >> "jawaban1,jawaban2,jawaban3,jawaban4"
        
        jawaban = semua_jawaban.split(",")      # ["jawaban1", "jawaban2", "jawaban3", "jawaban4"]
        jawaban_benar = jawaban[0]              # "jawaban1"
        random.shuffle(jawaban)                 # acak jawaban1 >> pindah posisi acak
        
        # append data dictionary
        soal_ujian.append({
            "pertanyaan" : pertanyaan,
            "jawaban" : jawaban,
            "jawaban_benar" : jawaban_benar
        })
        
    return soal_ujian

#----------------------------------------------------------------------------------------------------------------------------------------------
# BAHASA INDONESIA
#----------------------------------------------------------------------------------------------------------------------------------------------
def ambil_soal_indo(lokasi_file):
    soal_asli_indo = []
    with open(lokasi_file, "r") as file:
        for line in file:
            soal_asli_indo.append(line.strip())
    return soal_asli_indo

def buat_soal_indo(lokasi_file):
    soal_asli_indo = ambil_soal_indo(lokasi_file)
    #acak soal yang sudah ada dlam bentuk list
    import random
    random.shuffle(soal_asli_indo)
    
    soal_ujian_indo = []
    for a in range(10):
        soal = soal_asli_indo[a]
        data = soal.split("|")
        
        pertanyaan = data[0]
        semua_jawaban = data[1]
        
        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]
        random.shuffle(jawaban)
        
        #append data dictionary
        soal_ujian_indo.append({
            "pertanyaan" : pertanyaan,
            "jawaban" : jawaban,
            "jawaban_benar" : jawaban_benar
        })
    return soal_ujian_indo

#----------------------------------------------------------------------------------------------------------------------------------------------
# PKN / KEWARGANEGARAAN
#----------------------------------------------------------------------------------------------------------------------------------------------
def ambil_soal_pkn(lokasi_file):
    soal_asli_pkn = []
    with open(lokasi_file, "r") as file:
        for line in file:
            soal_asli_pkn.append(line.strip())
    return soal_asli_pkn

def buat_soal_pkn(lokasi_file):
    soal_asli_pkn = ambil_soal_pkn(lokasi_file)
    #acak soal yang sudah ada dlam bentuk list
    import random
    random.shuffle(soal_asli_pkn)
    
    soal_ujian_pkn = []
    for a in range(10):
        soal = soal_asli_pkn[a]
        data = soal.split("|")
        
        pertanyaan = data[0]
        semua_jawaban = data[1]
        
        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]
        random.shuffle(jawaban)
        
        #append data dictionary
        soal_ujian_pkn.append({
            "pertanyaan" : pertanyaan,
            "jawaban" : jawaban,
            "jawaban_benar" : jawaban_benar
        })
    return soal_ujian_pkn

#----------------------------------------------------------------------------------------------------------------------------------------------
# BAHASA INGGRIS
#----------------------------------------------------------------------------------------------------------------------------------------------
def ambil_soal_ingris(lokasi_file):
    soal_asli_ingris = []
    with open(lokasi_file, "r") as file:
        for line in file:
            soal_asli_ingris.append(line.strip())
    return soal_asli_ingris

def buat_soal_ingris(lokasi_file):
    soal_asli_ingris = ambil_soal_ingris(lokasi_file)
    #acak soal yang sudah ada dlam bentuk list
    import random
    random.shuffle(soal_asli_ingris)
    
    soal_ujian_ingris = []
    for a in range(10):
        soal = soal_asli_ingris[a]
        data = soal.split("|")
        
        pertanyaan = data[0]
        semua_jawaban = data[1]
        
        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]
        random.shuffle(jawaban)
        
        #append data dictionary
        soal_ujian_ingris.append({
            "pertanyaan" : pertanyaan,
            "jawaban" : jawaban,
            "jawaban_benar" : jawaban_benar
        })
    return soal_ujian_ingris



    
        