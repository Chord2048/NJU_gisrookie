#coding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
#对数变换
def gammaStretch(src, c, y):
    src = np.float32(src)
    dst = np.uint16(c * (src**y)+.5)
    dst[dst>255]=255
    return np.uint8(dst)

def plotG(c, y):
    def gammachange(i):
        out =  int(c*(i**y)+0.5)
        if out < 255:
            return out
        else: 
            return 255
    X = list(range(0,256))
    Y = [gammachange(i) for i in X]
    plt.plot(X,X,'r-',label='origin')
    plt.plot(X,Y,'g-',label='c = {} {} = {}'.format(c,chr(947),y))
    plt.legend(loc='best')
    plt.xlim(0,255)
    plt.ylim(0,255)
    plt.show()

def main():
    y = float(input('please input '+chr(947)+': '))
    c = float(input('please input c: '))
    plotG(c,y)
    img = cv2.imread('city.tif', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('input', img)
    img2 = gammaStretch(img, c, y) 
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