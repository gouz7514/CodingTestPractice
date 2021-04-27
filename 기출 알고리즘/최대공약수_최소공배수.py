x = 15
y = 20

# def gcd(x, y):
#     while y > 0:
#         x, y = y, x % y
#     return x
#
# print(gcd(x, y))

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x
print(gcd(x, y))

def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(x, y))