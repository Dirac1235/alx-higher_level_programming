#!/usr/bin/python3
"defines BaseGeometry class"


class BaseGeometry:
    def area(self):
        raise NotImplementedError("area() is not implemented")
