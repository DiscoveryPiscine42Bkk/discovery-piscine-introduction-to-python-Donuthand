#!/usr/bin/env python3
table = 0
while table <= 10:
    multiplier = 0
    print(f"Table de {table} :" , end=' ') #end=' ' is create a space after it instead of a newline
    while multiplier <= 10:
        result = table * multiplier
        print(result, end=' ')
        multiplier += 1
    print()
    table +=1