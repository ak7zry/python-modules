#===================================== 
# import json ke tipe data di python
#===================================== 

import json

file = open("contoh.json", "r") # open file json
text = file.read()              # read file json
file.close()                    # close file json


print("=======================================")
print("  IMPORT JSON TO DATA TYPE ON PYTHON   ")
print("=======================================")
print()
print(text)
# hasil print(text):
# {
#     "nama": "eko",
#     "umur": "38",
#     "alamat":  "jakarta"
# }
print("---------------------------------------")

# bisa ambil data json sesuai yang kita mau >> get

murid = json.loads(text)
print(type(murid))  # == class : dictionary
print(murid.get("nama"))      # eko
print(murid.get("umur"))      # 38
print(murid.get("alamat"))    # jakarta

#=====================================================
#          IMPORT DATA TYPE IN PYTHON TO JSON
#=====================================================

sekolah = {
    "nama"   : "Universitas Programmer Zaman Now",
    "alamat" : "Jakarta",
    "Jurusan": [
        "Teknik Komputer",
        "Sistem Informasi",
        "Akuntansi"
    ]
}

text_json = json.dumps(sekolah)
print("------------------------------------------------")
print("=====================================================")
print("          IMPORT DATA TYPE IN PYTHON TO JSON         ")          
print("=====================================================")
print()
print(text_json) 
# hasil print(text_json) :
# {"nama": "Universitas Programmer Zaman Now", "alamat": "Jakarta", "Jurusan": ["Teknik Komputer", "Sistem Informasi", "Akuntansi"]}

## simpan ke file json
file = open("sekolah.json", "w")  # buat file sekolah.json
file.write(text_json)             # tulis di file sekolah.json
file.close()                      # tutup file
