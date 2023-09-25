#!/usr/bin/python3
def safe_print_division(a, b):
    product = 0
    try:
        product = a / b
    except (ValueError, ArithmeticError):
        product = None
    finally:
        print("Inside result: {}".format(product))
        return product
