# To Make the QR Code Colorful

import qrcode as q
from PIL import Image
qr = q.QRCode(version=1,
              error_correction=q.constants.ERROR_CORRECT_H,
              box_size=10,
              border=10)
qr.add_data("https://bhuvneshjai.github.io/Business-Website/")
qr.make(fit=True)
img = qr.make_image(fill_color="white",
                    back_color="Black")
img.save("Business_Website.png")