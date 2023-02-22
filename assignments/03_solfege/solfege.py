#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-02-6
Purpose: solfege
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', nargs='+', help='Song Words')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """word checker"""

    args = get_args()
    text = args.text

    song = {
        'Do': 'Do, A deer, a female deer',
        'Re': 'Re, A drop of golden sun',
        'Mi': 'Mi, A name I call myself',
        'Fa': 'Fa, A long long way to run',
        'Sol': 'Sol, A needle pulling thread',
        'La': 'La, A note to follow sol',
        'Ti': 'Ti, A drink with jam and bread',
    }
    for i in range(len(text)):
        print(song.get(text[i], f'I don\'t know "{text[i]}"'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
