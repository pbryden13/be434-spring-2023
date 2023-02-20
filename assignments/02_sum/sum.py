#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-02-01
Purpose: sum(HW2)
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='sum the numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='num',
                        type=int,
                        nargs='+',
                        help='numbers to be added')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """sum the numbers"""

    args = get_args()
    n = args.numbers
    num = len(n)

    if num == 1:
        print(n[0], '=', n[0])

    else:
        n2 = 0
        for i in range(0, num, 1):
            n2 = n[i] + n2
        nm = n[0:-1]
        for item in nm:
            print(item, end=" + ")
        print(n[-1], '=', n2)


# --------------------------------------------------
if __name__ == '__main__':
    main()
