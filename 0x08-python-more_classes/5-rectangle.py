
#!/usr/bin/python3
""" This is Rectangle Class """


class Rectangle:
    """ Define the width and height """
    def __init__(self, width=0, height=0):
        """ Initialization of attributes for width and height """
        self.width = width
        self.height = height

    def area(self):
        """" Instance method that returns rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ Instance method that returns rectangle perimeter """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ return the string to print rectangle """
        rect = ""
        for i in range(self.height):
            for j in range(self.width):
                rect += '#'
            if i != self.height - 1 and self.width != 0:
                rect += '\n'
        return rect

    def __repr__(self):
        """ return the representation of objet """
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """ Call this instance for delete rectangle """
        print("Bye rectangle...")

    @property
    def width(self):
        """ @property for width """
        return self.__width

    @property
    def height(self):
        """ @property for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ @width.setter attribute """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ @height.setter attribute """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
