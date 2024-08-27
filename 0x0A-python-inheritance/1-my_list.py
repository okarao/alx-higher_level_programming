#!/usr/bin/python3
'''
Define a class MyList that inherits from lists

'''

class MyList(list):
    """
    Class MyList that inherits from list

    """

    def print_sorted(self):
        """
        
        Prints the list ascending order
        Assumes that all the elements of the list will be of type int
        
        """
        print(sorted(self))
