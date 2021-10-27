import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy.lib.shape_base import tile

def histPlot(ori,ref,out):
    # 统计图像直方图
    hist_ori = np.zeros(256, dtype=np.float32)
    for i in range(ori.shape[0]):
        for j in range(ori.shape[1]):
            index = ori[i, j]
            hist_ori[index] += 1
            
    hist_ref = np.zeros(256, dtype=np.float32)
    for i in range(ref.shape[0]):
        for j in range(ref.shape[1]):
            index = ref[i, j]
            hist_ref[index] += 1

    hist_out = np.zeros(256, dtype=np.float32)
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            index = out[i, j]
            hist_out[index] += 1
            
    DN = range(256)
	#双Y轴展示直方图和积累图
    fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(18,6),sharey=True)
    # ax1.hist(hist_ori)
    ax1.bar(DN, hist_ori,color='b',label = 'origin')
    ax1.set_ylabel('Histogram')
    ax1.set_xlabel('GrayScale')
    ax2.bar(DN,hist_ref,color='g', label = 'reference')
    ax2.set_xlabel('GrayScale')
    ax3.bar(DN,hist_out,color='r', label = 'output')
    ax3.set_xlabel('GrayScale')
    
	#整饰
    fig.legend(loc=1, bbox_to_anchor=(1,1), bbox_transform = ax3.transAxes)
    fig.tight_layout()
    plt.xlim([0, 256])
    plt.savefig("hist.png")
    plt.show()

def cumuFre(src):
    row = src.shape[0]
    col = src.shape[1]
    hist = np.zeros(256, dtype = np.float32)
    cumuHist = np.zeros(256, dtype = np.float32)
    for i in range(row):
        for j in range(col):
            index = src[i, j]
            hist[index] += 1
    cumuHist[0] = hist[0]
    for i in range(1, 256):
        cumuHist[i] = cumuHist[i-1] + hist[i]
    cumuHist = cumuHist / np.float32(row*col)
    return cumuHist

#直方图匹配
def histMatching(oriImg, tarImg):
    out = np.zeros_like(oriImg)
    cumu_ori = cumuFre(oriImg)
    cumu_tar = cumuFre(tarImg)
    for i in range(256):
        tmp = abs(cumu_ori[i]-cumu_tar)
        tmp = tmp.tolist()
        idx = tmp.index(min(tmp))
        out[:, :][oriImg[:, :] == i] = idx
    return out



def main():
    img = cv2.imread('Original_Reference.jpg',cv2.IMREAD_UNCHANGED)
    ref = cv2.imread('Target_Img.png',cv2.IMREAD_UNCHANGED)
    cv2.imshow('origin',img)
    cv2.imshow('reference',ref)
    out = histMatching(img,ref)
    cv2.imshow('out',out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    histPlot(img,ref,out)
    cv2.imwrite('output.png',out)

if __name__ == '__main__':
    main()