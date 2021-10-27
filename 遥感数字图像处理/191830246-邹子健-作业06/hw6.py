# coding:utf-8
import numpy as np
import cv2


def LaplacianFilter(src, background=False):

    # 为图像添加边框，并将图像转换成np.float64类型
    src = cv2.copyMakeBorder(src, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
    src = np.int16(src)
    rows = src.shape[0]
    cols = src.shape[1]
    g = np.zeros(src.shape, dtype=np.int16)

    # 定义滤波器(True为有背景，False为无背景)
    if background == False:
        template = np.array([[1, 1, 1],
                             [1, -8, 1],
                             [1, 1, 1]], dtype=np.int16)
    else:
        template = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]], dtype=np.int16)

    # bgr
    if len(src.shape) == 3:
        colors = src.shape[2]
        # Laplacian滤波

        for c in range(colors):
            for i in range(1, rows-1):
                for j in range(1, cols-1):
                    temp = src[i-1: i+2, j-1: j+2, c]
                    g[i, j, c] = np.sum(temp*template)
                    if g[i, j, c] < 0:
                        g[i, j, c] = 0
                    elif g[i, j, c] > 255:
                        g[i, j, c] = 255

    # 灰度图
    else:
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                temp = src[i-1:i+2, j-1:j+2]
                g[i, j] = np.sum(temp*template)
                if g[i, j] < 0:
                    g[i, j] = 0
                elif g[i, j] > 255:
                    g[i, j] = 255

    g = g[1: rows-1, 1: cols-1]
    g = np.uint8(g)
    return g


def main():
    fp = r'homework_img.tif'
    img = cv2.imread(fp, cv2.IMREAD_UNCHANGED)
    iscolored = '_color'

    # 作为灰度图输入
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    iscolored = ''

    # 不显示背景
    out = LaplacianFilter(img, False)
    cv2.imwrite('output{}_noBackground_191830246.tif'.format(iscolored), out)

    # 显示背景
    # out = LaplacianFilter(img, True)
    # cv2.imwrite('output{}_withBackground_191830246.tif'.format(iscolored), out)

    # cv2自带的方法
    # out = cv2.Laplacian(img, -1, ksize=3)

    cv2.imshow('input', img)
    cv2.imshow('output', out)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
