#!/usr/bin/python3
import sys
argc = len(sys.argv) - 1
print("{} arguments".format(argc), end=":\n" if argc > 0 else ".\n")
for i in range(1, argc + 1):
    print("{}: {}".format(i, sys.argv[i]))
