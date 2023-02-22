#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@arizona.edu>
Date   : 2023-02-6
Purpose: jump the five example
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='input text')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """jump the five main"""

    args = get_args()
    text=args.text

    jumper={'1':'9',
            '2':'8',
            '3':'7',
            '4':'6',
            '5':'0',
            '6':'4',
            '7':'3',
            '8':'2',
            '9':'1',
            '0':'5'}

    for char in text:
        print(jumper.get(char,char),end='')
        #newtext += jumper.get(char,char)

    #print(newtext)
# --------------------------------------------------
if __name__ == '__main__':
    main()
