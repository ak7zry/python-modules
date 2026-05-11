===========================================================================================
                                        MODULES
===========================================================================================

-------------------------------------------------------------------------------------------
                          >>  STRUKTUR KODE YANG BAIK  << 
-------------------------------------------------------------------------------------------
>> import : gunakan awal file
>> constant / variable
>> function
>> __main__
-------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------
                                 >>  MODULE BUATAN SENDIRI  << 
-------------------------------------------------------------------------------------------
>> file python berisi function, variables dan statemet yang bisa digunakan program lain
>> keuntungan :
    ^^ code reuse    : tidak perlu menulis ulang function
    ^^ organization  : membagi code menjadi file-file yang mudah dikelola
    ^^ collaboration : bisa bekerja sama dengan tim pada file berbeda
    ^^ maintenance   : mudah mencari dan memperbaiki bug
    ^^ readability   : code lebih mudah dibaca

>> menggunakan MODULES : 
    ^^ import (nama file tanpa .py)
    ^^ menggunakan function / variabel dalam modules harus menyebutkan nama modules dulu

>> antisipasi modules dijalankan sebagai program utama :
    ^^ __name__ == string __main__
    ^^ penggunaan :
        if __name__ == "__main__":
            print("File Ini Tidak Dapat Dijalankan Sebagai Program Python")

>> docstring :
    ^^ menjelaskan kegunaan dari function / variabel yg dibuat di modules
    ^^ gunakan tanda petik (""") 3 kali

>> metode import modules (program_matematika.py) :
    ^^ import : import seluruh isi modules (WARNING) :
        && import module harus sebut nama modules
        && from nama_module import * == import module tanpa harus sebut nama module
        && WARNING == JIKA ADA NAMA FUNCTION/VARIABLE MODULE BENTROK DENGAN FUNCTION/VARIABLE DI FILE UTAMA
    ^^ import function tertentu :
        && untuk satu function                       == from nama_module import function_name
        && untuk dua function gunakan tanda koma(,)  == from nama_module import function_name, variable_name
        && bisa gunakan function / variabel dala modules tanpa sebut nama_module 
    ^^ import dengan alias (alias.py) :
        && kadang nama modules sama dengan module yang lain, bisa akali dengan alias (nama lain)
        && import nama_module as alias >>> bisa akses seluruh isi module dengan alias

-------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------
                                 >>  MODULE STANDARD LIBRARY  << 
-------------------------------------------------------------------------------------------
>> Python Standard Library : kumpulan modules yg sudah tersedia secara default pada python
>> Tanpa Install Tambahan

1. Module Math - Operasi Matemamatika 
    https://docs.python.org/3/library/math.html

2. Module Random - Angka dan Pilihan Acak
    https://docs.python.org/3/library/random.html

3. Module Datetime - Tanggal dan Waktu
    https://docs.python.org/3/library/datetime.html

4. Module OS - Operasi Sistem
    https://docs.python.org/3/library/os.html

5. Module JSON - Javascript Object Notation
    https://www.json.org/
    https://docs.python.org/3/library/json.html


-------------------------------------------------------------------------------------------