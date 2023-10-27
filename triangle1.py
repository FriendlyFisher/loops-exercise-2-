# coding: utf8
"""
Write a program that will ask the user for an integer (the size of the triangle)
and then print a right-angled triangle (with a right angle in the lower left
corner) composed of `*` characters of the given size. E.g:

Enter the size of the triangle: 4
*
**
***
****

"""

# your code here
number = int(input("Enter the size of the triangle: "))

for i in range(number):
    print("*" * (i + 1))
