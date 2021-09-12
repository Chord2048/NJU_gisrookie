# coding:utf-8
# if elif else

# a = 200
# b = 201
# print(">") if a > b else print("<") if a < b else print("=")

# pass 语句
# if 语句不能为空，但是如果您处于某种原因写了无内容的 if 语句，请使用 pass 语句来避免错误。
# a = 66
# b = 200
# if b > a:
#     pass

# python 循环
# i = 1
# out = 0
# while i <= 10:
#     out += i
#     if i == 3:
#         break
#     i += 1
# print(out)

# Python For 循环
# for 循环用于迭代序列（即列表，元组，字典，集合或字符串）。
# for x in "banana":
#     print(x)

# range() 函数
# 如需循环一组代码指定的次数，我们可以使用 range() 函数，
# range() 函数返回一个数字序列，默认情况下从 0 开始，并递增 1（默认地），并以指定的数字结束。
# for i in range(n, m, s) 相当于 for(i = n, i < m, i+=s)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

# python 函数
# 默认参数
# def myfunc(age=10):
#     print(age)


# myfunc(1)
# myfunc()

# list传参
# def myfunc(ls):
#     for x in ls:
#         print(x)


# myfunc([1, 2, 3])
# myfunc("wuhu")

# 关键字传参 参数顺序无关
# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)


# my_function(child1="Phoebe", child2="Jennifer", child3="Rory")

# 任意参数
# 如果您不知道将传递给您的函数多少个参数，请在函数定义的参数名称前添加 *。
# 这样，函数将接收一个参数元组，并可以相应地访问各项：
# def my_function(*kids):
#     print("The youngest child is " + kids[2])   # kids是一个参数元组


# my_function("Phoebe", "Jennifer", "Rory")

# Python Lambda
# lambda 函数是一种小的匿名函数。
# lambda 函数可接受任意数量的参数，但只能有一个表达式。
# 语法： lambda arguments : expression
# x = lambda a,b : a*b
# print(x(5, 6))

# def myfunc(n):
#     return lambda a: a * n  # 返回参数为a的匿名函数


# mydoubler = myfunc(2)   # n=2，mydoubler是一个函数 参数为a
# mytripler = myfunc(3)

# print(mydoubler(11))    # 11 * 2
# print(mytripler(11))
