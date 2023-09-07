#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    print("{} arguments".format(argc), end=":\n" if argc > 0 else ".\n")
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))
