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

# 元组（Tuple）
# 元组是有序且不可更改的集合。在 Python 中，元组是用圆括号编写的。
# thistuple = ("apple", "banana", "cherry")
# print(type(thistuple))
# print(thistuple)

# 集合（Set）
# 集合是无序和无索引的集合。在 Python 中，集合用花括号编写。
# thisset = {"apple", "banana", "cherry"}
# print(type(thisset))
# print(thisset)

# 集合一旦创建就无法更改项目，但是可以添加项目
# 使用 add() 方法向 set 添加项目：
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# 使用 update() 方法将多个项添加到集合中：
# thisset = {"apple", "banana", "cherry"}
# addlist = ["a", "b", "c"]
# thisset.update(["orange", "mango", "grapes"])
# print(thisset)
# thisset.update(addlist)
# print(thisset)

# 删除项目 remove() 方法 discard() 方法
# 因为如果指定的项目不存在，则 remove() 方法将引发错误，而 discard() 方法不会。
# thisset = {"a", "b", "c"}
# thisset.discard("a")
# print(thisset)

# 合并集合 union() update()
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)  # 不改变set1
# print(set3)
# print(set1)

# python中的set方法
# add()	向集合添加元素。
# clear()	删除集合中的所有元素。
# copy()	返回集合的副本。
# difference()	返回包含两个或更多集合之间差异的集合。
# difference_update()	删除此集合中也包含在另一个指定集合中的项目。
# discard()	删除指定项目。
# intersection()	返回为两个其他集合的交集的集合。
# intersection_update()	删除此集合中不存在于其他指定集合中的项目。
# isdisjoint()	返回两个集合是否有交集。
# issubset()	返回另一个集合是否包含此集合。
# issuperset()	返回此集合是否包含另一个集合。
# pop()	从集合中删除一个元素。
# remove()	删除指定元素。
# symmetric_difference()	返回具有两组集合的对称差集的集合。
# symmetric_difference_update()	插入此集合和另一个集合的对称差集。
# union()	返回包含集合并集的集合。
# update()	用此集合和其他集合的并集来更新集合。

# 字典
# thisidct = {
#     "小明": "10086",
#     "小花": "10001"
# }
# print(thisidct)
# print(thisidct["小明"])
# print(thisidct.get("小明"))

# for x in thisidct:
#     print(x, thisidct[x])
# for x in thisidct.values():
#     print(x)
# # items() 方法
# for x, y in thisidct.items():
#     print(x, y)

# thisdict = {
#     "brand": "Porsche",
#     "model": "911",
#     "year": 1963
# }
# thisdict.pop("model")   # pop()的参数是键
# print(thisdict)


# 嵌套字典
# myfamily = {
#     "child1": {
#         "name": "Phoebe Adele",
#         "year": 2002
#     },
#     "child2": {
#         "name": "Jennifer Katharine",
#         "year": 1996
#     },
#     "child3": {
#         "name": "Rory John",
#         "year": 1999
#     }
# }
# print(myfamily["child1"]["year"])   # 2002

# python 字典方法
# clear()	删除字典中的所有元素
# copy()	返回字典的副本
# fromkeys()	返回拥有指定键和值的字典
# get()	返回指定键的值
# items()	返回包含每个键值对的元组的列表
# keys()	返回包含字典键的列表
# pop()	删除拥有指定键的元素
# popitem()	删除最后插入的键值对
# setdefault()	返回指定键的值。如果该键不存在，则插入具有指定值的键。
# update()	使用指定的键值对字典进行更新
# values()	返回字典中所有值的列表
