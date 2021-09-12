# coding:utf-8
import numpy as np


def matrix_multiply(a, b):
    if len(a[0]) == len(b):
        res = np.array([[0]*len(b[0])]*len(a),
                       dtype=np.float32)    # a的行数 * b的列数
        for i in range(0, len(a)):
            for j in range(0, len(b[0])):
                for k in range(0, len(b)):
                    res[i][j] += a[i][k]*b[k][j]
    else:
        print("error : to do matrix multiply, the cols of former matrix mush match the rows of the latter")
        exit()
    return res


def main():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float32)
    b = np.array([[5, 8, 3], [9, 4, 2], [1, 6, 7]], dtype=np.float32)
    result = matrix_multiply(a, b)
    print("my result:\n", result)
    print("numpy result:\n", np.dot(a, b))


# 进入主函数
if __name__ == '__main__':
    main()
