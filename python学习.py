# coding:utf-8
# x = "awesome"


# def myfunc():
#     print("Python is " + x)


# myfunc()

# 在函数内创建全局变量 global
# def myfunc():
#     global x
#     x = "芜湖"

# myfunc()
# print(x+"起飞")

# 要在函数内部更改全局变量的值，请使用 global 关键字引用该变量：

# 数据类型
# 文本类型：	str
# 数值类型：	int, float, complex
# 序列类型：	list, tuple, range
# 映射类型：	dict
# 集合类型：	set, frozenset
# 布尔类型：	bool
# 二进制类型：	bytes, bytearray, memoryview

# python 数字类型
# x = 10    # int
# y = 6.3  # float
# z = 2j   # complex
# print(type(x))
# print(type(y))
# print(type(z))
# output：
# <type 'int' >
# <type 'float' >
# <type 'complex' >

# 类型转换
# x = 1.4
# y = 1.5
# z = 1.7
# q = -1.3
# print(int(x))
# print(int(y))
# print(int(z))
# print(int(q))
# 1
# 1
# 1
# 1

# 多行字符串
# x = """
# 第一行
# 第二行

# 第 四 行
# """
# print(x)

# a = "abcdef"
# print(a[1:2])
# print(a[-4:-2])
# print(a.upper())
# print(a.replace("abc", "ddd"))  # 实际上不改变a
# print(a)
# print("ddd" not in a)
# output:
# b
# cd
# ABCDEF
# ddddef
# abcdef
# True

# fomat 方法
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# #I want 3 pieces of item 567 for 49.95 dollars.
# 占位符
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))
# #I want to pay 49.95 dollars for 3 pieces of item 567.

# #python运算符
# print(2**5)
# print(5//2)
# #逻辑算符
# print(not(1 == 1))  # false
# print(not 0)  # true
# #Python 成员运算符
# #in #not in
# print('x' in 'xyz')  # true
