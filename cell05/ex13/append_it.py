#!/usr/bin/env python3
import sys
import re
if len(sys.argv) == 1:
    print("none")
else:
    for i in sys.argv[1:]:
        if not re.search(r'ism$', i):  
            print(i + "ism")