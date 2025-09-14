import imageio.v2 as imageio
import numpy as np
from PIL import Image

filenames = ['1.jpg', '2.jpg', '3.jpg']
images = []

# İlk resmi baz alarak boyut al
base_img = Image.open(filenames[0])
width, height = base_img.size

for filename in filenames:
    img = Image.open(filename).resize((width, height))  # tüm resimleri aynı boyuta getir
    images.append(np.array(img))

# GIF oluştur
imageio.mimsave('out.gif', images, duration=500, loop=0)  # saniye cinsinden süre