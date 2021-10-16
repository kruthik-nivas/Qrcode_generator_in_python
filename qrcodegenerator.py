import qrcode
import image

qr= qrcode.QRCode(
    version = 15, #15 means version higher the number bigger the code
    box_size=10, #size of the box where qr code will be held
    border = 5,

)

data=input()
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")