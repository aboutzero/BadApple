from PIL import Image
import os
import numpy as np


filepath = './out2/'
dir = os.listdir(filepath)


def change_byte(input, output, name):
    img = Image.open(input)
    if not os.path.exists(output):
        os.mkdir(output)

    h, w = img.size
    if not os.path.exists(output+name):
        os.system('cd >'+output+name)
    f = open(output+name, 'r+')
    for i in range(h):
        for j in range(w):
            if img.getpixel((i, j)) == 0:
                f.write(str(0))
            else:
                f.write(str(1))
            if j == w-1:
                f.write('\n')
    f.close()
    # print(name)


if __name__ == '__main__':
    for k in dir:
        m = k.replace('.bmp', '.txt')
        print(m)
        change_byte(filepath+k, './bmp2/', m)
