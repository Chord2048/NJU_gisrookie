# coding:utf-8
# 列表
# 集合数据类型
# Python 集合（数组）
# Python 编程语言中有四种集合数据类型：

# 列表（List）是一种有序和可更改的集合。允许重复的成员。
# 元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
# 集合（Set）是一个无序和无索引的集合。没有重复的成员。
# 词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# for x in thislist:
#     print(x)
# if "apple" in thislist:
#     print("yes, apple is in the list")
# print("the lenth of this list is "+str(len(thislist)))
# thislist.append("huolongguo")
# print(thislist)
# thislist.insert(1, "kaixinguo")
# print(thislist)
# thislist.remove("apple")
# print(thislist)
# thislist.pop()
# print(thislist)
# del thislist[3]
# print(thislist)

# 复制列表
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# testlist = mylist
# print(mylist)
# testlist[1] = "wuhuqifei"  # 只是引用
# print(testlist)
# print(mylist)
# copylist = list(mylist)  # 内建方法
# print(copylist)


# 合并列表
# +方法
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
# print(list1)
# extend() 方法
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# 构造函数 list()
# thislist = list(("apple", "banana", "cherry"))  # 请注意双括号
# print(thislist)

# list 内建方法
# append()
# clear()
# copy()
# count()   返回元素计数
# extend()  将列表元素（或任何可迭代的元素）添加到当前列表的末尾
# index()   返回第一个索引
# insert()  插入元素
# pop()     删除指定位置的元素
# remove()  删除指定值的元素
# reverse() 颠倒顺序
# sort()    排序 list.sort(reverse=True | False, key=myFunc)

# sort()实例 按照值的长度对列表进行降序排序：

# # 返回值的长度的函数：
# def myFunc(e):
#     return len(e)
# cars = ['Porsche', 'Audi', 'BMW', 'Volvo']
# cars.sort(reverse=True, key=myFunc)
# print(cars)
