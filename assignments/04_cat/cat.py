#!/usr/bin/env python3

"""
Author : philipbryden <philipbryden@arizona.edu>
Date   : 2023-02-13
Purpose: hw4 cat
"""
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='hw4 cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        nargs='*',
                        metavar='FILE',
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-n',
                        '--number',
                        help=' boolean flag "with lines"',
                        action='store_true')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """read files"""

    args = get_args()

    for fh in args.file:
        line = args.file
        if args.number is True:
            line_num = 1
            for line in fh:
                print(f'{line_num:6}\t{line}', end='')
                line_num += 1
        else:
            for line in fh:
                print(f'{line}', end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
