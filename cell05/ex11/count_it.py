#!/usr/bin/env python3
import sys
if len(sys.argv) == 1:
    print("none")
else:
    parasen = len(sys.argv) -1
    print(f"parameters: {parasen}")
    for i in range(1,parasen + 1):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
