import os
import time

path = './bmp2/'
dir = os.listdir(path)


def code(input, name):
    name = str(name)+'.txt'
    f = open(input+name, mode='r', newline='\n')
    txt = f.readlines()
    for j in txt:
        print(j)
    f.close()


if __name__ == '__main__':
    i = 0
    for i in range(6571):
        code(path, i)
        time.sleep(1/30)
        i += 1
