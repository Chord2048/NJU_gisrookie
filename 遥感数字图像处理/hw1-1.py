def gcd(a, b):
    if a < b:
        temp = b
        b = a
        a = temp
    if b == 0:
        return a
    else:
        a %= b
        return gcd(a, b)


print(gcd(3, 3), gcd(10, 2), gcd(2, 10), gcd(
    100, 50), gcd(27, 36), gcd(1, 10086))
