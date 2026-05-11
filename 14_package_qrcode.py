import qrcode

# membuat qr code
img = qrcode.make('https://pypi.org/project/qrcode/')

# simpan qr code
img.save("qr_pzn.png")