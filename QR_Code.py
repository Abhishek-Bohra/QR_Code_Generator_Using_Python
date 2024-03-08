# QR Code  of any website Using Python

import qrcode as qr
img=qr.make("https://openai.com/")
img.save("Open_AI.Png")