import qrcode as qr

img= qr.make("https://www.youtube.com/watch?v=41OTXkcisrQ")
img.save("wscube_youtube.png")