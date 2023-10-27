# coding: utf8
"""
Write a program that prompts the user to enter a password, and then prints
exactly one of the following messages: ‘The password is secure.’ or
‘The password is insecure!’. A secure password must meet the following
conditions:

* have at least one lowercase letter,
* have at least one capital letter,
* have at least one digit.

Examples:

Enter the password: Katar7yna
The password is secure.
Enter the password: catastrophe01
The password is insecure!

"""

# your code here
enter = input("Enter the password:")
capital = 0
lower = 0
digit = 0
for i in enter:
    if(i.isupper()):
        capital = capital + 1
    if(i.islower()):
        lower = lower + 1  
    if(i.isdigit()):
        digit = digit + 1     
if (capital>=1 and lower>=1 and digit>=1):
    print("The password is secure.")
else:
    print("The password is insecure!")      