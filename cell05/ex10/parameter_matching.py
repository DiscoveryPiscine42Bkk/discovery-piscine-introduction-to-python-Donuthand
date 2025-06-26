#!/usr/bin/env python3
import sys
if len((sys.argv)) != 2:
    print("none")
else:
    ques = sys.argv[1]
    ans = input(f"What was the parameter? ")
    if ques == ans:
        print("Good Job!")
    else:
        print("Nope, sorry...")