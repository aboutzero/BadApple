from PIL import Image
import os

filepath = './pictures/'
dir = os.listdir(filepath)

out = './out/'
if not os.path.exists(out):
    os.makedirs(out)


def img_resize(inpath, outpath, name):
    img = Image.open(inpath)
    img = img.resize((128, 64), Image.NEAREST, None, None)
    img = img.convert('1')
    img.save(outpath+name+'.bmp', 'bmp')


if __name__ == '__main__':
    i = 0
    for file in dir:
        img_resize(filepath+file, out, str(i))
        i += 1
    print('complete!')
