#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
argparse module demo.
"""

__author__ = 'Ziang Lu'

import argparse
import sys


def fib(n: int) -> int:
    """
    Calculates the given n-th Fibonacci number.
    :param n: int
    :return: int
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description='Calculates the num-th Fibonacci number'
    )

    # POSITIONAL argument
    parser.add_argument(
        'num',
        help='The n-th Fibonacci number to calculate (default: %(default)s)',
        type=int, default=10
    )
    # By using %(default)s, we can directly use the default value without repetition.
    # Note that if we set help=argparse.SUPPRESS, that help entry will be silenced

    # OPTIONAL argument
    # If not set and default is not specified, default to None
    parser.add_argument(
        '--output', help='Whether to also output to a text file',
        nargs='?', type=argparse.FileType('wt'), default=sys.stdout
    )
    # Note that nargs specifies the number of command-line arguments that should be consumed, and nargs='?' specifies
    # that one argument will be consumed from the command line, if possible; if no command-line argument is present,
    # the default value will be produced, which is sys.stdout in this case
    # Note that we can use FileType, which takes some arguments of open() function, to open the given file (value of
    # the argument)

    # Note that if we want to restrict the values that some optional argument can accept, we can do something like
    # choices=[0, 1, 2], or choices=range(3), or choices={0, 1, 2} (any object that supports the "in" operator)

    # Mutually exlusive arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', help='Output to console',
                       action='store_true')
    group.add_argument('-q', '--quiet', help='Simple output',
                       action='store_true')
    # action='store_true' turns the optional argument into a flag, rather than requiring some value, which means that
    # if -v or --verbose is specified, set it to True, and False otherwise.

    # Parse the arguments
    args = parser.parse_args()

    # Calculate the result
    print(f'num = {args.num}')
    result = fib(args.num)

    # Output to text file if specified
    print(f'output = {args.output}')
    if args.output:
        # with open(args.output, 'wt') as f:
        #     f.write(str(result) + '\n')
        # The above FileType('wt') creates a writable file, so we don't need to open the file by ourselves.
        args.output.write(str(result) + '\n')

    # Output in a verbose/quiet way as specified
    print(f'verbose = {args.verbose}')
    print(f'quiet = {args.quiet}')
    if args.verbose:
        print(f'The {args.num}th Fibonacci number is {result}.')
    elif args.quiet:
        print(result)
    else:
        print(f'fib({args.num}) = {result}')


if __name__ == '__main__':
    main()
