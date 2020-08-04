import cv2


def zh_ch(string):
    return string.encode("gbk").decode(errors="ignore")


# 图像腐蚀
def erode():
    cv2.imshow(zh_ch("【原图】腐蚀操作"), srcImage)

    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    element3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

    dstImage1 = cv2.erode(srcImage, element1)
    dstImage2 = cv2.erode(srcImage, element2)
    dstImage3 = cv2.erode(srcImage, element3)
    cv2.imshow(zh_ch("【效果图】腐蚀操作-RECT"), dstImage1)
    cv2.imshow(zh_ch("【效果图】腐蚀操作-ELLIPSE"), dstImage2)
    cv2.imshow(zh_ch("【效果图】腐蚀操作-CROSS"), dstImage3)
    cv2.waitKey(0)


# 图像模糊
def blur():
    cv2.imshow(zh_ch("原图-模糊操作"), srcImage)

    dstImage = cv2.blur(srcImage, (7, 7))

    cv2.imshow(zh_ch("效果图-均值滤波"), dstImage)

    cv2.waitKey(0)


# 边缘检测
def canny():
    cv2.imshow(zh_ch("原图-边缘检测"), srcImage)

    grayImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    cv2.imshow('效果图-灰度图', grayImage)

    blurImage = cv2.blur(grayImage, (3, 3))
    cv2.imshow('效果图-模糊', blurImage)

    cannyImage = cv2.Canny(blurImage, 30, 70)
    cv2.imshow('效果图-边缘检测', cannyImage)

    cv2.waitKey(0)
    # 先阈值分割后检测



# do nothing
def callbackme(*arg):
    print("触发回调")


if __name__ == '__main__':
    srcImage = cv2.imread("cat.102.jpg")
    erode()
    blur()
    canny()
