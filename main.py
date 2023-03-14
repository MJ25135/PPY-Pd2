# a = 100
# b = 100
# print(id(a))
# print(id(b))
import sys

c = d = 50
# print(c)
# print(d)
# print(id(c))
# print(id(d))
print(sys.getrefcount(c))
print(type(c))
