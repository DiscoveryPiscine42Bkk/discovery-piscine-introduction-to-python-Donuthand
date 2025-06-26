#!/usr/bin/env python3
import sys
import re
if len(sys.argv) < 3:
    print("none")
else:
    text = sys.argv[2]
    pattern = sys.argv[1]
    matches = re.findall(pattern,text)
    print(len(matches))