from post_and_comments import post

if __name__ == "__main__":
    while True:
       print("====================================") 
       print("1. Daftar Post")
       print("2. Keluar")
       print("====================================")
       
       pilihan = int(input("Masukkan Pilihan: "))
       if pilihan == 1:
           post.menu_post()
       elif pilihan == 2:
           print("Program Selesai")
           break
        