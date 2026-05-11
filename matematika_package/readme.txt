==============================================================================
                                              PACKAGE
==============================================================================

------------------------------------------------------------------------------
                                  READ ME
------------------------------------------------------------------------------
^^ package = folder berisi modules
^^ package = mengorganisisr file-file python yang berkaitan
^^ package = membantu mengkelompokkan moduke berdasarkan fungsi/tema
------------------------------------------------------------------------------

------------------------------------------------------------------------------
                          STRUKTUR PACKAGE SEDERHANA
------------------------------------------------------------------------------
nama_package/    : direktori/folder package
__init__.py      : file khusus penanda ini adalah package >> WAJIB ADA [walapun file kosong]
module1.py       : Module 1    
module2.py       : Module 2    
module3.py       : Module 3    
------------------------------------------------------------------------------

matematika_package/__init__.py
file ini = package
bisa kosong / infomasi package

------------------------------------------------------------------------------
                          MENGGUNAKAN PACKAGE
------------------------------------------------------------------------------
^^ import seluruh module :
    from matematika_package import dasar
^^ impor member tertentu :
    from matematika_package import tambah, kali
^^ import dengan alias :
    from matematika_package import dasar as math_dasar
^^ mempermudah untuk maintenance koding
^^ disarankan menggunakan package jika module sudah banyak
^^ mempermudah 
------------------------------------------------------------------------------

------------------------------------------------------------------------------
                          SUB PACKAGE
------------------------------------------------------------------------------
^^ jika aplikasi kompleks perlu membuat banyak package
^^ bisa juga membuat sub package (package di dalam package)
^^ contoh sub package:
    
    aplikasi_sekolah/
    __init__.py
    matematika/
        __init__.py
        artimatika.py
        geometri.py
    fisika/
        __init__.py
        mekanika.py
        termodinamika.py
    kimia/
        __init__.py
        organik.py
        anorganik.py

^^ cara panggil : aplikasi_sekolah.matematika
------------------------------------------------------------------------------