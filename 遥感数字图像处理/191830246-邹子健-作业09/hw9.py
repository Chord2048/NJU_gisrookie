# coding: utf-8
import cv2
import numpy as np


def normalize(img):
    img = np.float32(img)
    max = np.max(img)
    min = np.min(img)
    img = 255.0/(max - min)*(img - min)
    img = np.uint8(img + 0.5)
    return img


def showMag(title, mag):
    mag = np.abs(mag)
    # 频谱需要进行对数变换便于显示细节
    magView = np.log(mag + 1)
    magView = normalize(magView)
    cv2.imshow(title, magView)

# Homomorphic filter


def HF(src, H, L, d0, c, tag):
    # 傅里叶变换
    f = np.fft.fft2(src)
    fshift = np.fft.fftshift(f)
    # showMag('Mag_before'+tag, fshift)
    # 定义滤波器
    rows, cols = src.shape
    m, n = rows/2, cols/2
    d0 = np.float32(d0)
    temp = np.zeros(src.shape, dtype=np.float32)
    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i-m) ** 2 + (j - n) ** 2)
            temp[i, j] = 1 - np.exp(-c * d ** 2 / d0 ** 2)
    template = (H - L) * temp + L
    # cv2.imshow('Tempalte'+tag, template)

    fshift2 = fshift * template
    # showMag('Mag_after'+tag, fshift2)

    f2 = np.fft.ifftshift(fshift2)
    dst = np.fft.ifft2(f2)
    dst = np.abs(dst)
    dst = normalize(dst)
    return dst

    f2 = np.fft.ifftshift(fshift2)
    dst = np.fft.ifft2(f2)
    dst = np.abs(dst)
    dst = normalize(dst)

    return dst


def main():
    img = cv2.imread('homework.tif', cv2.IMREAD_UNCHANGED)
    cv2.imshow('input', img)
    imgb, imgg, imgr = cv2.split(img)
    # cv2.imshow('b', imgb)
    # cv2.imshow('g', imgg)
    # cv2.imshow('r', imgr)
    dstb = HF(imgb, H=2.5, L=0.7, d0=20, c=2, tag='_b')
    dstg = HF(imgg, H=2.5, L=0.7, d0=20, c=2.5, tag='_g')
    dstr = HF(imgr, H=2, L=0.8, d0=20, c=1.5, tag='_r')
    # cv2.imshow('ob', dstb)
    # cv2.imshow('og', dstg)
    # cv2.imshow('or', dstr)

    dst = cv2.merge([dstb, dstg, dstr])
    # H>1,L<1 则滤波函数将同时减少低频分量、
    # 扩大高频分量，最后的结果是既压缩了明度范围，有增强了对比度；
    # d0截止频率，d到频谱中心的距离；常数c控制函数坡度

    cv2.imshow('output', dst)

    cv2.waitKey(0)
    cv2.imwrite('output.tif', dst)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
