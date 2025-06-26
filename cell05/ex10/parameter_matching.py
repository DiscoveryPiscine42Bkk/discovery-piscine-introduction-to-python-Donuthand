#!/usr/bin/env python3
import sys
import re
ques = sys.argv[1]
if len((sys.argv)) != 2:
    print("none")
else:
    ans = input(f"What was the parameter? ")
    if ques == ans:
        print("Good Job!")
    else:
        print("Nope, sorry...")
    