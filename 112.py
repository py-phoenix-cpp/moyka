import string
import random
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits


all = lower+upper+num

temp = random.sample(all, 11)

password = "".join(temp)

# qr_img = qrcode.make(password)
# qr_img.save(f'{"name"},{"car_number"}qr_code.jpg')
#
# qrcode_img = qrcode.make(password)
# canvas = Image.new('RGB', (300, 300), 'white')
# draw = ImageDraw.Draw(canvas)
# canvas.paste(qrcode_img)
# fname = f'{self.name}, {self.car_number} qr_code' + '.png'
# buffer = BytesIO()
# canvas.save(buffer, 'PNG')
# self.card_id.save(fname, File(buffer), save=False)
# canvas.close()
# super().save(*args, **kwargs)