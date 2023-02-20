#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-02-19
Purpose: picnic listing
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='items for picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='item',
                        type=str,
                        nargs='+',
                        help='items we are bringing')

    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main area"""
    
    args=get_args()
    items=args.items
    num=len(items)
    
    if args.sorted:
        items=sorted(items)

    bringing=''

    if num==1:
        bringing=items[0]
        #print(f'You are bringing {items[0]}.')
    elif num==2:
        bringing=f'{items[0]} and {items[1]}'
        #print(f'You are bringing {items[0]} and {items[1]}.')
    else:
        items[-1]='and ' + items[-1]
        bringing=f', '.join(items)
        #bringing = ', '.join(item[:-1]) + ', and' +items[-1]

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
