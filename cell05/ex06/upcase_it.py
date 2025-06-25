#!/usr/bin/env python3
import sys
length = len(sys.argv)
input = sys.argv[1]
if length == 2: 
    print(input.upper())
else:
    print("none")
