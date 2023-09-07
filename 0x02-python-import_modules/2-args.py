#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    print("{} arguments".format(argc if argc > 1 else 0),
          end=":\n" if argc > 1 else ".\n")
    if (argc >= 2):
        for i in range(1, argc):
            print("{}: {}".format(i, sys.argv[i]))
