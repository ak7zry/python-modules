from PIL import Image, ImageDraw

# operasi dasar gambar
# pastikan ada gambar untuk demo

print("=======================================")
print("              PACKAGE PILLOW"           )
print("=======================================")

# buat gambar baru (background)
img = Image.new('RGB', (400,300), color='Lightblue')

# tambahkan teks
draw = ImageDraw.Draw(img)
draw.text((50,50), "Hello, Pill!", fill='black')            # buat teks
draw.rectangle([50,100,350,200], outline='red', width=3)    # buat persegi panjang garis warna merah
draw.ellipse([100,150,300,250], fill='yellow')              # buat eclips fill kuning

# simpan gambar
img.save("demo_image.png")
print(" Demo Image Created : demo_image.png")
print("=======================================")