#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as k:
    print(k)

try:
    print(my_square_1.__size)
except Exception as k:
    print(k)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
