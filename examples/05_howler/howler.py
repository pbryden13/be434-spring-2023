#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@arizona.edu>
Date   : 2023-02-13
Purpose: howler example
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='howler example',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                            metavar='str',
                            help='input text')

    parser.add_argument('-o',
                        '--outfile',
                        help='out put file name',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """howler example"""

    args = get_args()

    out_fh = None

    if args.outfile:
        out_fh = open(args.outfile, 'wt')
        #print(args.text.upper(), file=open(args.outfile, 'wt'))
    else:
        out_fh = sys.stdout
        #print(args.text.upper())
    print(args.text.upper(), file=out_fh)

# --------------------------------------------------
if __name__ == '__main__':
    main()
