## ==============================================================================
##                                               PACKAGE
## ==============================================================================

## ------------------------------------------------------------------------------
##                                   READ ME
## ------------------------------------------------------------------------------
## ^^ package = folder berisi modules
## ^^ package = mengorganisisr file-file python yang berkaitan
## ^^ package = membantu mengkelompokkan moduke berdasarkan fungsi/tema
## ------------------------------------------------------------------------------

## ------------------------------------------------------------------------------
##                           STRUKTUR PACKAGE SEDERHANA
## ------------------------------------------------------------------------------
## nama_package/    : direktori/folder package
## __init__.py      : file khusus penanda ini adalah package >> WAJIB ADA [walapun file kosong]
## module1.py       : Module 1    
## module2.py       : Module 2    
## module3.py       : Module 3    
## ------------------------------------------------------------------------------

## matematika_package/__init__.py
## file ini = package
## bisa kosong / infomasi package

__version__ = "1.0.0"
__author__ = "Tim Matematika"

print("ini adalah file package : matematika_package")

