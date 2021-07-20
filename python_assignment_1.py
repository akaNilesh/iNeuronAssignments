#Problem Statement
'''
1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
#initializing blank array to store the result set
array = []
i=2000
while i<=3200:
    if i%7==0 and i%5!=0:
        array.append(i)
    i=i+1
print(array)

'''
2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
'''
firstName =input("Enter first name ")
secondName = input("Enter second name ")
print(f"{secondName} {firstName}")

'''
3. Write a Python program to find the volume of a sphere with diameter 12 cm.
'''
from math import pi
diameter = 12
r=diameter/2
volume = (4/3)*pi*(r**3)
print(f"Volume of given sphere is {volume}")