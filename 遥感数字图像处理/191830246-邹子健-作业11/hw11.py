# coding: utf-8
import numpy as np
from cv2 import cv2


def min_max_strech(src):
    src = np.float128(src)
    max = np.max(src)
    min = np.min(src)
    src = np.uint8((src - min) / (max - min) * 255 + .5)
    return src


def motion_blur(src_f, T, a, b):
    rows, cols = src_f.shape
    dst = src_f.copy()
    m = round(rows / 2)
    n = round(cols / 2)
    template = np.zeros(src_f.shape, dtype=np.float64)
    for i in range(rows):
        for j in range(cols):
            u = i - m
            v = j - n
            factor = np.float128(3.14159265359) * (u * a + v * b)
            if factor != 0:
                template[i, j] = T / factor * \
                    np.sin(factor) * np.exp(-1j * factor)
            else:
                template[i, j] = T
    template[abs(template) < 0.000001] = 0.0000001
    dst = dst * template
    return dst, template


def addGaussNoise(src):
    img = src.copy()
    img2 = np.float128(img)
    rows, cols = img.shape
    GaussNoise = np.random.normal(0, .3, (rows, cols))
    img3 = img2 + GaussNoise * 8
    # return min_max_strech(img3)
    return img3


def inverseFliter(srcImg, template):
    degImg = srcImg.copy()
    degf2 = np.fft.fft2(degImg)
    degfsh2 = np.fft.fftshift(degf2)
    dirReImgfsh = degfsh2 / (template)
    dirReImgf = np.fft.ifftshift(dirReImgfsh)
    dirReImg = np.fft.ifft2(dirReImgf)
    dirReImg = np.abs(dirReImg)
    # return min_max_strech(dirReImg)
    return dirReImg


def wienerFliter(srcimg, template, k2):
    img = srcimg.copy()
    degf2 = np.fft.fft2(img)
    degfsh2 = np.fft.fftshift(degf2)
    temp = template ** 2
    wtemplate = template / (temp + k2)
    wfsh = degfsh2 * wtemplate
    wf = np.fft.ifftshift(wfsh)
    wtemp = np.fft.ifft2(wf)
    wImg = np.abs(wtemp)
    return wImg


def main():
    ipath = 'NJU.tif'
    src = cv2.imread(ipath, cv2.IMREAD_UNCHANGED)
    cv2.imshow('raw', src)
    src_f = np.fft.fft2(src)
    src_sf = np.fft.fftshift(src_f)
    src_sf_b, tp = motion_blur(src_sf, 1, .01, .01)

    src_s = np.fft.ifftshift(src_sf_b)
    src_b = np.fft.ifft2(src_s)
    src_b = np.abs(src_b)

    # src_b = min_max_strech(src_b)
    cv2.imshow('motion blur image', min_max_strech(src_b))
    cv2.imwrite('NJU_blured.tif', min_max_strech(src_b))

    src_b_n = addGaussNoise(src_b)
    cv2.imshow('blured image with Gauss noise', min_max_strech(src_b_n))
    cv2.imwrite('NJU_bluredNoise.tif', min_max_strech(src_b_n))

    dst_i = inverseFliter(src_b_n, tp)
    cv2.imshow('inverseFliter', min_max_strech(dst_i))
    cv2.imwrite('inverse_out.tif', min_max_strech(dst_i))

    dst_w = wienerFliter(src_b_n, tp, 0.01)
    cv2.imshow('wienerFliter', min_max_strech(dst_w))
    cv2.imwrite('wiener_out.tif', min_max_strech(dst_w))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
