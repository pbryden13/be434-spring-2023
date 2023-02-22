#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-02-13
Purpose: hw4 cat
"""
import os
import io
import sys
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='hw4 cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    args = parser.parse_args()

    if os.path.isfile(args.file):
        file_exists = os.path.exists(args.file)
        if file_exists==True:
            args.file = open(args.file).read().rstrip()
        else:
            print(f"No such file or directory: '{args.file}'")

    return args

# --------------------------------------------------
def main():
    """read files"""

    args = get_args()

    print(args.file)
    
    #str_arg = args.arg
    
    #flag_arg = args.on
    #pos_arg = args.positional

    #print(f'str_arg = "{str_arg}"')
    #print(f'int_arg = "{int_arg}"')
    #print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    #print(f'flag_arg = "{flag_arg}"')
    #print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
