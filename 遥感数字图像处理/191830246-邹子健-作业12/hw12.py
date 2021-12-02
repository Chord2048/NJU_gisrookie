# coding : utf-8
from cv2 import cv2
import numpy as np

# 定义connect函数


def connect(img, y, x, low):
    row, col = img.shape[0: 2]
    neighbour = np.array(
        [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
    for k in range(8):
        yy = y + neighbour[k, 0]
        xx = x + neighbour[k, 1]
        if yy >= 0 and yy < row and xx >= 0 and xx < col:
            if img[yy, xx] >= low and img[yy, xx] != 255:
                img[yy, xx] = 255
                connect(img, yy, xx, low)


def LoG(src):
    # step 1. make border
    src = np.float64(src)
    # step 2. define LoG template
    template = np.array([[0, 0, -1, 0, 0],
                        [0, -1, -2, -1, 0],
                        [-1, -2, 16, -2, -1],
                        [0, -1, -2, -1, 0],
                        [0, 0, -1, 0, 0]], dtype=np.float64)
    row, col = list(template.shape)
    radius = int(row / 2)

    # step 3. filter
    rows, cols = list(src.shape)
    dst = np.zeros(src.shape, dtype=np.float32)
    src = cv2.copyMakeBorder(src, radius, radius, radius,
                             radius, cv2.BORDER_REPLICATE)
    for i in range(rows):
        for j in range(cols):
            ni = i + radius
            nj = j + radius
            tp = src[ni - radius:ni + radius + 1, nj - radius:nj + radius + 1]
            # print(tp.shape)
            dst[i, j] = np.sum(tp * template)
    # step 4. post processing
    dst = np.abs(dst)
    dmin = np.min(dst)
    dmax = np.max(dst)
    dst = 255.0 / (dmax-dmin) * (dst-dmin)
    dst = np.uint8(dst + 0.5)
    row1, col1 = dst.shape
    res = dst.copy()
    count = 0
    up = 40
    low = 38
    for i in range(row1):
        for j in range(col1):
            if res[i, j] > up:
                res[i, j] = 255
                connect(res, i, j, low)
    res = np.uint8(res)
    final = np.zeros(res.shape, dtype=np.uint8)
    final[res == 255] = 255
    return final


def main():
    src = cv2.imread('Lena.tif', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('input', src)
    dst = LoG(src)
    cv2.imshow('output', dst)
    cv2.imwrite('LOG_output.tif', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
