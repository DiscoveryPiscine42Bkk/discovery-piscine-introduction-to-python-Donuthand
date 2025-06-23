#!/usr/bin/env python3
firstnum = int(input("Enter the first number:\n"))
secondnum = int(input("Enter the second number:\n"))
result = firstnum * secondnum
print(f"{firstnum} x {secondnum} = {result}")
if result > 0:
    print("The result is positive")
elif result < 0:
    print("The result is negative")
else:
    print("The result is zero")