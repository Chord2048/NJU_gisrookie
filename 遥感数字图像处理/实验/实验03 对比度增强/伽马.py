# coding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt


def gammaStretch(src, c, y):
    src = np.float32(src)
    dst = c*(src**y)
    dst = np.uint8(dst+0.5)
    return dst


def plotG(src, c, y):
    X = list(range(0, 256))
    Y = [gammaStretch(i, c, y) for i in X]
    plt.plot(X, Y)


def main():
    c, y = input('please input c & y: ')
    fp = 'NJU_gray.tif'
    img = cv2.imread(fp, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('input', img)
    img2 = gammaStretch(img, c, y)
    plotG(img, c, y)
    cv2.imshow('output', img2)
    cv2.waitKey(0)

    # 计算直方图
    histb = cv2.calcHist([img], [0], None, [256], [0, 255])
    hista = cv2.calcHist([img2], [0], None, [256], [0, 255])
    # 对第 1 子图进行设定
    plt.subplot(2, 1, 1)
    plt.plot(histb, 'y', label='Before')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    # 对第 2 子图进行设定
    plt.subplot(2, 1, 2)
    plt.plot(hista, 'c', label='After')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
