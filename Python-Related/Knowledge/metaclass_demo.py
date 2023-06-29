#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python metaclass demo.
"""


# Regular class definition
# class Hello:
#     def hello(self, name='World'):
#         print(f'Hello, {name}')


def func(self, name='World'):
    """
    This function will be bound to a class.
    :param self: object
    :param name: str
    """
    print(f'Hello, {name}')


# Create type "Hello", without needing to write the regular 'class Hello'
Hello = type('Hello', (object,), dict(hello=func))

# Test the newly created type "Hello"
h = Hello()
h.hello('Jack')

# Output:
# Hello, Jack


# Metaclass: 元类
# 定义metaclass ("type") -> 实例化metaclass ("type") => class (type)
# 定义class -> 实例化class -> object

class ListMetaclass(type):
    """
    ListMetaclass used to create classes (types) that has an "add()" method.
    """

    def __new__(cls, name, bases, attrs):
        # Constructor
        # This method is called when a new type is created.
        # Thus, we need to bind an "add()" method to that new type.
        attrs['add'] = lambda self, val: self.append(val)
        # Continue to call the super constructor
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    """
    When the type "MyList" is created, Python interpreter will call  ListMetaclass.__new__() to create the type
    "MyList", so the "add()" method will be bound to the type "MyList".
    """
    pass


# Test the newly created type "MyList" and its "add()" method
l = MyList()
l.add(1)
print(l)

# Output:
# [1]
