#coding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
#对数变换

# def plotG(c, y):
#     def gammachange(i):
#         out =  int(c*(i**y)+0.5)
#         if out < 255:
#             return out
#         else: 
#             return 255
#     X = list(range(0,256))
#     Y = [gammachange(i) for i in X]
#     plt.plot(X,X,'r-',label='origin')
#     plt.plot(X,Y,'g-',label='c = {} {} = {}'.format(c,chr(947),y))
#     plt.legend(loc='best')
#     plt.xlim(0,255)
#     plt.ylim(0,255)
#     plt.show()

def main():
    img = cv2.imread('subset.tif', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('input', img)

    cv2.waitKey(0)
    # 计算直方图
    histb = cv2.calcHist([img], [0], None, [256], [0, 255])
    plt.plot(histb, 'y', label='Before')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()