#!/usr/bin/python3
""" 17-main """
from models.square import Square

if __name__ == "__main__":

    r1 = Square.create(**{"size": 2})
    r1.display()
    print(r1)
