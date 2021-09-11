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
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
