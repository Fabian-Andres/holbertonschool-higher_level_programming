#!/usr/bin/python3
class Square:

    def __init__(self, height="", width=""):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if value.isdigit():
            self.__height = value
        else:
            pass

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            pass

    def getArea(self):
        return int(self.__height) * int(self.__width)
