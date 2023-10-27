# coding: utf8
"""
Write a program that will ask the user for an integer (the size of the triangle)
and then print an isosceles triangle composed of `*` characters of the given
size. E.g:

Enter the size of the triangle: 3
  *
 ***
*****

"""

# your code here
number = int(input("Enter the size of the triangle: "))
for i in range(0, number):
    print(" " * (number - i-1), end=" ")
    for j in range(0, i+1):
      if j == 0:
        print("*", end="")
      else:
         print("*" * 2, end="")
    print()