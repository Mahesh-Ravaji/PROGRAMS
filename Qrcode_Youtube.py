import qrcode 
from PIL import image
qr=qrcode.QRCode (version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=10,border=10,)
qr.add_data("https://www.youtube.com/channel/UCZmuhoeVNChsiaHQkCSgIHA")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("wscube_web.png")