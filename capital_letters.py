# coding: utf8
"""
Write a program that prompts user to enter some text and prints the number
of CAPITAL LETTERS on the screen. E.g:

Enter text: Data Science is SUPER!
7

"""

# your code here
enter = input("Enter text:")
capital = 0
for i in enter:
    if(i.isupper()):
        capital = capital+1
print(capital)