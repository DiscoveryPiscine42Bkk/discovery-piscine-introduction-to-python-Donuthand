#!/usr/bin/env python3
enter_num = int(input("Enter a number less than 25\n"))
if enter_num > 25 :
    print("Error")
else :
    while enter_num <= 25 :
        print(f"Inside the loop, my variable is {enter_num}")
        enter_num += 1