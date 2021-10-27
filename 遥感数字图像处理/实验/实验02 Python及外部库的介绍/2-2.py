#coding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    path = input('请输入图片路径:  ')
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
    histb = cv2.calcHist([img], [0], None, [256], [0, 255])
    histg = cv2.calcHist([img], [1], None, [256], [0, 255])
    histr = cv2.calcHist([img], [2], None, [256], [0, 255])
    cv2.imshow("image", img)

    plt.subplot(2,2,1)
    plt.plot(histb, 'b', label='blue')
    plt.legend()
    plt.title('blue')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(2, 2, 2)
    plt.plot(histg, 'g', label='green')
    plt.legend()
    plt.title('green')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(2, 2, 3)
    plt.plot(histr, 'r', label='red')
    plt.legend()
    plt.title('red')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(2, 2, 4)
    plt.hist(img.ravel(),256,color='k',label='gray')
    plt.legend()
    plt.title('gray')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
