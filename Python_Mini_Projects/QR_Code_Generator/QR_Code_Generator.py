# To Make the QR Code of any website

import qrcode as qr
img = qr.make("https://bhuvneshjai.github.io/Business-Website/")
img.save("Business Website.png")