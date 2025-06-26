#!/usr/bin/env python3
import sys
if len(sys.argv) == 1 :
    print("none")
else:
    input = sys.argv[1]
    input_count = input.count("z")
    if input_count > 0 :
        print(f"{'z' * input_count}")  
    else:
        print("none")