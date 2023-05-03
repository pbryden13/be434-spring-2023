#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-04-07
Purpose: create password example code
"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='password ex code',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num',
                        type=int,
                        default='3')

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words per password',
                        metavar='words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minium length of word',
                        metavar='words',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maxinum length of word',
                        metavar='max',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='',
                        metavar='Seed for random',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate the password',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make password prog work here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)

    passwords = []
    for _ in range(args.num):
        passwords.append(''.join(random.sample(words, k=args.num_words)))
        #print(l33t(password) if args.l33t else password)

    if args.l33t:
        #passwords = [l33t(word) for word in passwords]
        passwords = map(l33t, passwords)

    print('\n'.join(passwords))


# --------------------------------------------------
def clean(word):
    """Remove non-letters from word"""

    return re.sub('[^a-zA-Z]', '', word)


# --------------------------------------------------
def ransom(text):
    """Randomly choose an upper or lowercase letter to return"""

    return ''.join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text))


# -------------------------------------------------
def l33t(text):
    """l33t"""

    text = ransom(text)
    xform = str.maketrans({
        'a': '@',
        'A': '4',
        'O': '0',
        't': '+',
        'E': '3',
        'I': '1',
        'S': '5'
    })

    return text.translate(xform) + random.choice(string.punctuation)


# -------------------------------------------------

if __name__ == '__main__':
    main()
