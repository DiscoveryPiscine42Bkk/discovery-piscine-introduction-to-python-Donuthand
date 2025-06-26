#!/usr/bin/env python3
import sys
lenght = len(sys.argv) -1
if lenght <2:
    print("none")
else:
    rev = list(reversed(sys.argv[1:])) #sequence[start:stop:step]
    for n in rev:
        print(n)
