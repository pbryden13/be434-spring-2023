#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-02-12
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='What is the greeting',
                        metavar='greeting',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='What is the name',
                        metavar='name',
                        type=str,
                        default='Stranger')

    parser.add_argument(
        '-e',
        '--excited',
        help='Include an exclamation point',
        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    flag_arg = args.excited
    if flag_arg is True:
        punch = '!'

    else:
        punch = '.'

    print(f'{greeting}, {name}{punch}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
