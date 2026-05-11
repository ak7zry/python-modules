# modules perhitungan matematika

# variabel yang bisa digunakan
# kebiasan programmer python, variabel pakai huruf kapital
PI = 3,14159

PEMBUAT = "Tim Matematika"


def tambah(a,b):
    """fungsi tambah 2 angka"""
    return a + b

def kurang(a,b):
    """
    fungsi kurang 2 angka
    """
    return a - b

def kali(a,b):
    """fungsi kali 2 angka"""
    return a * b

def bagi(a,b):
    """fungsi bagi 2 angka"""
    if b != 0:
        return a / b
    else:
        return "Error: Angka Tidak Bisa Dibagi Nol !!"

# untuk antisipasi jika modules ini dijalakan sebagai program python
if __name__ == "__main__":
    print("File Ini Tidak Bisa Dijalankan Sebagai Modules !!")