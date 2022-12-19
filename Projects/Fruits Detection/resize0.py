import PIL

import os
import os.path
from PIL import Image
f=r'C:\Users\admin\Desktop\Fruits\My Data\10'
for file in os.listdir(f):
    f_img=f+"/"+file
    img=Image.open(f_img)
    img=img.resize((32,32))
    img.save(f_img)
    