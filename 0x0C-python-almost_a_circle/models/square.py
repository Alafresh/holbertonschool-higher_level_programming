#!/usr/bin/pyhton3
"""Import module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Base Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor initialize"""
        super().__init__(size, size, x, y, id)
