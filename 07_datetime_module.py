# import datetime module

import datetime

# menampilkan tanggal dan waktu lengkap
sekarang = datetime.datetime.now()
print("Datetime:", sekarang)

# menampilkan tanggal
tgl = datetime.date.today()
print("Hari Ini Tanggal:", tgl)

# menampilkan waktu
jam = datetime.datetime.now().time()
print("Waktu Sekarang:", jam)

# menampilkan tanggal tertentu
thn = datetime.date(2025, 5, 4)              # tahun, bulan, tanggal
print("Tanggal Ulang Tahun:", thn)

# menampilkan waktu tertentu
wkt = datetime.datetime(2025, 10,2,15,35,0)  # tahun, bulan, tanggal, jam, menit, detik
print("Jam:", wkt)

# format indonesia >> strftime (string format time)
print("Format Indonesia :", sekarang.strftime("%d/%m/%y %H:%M:%S"))

# format panjang
print("Format Panjang:", sekarang.strftime("%A, %d %B %Y"))


