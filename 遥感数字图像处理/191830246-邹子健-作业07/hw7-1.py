# coding: utf-8
import numpy as np
import cv2


# 拉伸，显示，并保存

def show_save(img, name='img'):
    max = np.max(img)
    min = np.min(img)
    img = 255.0*(img-min)/(max-min)
    img = np.uint8(np.round(img))
    cv2.imshow('show_'+name, img)
    cv2.imwrite(name+'.jpg', img)


def exchange_mag_pha(img1, img2):

    # 傅里叶变换
    sp1 = np.fft.fft2(img1)
    osp1 = np.fft.fftshift(sp1)

    mag1 = np.abs(osp1)
    pha1 = np.angle(osp1)

    sp2 = np.fft.fft2(img2)
    osp2 = np.fft.fftshift(sp2)

    mag2 = np.abs(osp2)
    pha2 = np.angle(osp2)

    # 保存频谱，相位谱图像
    # show_save(pha1, 'pha_im1')
    # show_save(np.log(mag1 + 1), 'mag_im1')
    # show_save(pha2, 'pha_im2')
    # show_save(np.log(mag2 + 1), 'mag_im2')

    # 交换频谱，相位谱
    image1 = np.zeros(img1.shape, dtype=np.complex)
    image1.real = mag1 * np.cos(pha2)
    image1.imag = mag1 * np.sin(pha2)

    image2 = np.zeros(img2.shape, dtype=np.complex)
    image2.real = mag2 * np.cos(pha1)
    image2.imag = mag2 * np.sin(pha1)

    # FFT 逆变换
    rst1 = np.uint8(np.abs(np.fft.ifft2(np.fft.ifftshift(image1))) + 0.5)
    rst2 = np.uint8(np.abs(np.fft.ifft2(np.fft.ifftshift(image2))) + 0.5)

    show_save(rst1, 'lena_mag_with_buildings_pha')
    show_save(rst2, 'buildings_mag_with_lena_pha')

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # 读取图像
    img_lena = cv2.imread(r'Lena.tif', cv2.IMREAD_GRAYSCALE)
    img_buildings = cv2.imread(r'buildings.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Lena Raw', img_lena)
    cv2.imshow('buildings Raw', img_buildings)

    exchange_mag_pha(img_lena, img_buildings)


if __name__ == '__main__':
    main()
