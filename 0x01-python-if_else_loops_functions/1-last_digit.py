#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number > 0 else number % -10
print(f"Last digit of {number} is {last} and is", end=" ")
if last == 0:
	print("zero")
elif last > 5:
	print("greater than 5")
else:
	print("less than six and not 0")
