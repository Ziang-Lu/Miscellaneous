#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ziang Lu'

import logging

# Set the level of the logging messages to print
logging.basicConfig(level=logging.INFO)


def foo(s: str) -> float:
    n = int(s)
    logging.info('n = {}'.format(n))
    return 10 / n


def main():
    print(foo('0'))


if __name__ == '__main__':
    main()


# Output:
# INFO:root:n = 0
# Traceback (most recent call last):
#   File "err.py", line 19, in <module>
#     main()
#   File "err.py", line 15, in main
#     print(foo('0'))
#   File "err.py", line 11, in foo
#     return 10 / n
# ZeroDivisionError: division by zero
