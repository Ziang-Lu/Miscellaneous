#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
argparse module simple example.
"""

__author__ = 'Ziang Lu'

import argparse


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
        'num', help='The Fibonacci number you wish to calculate.', type=int
    )

    # OPTIONAL argument
    # If not set and default is not specified, default to None
    parser.add_argument('--output',
                        help='Whether to also output to a text file')
    # Note that if we want to restrict the values that some optional argument
    # can accept, we can do something like choices=[0, 1, 2]

    # Mutually exlusive arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', help='Output to console.',
                       action='store_true')
    group.add_argument('-q', '--quiet', help='Output to group',
                       action='store_true')
    # action='store_true' turns the optional argument into a flag, rather than
    # requiring some value, which means that if -o or --output is specified,
    # set it to True, and False otherwise.

    # nargs ???

    # Parse the arguments, result in a Namespace object
    args = parser.parse_args()

    # Calculate the result
    print(f'num = {args.num}')
    result = fib(args.num)

    # Output to text file if specified
    print(f'output = {args.output}')
    if args.output:
        with open(args.output, 'wt') as f:
            f.write(str(result) + '\n')

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
