#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 or i % 3 == 0:
            if (i % 5 == 0 and i % 3 == 0):
                print("FizzBuzz", end=" ")
            else:
                print("Fizz" if i % 3 == 0 else "Buzz", end=" ")
        else:
            print(i, end=" ")
