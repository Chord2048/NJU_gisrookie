# coding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

def linearStretch(src):
    smax = np.max(src)
    smin = np.min(src)
    dst = 255 * (src - smin) / (smax - smin)
    dst = np.uint8(dst + 0.5)
    return dst

def linearDividedStretch(src, x1, y1, x2, y2):
    x1, x2 = np.float(x1), np.float(x2)
    y1 = [np.float(i) for i in y1]
    y2 = [np.float(i) for i in y2]
    x = np.arange(256)
    #三通道查找表
    b_channel = np.zeros(256, dtype = np.float64)
    g_channel = np.zeros(256, dtype = np.float64)
    r_channel = np.zeros(256, dtype = np.float64)
    for i in x:
        if i < x1:
            b_channel[i] = (y1[0] * 1.0 / x1) * i
            g_channel[i] = (y1[1] * 1.0 / x1) * i
            r_channel[i] = (y1[2] * 1.0 / x1) * i
        elif i < x2:
            b_channel[i] = (y2[0] - y1[0]) / (x2 - x1) * (i - x1) + y1[0]
            g_channel[i] = (y2[1] - y1[1]) / (x2 - x1) * (i - x1) + y1[1]
            r_channel[i] = (y2[2] - y1[2]) / (x2 - x1) * (i - x1) + y1[2]
        else:
            b_channel[i] = (255 - y2[0]) / (255 - x2) * (i - x2) + y2[0]
            g_channel[i] = (255 - y2[1]) / (255 - x2) * (i - x2) + y2[1]
            r_channel[i] = (255 - y2[2]) / (255 - x2) * (i - x2) + y2[2]
    lut = np.dstack((b_channel,g_channel,r_channel))
    lut = np.uint8(lut+0.5)
    dst = cv2.LUT(src, lut)
    return dst

def disHist(src):
    # 计算直方图
    histb = cv2.calcHist([src], [0], None, [256], [0, 255])
    histg = cv2.calcHist([src], [1], None, [256], [0, 255])
    histr = cv2.calcHist([src], [2], None, [256], [0, 255])
    # 对第 1 子图进行设定
    plt.subplot(3, 1, 1)
    plt.plot(histb, 'b', label='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    # 对第 2 子图进行设定
    plt.subplot(3, 1, 2)
    plt.plot(histg, 'g', label='g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    # 对第 3 子图进行设定
    plt.subplot(3, 1, 3)
    plt.plot(histr, 'r', label='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    cv2.destroyAllWindows()

img = cv2.imread('subset.tif', cv2.IMREAD_UNCHANGED)
disHist(img)
cv2.imshow('input', img)
img2 = linearStretch(img)
disHist(img2)
cv2.imshow('outputOfLineraStretch', img2)
x1 = 75
x2 = 105
y1 = (130,140,140)
y2 = (170,190,180)
img3 = linearDividedStretch(img2,x1,y1,x2,y2)
cv2.imshow('outputOfLinearDivStretch', img3)


cv2.imwrite('sstest.tif', img2)
cv2.waitKey(0)

disHist(img2)
disHist(img3)


