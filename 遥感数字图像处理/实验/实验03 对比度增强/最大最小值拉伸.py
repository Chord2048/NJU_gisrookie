import cv2
import numpy as np
import matplotlib.pyplot as plt
# 绘制变换函数图像


def linearPlot(x1, x2):
    plt.plot([x1, x2], [0, 255], 'r')
    # 第一个方框代表 x 的各个标记点，第二个方框代表 y 的各个标记点，第三个显示风格
    plt.plot([x2, x2], [0, 255], '--')
    plt.xlim(0, 255), plt.ylim(0, 255)
    plt.show()


def linearStretch(src):
    smax = np.max(src)
    smin = np.min(src)
    linearPlot(smin, smax)  # 调用绘图函数
    dst = 255.0 * (src - smin) / (smax - smin)
    dst = np.uint8(dst + 0.5)
    return dst


img = cv2.imread(r'NJU_gray.tif', 0)
cv2.imshow('input', img)
cv2.waitKey(0)
# waitKey() 函数的功能是不断刷新图像 , 频率时间为 delay , 单位为 ms； # waitKey(0) , 则表示程序会无限制的等待用户的按键事件
img2 = linearStretch(img)
cv2.imshow('output', img2)
cv2.waitKey(0)
cv2.imwrite(r'NJU_output.tif', img2)
cv2.waitKey()
cv2.destroyAllWindows()  # 删除所有窗口；若要删除特定的窗口，往输入特定的窗口值
print('done!')
