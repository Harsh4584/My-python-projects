#YE NORMAL QR CODE H BLACK AND WHITE

# import qrcode as qr
# img = qr.make("https://replit.com/@harshjangidjee/82-Day-82-Exercise-8-Solution")
# img.save("Day80.png")


# YE MODERN QR CODE H

import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=6,)
qr.add_data("https://www.youtube.com/watch?v=0U9-KUx0SD8")
qr.make(fit=True)
img = qr.make_image(fill_color = "black", back_color = "orange")
img.save("OWN WEBSITE.png")