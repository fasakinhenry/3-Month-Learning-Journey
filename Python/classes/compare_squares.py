#!/usr/bin/python3
# square_set_get
"""Define a class square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): The size of the new square"""
        self.size = size
        

    @property
    def size(self):
        """Retrives the value of the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the private size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
    
    # Check the comparision of the sqaures with other squares

    def __lt__(self, other):
        """Define the < comparison of the square"""
        return self.area() < other.area()
    
    def __le__(self, other):
        """Define the <= comparison of the square"""
        return self.area() <= other.area()
    
    def __eq__(self, other):
        """Define the == comparison of the square"""
        return self.area() == other.area()
    
    def __ne__(self, other):
        """Define the != comparison of the square"""
        return self.area() != other.area()
    
    def __gt__(self, other):
        """Define the > comparison of the square"""
        return self.area() > other.area()
    
    def __ge__(self, other):
        """Define the >= comparison of the square"""
        return self.area() >= other.area()
