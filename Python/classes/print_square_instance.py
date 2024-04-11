#!/usr/bin/python3
# print_square_instance
"""Define a class square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square
        Args:
            size (int): The size of the new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrives the value of the private size attribute"""
        return self.__size
    
    @property
    def position(self):
        """Retrieves the attribute of the private position attribute"""
        return self.__position

    @size.setter
    def size(self, value):
        """Set the value of the private size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the value of the private position attribute"""
        if (not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(num, int) for num in value) or \
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
    
    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        x, y = self.__position
        for _ in range(y):
            print()
        for _ in range(self.__size):
            print(" " * x + "#" * self.__size)
    
    def __str__(self):
        """prints in stdout the square with the character #"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
