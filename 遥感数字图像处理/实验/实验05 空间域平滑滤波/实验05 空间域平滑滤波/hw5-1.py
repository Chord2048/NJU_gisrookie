# coding:utf-8
import numpy as np
import cv2


def GaussFilter(src):
    src = cv2.copyMakeBorder(src, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
    pass


def main():
    img = cv2.imread('NJU_noise.tif', cv2.IMREAD_UNCHANGED)
    cv2.imshow('input', img)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()