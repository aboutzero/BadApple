from PIL import Image
import os

filepath='./out/'
dir=os.listdir(filepath)
out='./out2/'


def rotate_img(input,output,name):
	if not os.path.exists(output):
		os.makedirs(output)
	img=Image.open(input)
	img=img.transpose(Image.ROTATE_90)
	img.save(output+name)


if __name__=='__main__':
	for i in dir:
		rotate_img(filepath+i,out,i)