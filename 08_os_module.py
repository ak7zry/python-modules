# import module os

import os

# menampilkan direktori
print("Direktori Kerja Saat ini:", os.getcwd())

# informasi sistem
# 'nt' = windows , 'posix' = linux/unix/mac
print("Nama Sistem:", os.name)

# cek file/direktori ada = true, tidak ada = false
print("File ada:", os.path.exists("modules.txt"))
print("Direktori Ada:", os.path.exists("python-modules"))

# informasi file
if os.path.exists("modules.txt"):
    print("Adalah File:", os.path.isfile("modules.txt"))
    print("Adalah Direktori:", os.path.isdir("python-modules"))
    print("Ukuran File:", os.path.getsize("modules.txt"), "bytes")
    
    
# operasi path
file_path = "D:\ISI\Python\python-modules"
print("Direktori:", os.path.dirname(file_path))
print("Nama File:", os.path.basename(file_path))
print("Nama Tanpa Ekstensi:", os.path.splitext(file_path)[0])
print("Ekstensi:", os.path.splitext(file_path)[1])
