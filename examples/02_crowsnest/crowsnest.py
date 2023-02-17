#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-01-30
Purpose: Choose the article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='the thing we see')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word=args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    #print('Ahoy, Captain, {} {} off the larboard bow!'.format(article,word))
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
