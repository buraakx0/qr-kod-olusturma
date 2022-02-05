import qrcode

buraak = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, 
    border=4,
)
buraak.add_data('https://github.com/buraakx0') # buraya qr code okutulunca hangi siteye yönlendireceğini giriyoruz.
buraak.make(fit=True)

img = buraak.make_image(fill_color="black", back_color="white") # black ve white yazan kısımlara istediğiniz renkleri girebilirsiniz.
img.save("buraak.png") # buraya dosyamızın ne diye kaydedileceğini giriyoruz. 