import qrcode
import image
features = qrcode.QRCode(version = 15, box_size = 10, border = 5)

data = "https://github.com/Pratham1514"

features.add_data(data)
features.make(fit=True)
img = features.make_image(fill = "black", back_color = "white")
img.save("GITHUB.png")