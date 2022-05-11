from PIL import Image
from pyzbar.pyzbar import decode
import os

path_dir = 'qr/'
file_list = os.listdir(path_dir)
print (file_list)

num = 0
for i in file_list:
    print(file_list[num] + " : " + decode(Image.open("qr/"+i))[0].data.decode())
    num += 1