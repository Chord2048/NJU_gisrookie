import numpy as np
import cv2


def main():
    img = cv2.imread('city.tif', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('input',img)
    # 添加不同类型边框，并显示结果图像
    img1 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
    cv2.imshow('cv2.BORDER_CONSTANT value=10', img1)
    img2 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    cv2.imshow('cv2.BORDER_REFLECT', img2)
    img3 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
    cv2.imshow('cv2.BORDER_REFLECT_101', img3)
    img4 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_DEFAULT)
    cv2.imshow('cv2.BORDER_DEFAULT', img4)
    img5 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    cv2.imshow('cv2.BORDER_REPLICATE', img5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()