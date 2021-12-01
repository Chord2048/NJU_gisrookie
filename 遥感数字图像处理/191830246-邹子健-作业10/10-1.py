# 利用Brovey方法进行图像融合
import cv2
import numpy as np


def Brovey(mul, pan):

    # 将数据转换到浮点型
    mul = np.float64(mul)
    pan = np.float64(pan)
    dst = np.zeros(mul.shape, dtype=np.float64)

    # 数据融合
    row, col, dim = mul.shape
    if dim >= 2:
        mul_sum = np.sum(mul, axis=2)
        mul_sum[mul_sum == 0] = 0.000001
        dst = np.dstack(
            [mul[:, :, i].copy() / mul_sum * pan for i in range(dim)])
    else:
        dst = pan.copy()

    for i in range(dim):
        max = np.max(dst[:, :, i])
        min = np.min(dst[:, :, i])
        dst[:, :, i] = np.uint8((dst[:, :, i] - min) / (max - min) * 255 + 0.5)
    return np.uint8(dst)


def main():

    mul = cv2.imread('mul_input.tif', cv2.IMREAD_UNCHANGED)
    pan = cv2.imread('pan_input.tif', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('mul-image', mul)
    cv2.imshow('pan-image', pan)

    img = Brovey(mul, pan)
    cv2.imshow('fused image', img)
    cv2.imwrite('BroveyFusion.tif', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
