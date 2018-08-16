from PIL import Image
import numpy
import matplotlib.pyplot as plt

def load_image(file):
    im = Image.open(file)
    return im

def image_to_array(im):
    arr = numpy.array(im.convert('RGB'))

    return arr

def array_to_image(arr):
    im = Image.fromarray(arr).convert('RGB')
    return im

def print_image(im):
    print(im.size)
    (x, y) = im.size
    for i in range(0, x):
        for j in range(0, y):
            print(im.getpixel((i, j)), end=',')
        print('')

def image_arr_huidu(arr):
    arr.flags.writeable = 1
    rows, cols, dies = arr.shape
    # 灰度化
    for i in range(rows):
        for j in range(cols):
            gr = 0.299 * arr[i, j, 0] + 0.578 * arr[i, j, 1] + 0.114 * arr[i, j, 2]
            arr[i, j, 0] = gr
            arr[i, j, 1] = gr
            arr[i, j, 2] = gr

    arr.flags.writeable = 0
    return arr

def image_arr_erzhi(arr):
    arr.flags.writeable = 1
    rows, cols, dies = arr.shape
    #二值化
    for i in range(rows):
        for j in range(cols):
            if (arr[i, j, 0] > 140):
                arr[i, j, 0] = 255
                arr[i, j, 1] = 255
                arr[i, j, 2] = 255
            else:
                arr[i, j, 0] = 0
                arr[i, j, 1] = 0
                arr[i, j, 2] = 0

    arr.flags.writeable = 0
    return arr

def image_arr_do(arr):
    arr = image_arr_huidu(arr)
    arr = image_arr_erzhi(arr)

    return arr


def save_image(im,sfile):
    im.save(sfile,'PNG')

if __name__ == '__main__':
    im = load_image('D:\\MyCode\\vc_pic\\vc.png')
    arr = image_to_array(im)
    arr = image_arr_do(arr)
    im2 = array_to_image(arr)
    print_image(im2)
    save_image(im2,'D:\\MyCode\\vc_pic\\vc_123.png')
    plt.figure("beauty")
    plt.imshow(im2)
    plt.axis('off')
    plt.show()


