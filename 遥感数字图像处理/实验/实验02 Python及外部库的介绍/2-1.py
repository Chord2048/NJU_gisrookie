import cv2
import numpy as np

def imgFlip(path, method, winName='flipindow'):
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.namedWindow(winName, 0)
    if method=='x':
        #水平翻转
        h_img = cv2.flip(img, 1)
        cv2.imshow(winName, h_img)
    elif method=='y':
        #垂直翻转
        v_img = cv2.flip(img, 0)
        cv2.imshow(winName, v_img)
    else:
        #水平加垂直翻转
        hv_img = cv2.flip(img, -1)
        cv2.imshow(winName, hv_img)
    cv2.waitKey(0)               #等待事件触发，参数0表示永久等待
    cv2.destroyAllWindows()      #释放窗口


def main():
    path = input('请输入图片路径:  ')
    method = input('请输入翻转方式 x，y或xy:  ')
    imgFlip(path, method)
if __name__ == '__main__':
    main()
