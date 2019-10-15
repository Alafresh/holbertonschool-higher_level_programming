#!/usr/bin/python3


class MyInt(int):

    def __eq__(self, other):
        super().__ne__(self)

    def __ne__(self, other):
        super().__eq__(self)
