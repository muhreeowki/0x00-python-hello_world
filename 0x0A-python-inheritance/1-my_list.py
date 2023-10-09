"""Module that contains a Class called MyList that inherits the list class"""


class MyList(list):
    """This is a child class of the list class"""
    def print_sorted(self):
        """Method that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
