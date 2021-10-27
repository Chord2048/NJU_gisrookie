# coding:utf-8
import numpy as np
import cv2

def maketemplate(fsize):
    bordersize = int((fsize-1)//2)
    template1 = np.zeros((fsize,fsize),dtype=np.uint16)
    template2 = np.zeros((fsize,fsize),dtype=np.uint16)
    for i in range(0,fsize):
        for j in range(0,fsize):            
            if i == j or i + j == fsize -1:
                template1[i,j] = 1
            if i == bordersize or j == bordersize:
                template2[i,j] = 1
    return template1,template2

# fsize 可以更换，运行速度略慢
def EdgePreservingFilter(src,fsize=5):
    bordersize = int((fsize-1)//2)
    src = cv2.copyMakeBorder(src, bordersize, bordersize, bordersize, bordersize, cv2.BORDER_REPLICATE)
    dst = np.zeros(src.shape, dtype = np.uint16)
    rows, cols, dim = src.shape
    template1,template2 = maketemplate(fsize)
    
    for i in range(bordersize, rows-bordersize):
        for j in range(bordersize, cols-bordersize):
            for k in range(dim):
                temp = src[i-bordersize: i+bordersize+1, j-bordersize: j+bordersize+1, k]
                temp = np.uint16(temp)
                temp += 1
                median1 = temp*template1
                median2 = temp*template2
                median1 = median1[median1>0]
                median2 = median2[median2>0]
                median1 = np.uint8(np.median(median1)-1)
                median2 = np.uint8(np.median(median2)-1)
                # print(median1,median2)
                dst[i,j,k] = np.median((median1,median2,dst[i,j,k]))

    dst = np.uint8(dst[bordersize: rows-bordersize, bordersize: cols-bordersize,:])     
    return dst



def main():
    img = cv2.imread('NJU_noise.tif', cv2.IMREAD_UNCHANGED)
    cv2.imshow('input', img)
    
    # fsize 可以更换，运行速度略慢
    img2 = EdgePreservingFilter(img,fsize=5)
    cv2.imshow('output',img2)
    cv2.imwrite('output.png',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()