# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 17:51
# @Author  : Apokar
# @Email   : Apokar@163.com
# @File    : opencv_yprac.py
# @Comment :

# 黑暗中拍的图片增亮

import cv2
import matplotlib.pyplot as plt
import numpy as np


img_path = r"D:\work\PycharmProjects\photo_mark\dataset\Image0628_Label\1c3afa7e3746369d7250913c3a67c915.jpg"

def show(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()


def imread(image):
    image=cv2.imread(image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image


def add_liangdu():
    dark_img = imread(img_path)
    # show(dark_img)

    print(dark_img.shape)
    #生成和图像shape相同的图片，且全为100的数据
    M=np.ones(dark_img.shape,dtype='uint8')*100
    image=cv2.add(M,dark_img)

    show(image)

# 彩色图像进行直方图均衡化


def get_yuv_image():
    """
    YUV色彩空间是把亮度（Luma）与色度（Chroma）分离。
    “Y”表示亮度，也就是灰度值。
    “U”表示蓝色通道与亮度的差值。
    “V”表示红色通道与亮度的差值。

    对彩色图像进行直方图均衡化时，先将图像从RGB空间转到YUV空间，然后对亮度Y通道进行直方图均衡化得到通道Y"，然后将Y"UV通道进行合并。
    """

    dark_img = imread(img_path)
    img_yuv = cv2.cvtColor(dark_img, cv2.COLOR_BGR2YUV)

    # 均衡Y通道的直方图
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

    # 将yuv图像转换回rgb格式
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    show(dark_img)
    show(img_output)



if __name__ == '__main__':
    add_liangdu() # 1
    get_yuv_image() # 2
