import requests

def menu_comment(post_id):
    while True:
     print("=================================")
     print("           MENU COMMENTS         ")   
     print("=================================")
     print(f"1. Tampilkan Semua Comments Dari Post {post_id}")
     print(f"2. Tampilkan Comments Berdasarkan ID Comments Dari Post {post_id}")
     print("3. Keluar")
     
     pilihan = int(input("Masukkan Pilihan: "))
     
     if pilihan == 1:
         tampilkan_semua_comment(post_id)
     elif pilihan == 2:
         comment_id = int(input("Masukkan ID Comment: "))
         tampilkan_comment_berdasarkan_id(post_id, comment_id)
     elif pilihan == 3:
         print("Selesai")
         break

def ambil_semua_comment(post_id):
    respon = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    if respon.status_code == 200:
        list = respon.json()
        return list
    else:
        print("Data Tidak Ditemukan")
        return[]
    
def tampilkan_semua_comment(post_id):
    list_comment = ambil_semua_comment(post_id)
    for comment in list_comment:
        print("==========================================================")
        print(f"ID Comments: {comment['id']}")
        print(f"Name: {comment['name']}")

def tampilkan_comment_berdasarkan_id(post_id, comment_id):
    respon = requests.get(f"https://jsonplaceholder.typicode.com/comments/{comment_id}")
    if respon.status_code == 200:
        data = respon.json()
        if data["postId"] == post_id:
            print("==========================================================")
            print(f"ID Comments: {data['id']}")
            print(f"Name: {data['name']}")
            print(f"Body: {data['body']}")
        else:
            print("ID Commnent Tidak Sesuai")
    else:
        print("Data Tidak Ditemukan")
        