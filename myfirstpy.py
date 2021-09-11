print("hello world!")


# def fc():
#     x = "wuhu"
#     y = "qifei"
#     print(x + " " + y)


# fc()

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
print(type(x))
