import requests
from post_and_comments import comments

def menu_post():
    while True:
     print("=================================")
     print("             MENU POST           ")   
     print("=================================")
     print("1. Tampilkan Semua Post")
     print("2. Tampilkan Post Berdasarkan ID")
     print("3. Keluar")
     
     pilihan = int(input("Masukkan Pilihan: "))
     
     if pilihan == 1:
         tampilkan_semua_post()
     elif pilihan == 2:
         post_id = int(input("Masukkan ID Post: "))
         tampilkan_post_berdasarkan_id(post_id)
         comments.menu_comment(post_id)
     elif pilihan == 3:
         print("Selesai")
         break
        
        
        

def ambil_semua_post():
    respons = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    # cek respons jika berhasil
    if respons.status_code == 200: 
       list = respons.json()
       return list
    else:
        print("Data Tidak Ditemukan")
        return[]
    
def tampilkan_semua_post():
    list_post = ambil_semua_post()
    for post in list_post:
        print("===========================================")
        print(f"ID Post: {post['id']}")
        print(f"Title: {post['title']}")
        
def tampilkan_post_berdasarkan_id(post_id):
    respon = requests.get(f"https://jsonplaceholder.typicode.com/post/{post_id}")
    
    if respon.status_code == 200:
        data = respon.json()
        print("===========================================")
        print(f"ID Post: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print("Data Tidak Ditemukan")