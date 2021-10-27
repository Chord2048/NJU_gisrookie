# coding:utf-8
import numpy as np
import cv2
from numpy.core.fromnumeric import shape


def GaussFilter(src):
    src = cv2.copyMakeBorder(src, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
    dst = np.zeros(src.shape, dtype = np.float32)
    rows, cols, dim = src.shape
    
    template = 1.0/16 * np.array([1,2,1,2,4,2,1,2,1],dtype=float).reshape((3,3))
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
             for k in range(dim):
                  temp = src[i-1: i+2, j-1: j+2, k]
                  dst[i, j, k] = np.sum(temp * template)
                  
    dst = np.uint8(dst + 0.5)
    dst = dst[1: rows-1, 1: cols-1,:]     
    return dst



def main():
    img = cv2.imread('NJU_noise.tif', cv2.IMREAD_UNCHANGED)
    cv2.imshow('input', img)
    img_guass = GaussFilter(img)
    cv2.imshow('output',img_guass)


    cv2.waitKey(0)


if __name__ == '__main__':
    main()