#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-03-03
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='iupac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='SEQ', nargs='+', help='Input sequence(s)')
    '''
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        default=_io.TextIOWrapper,
                        name='<stdout>',
                        mode = 'w',
                        encoding='utf-8')
                        '''

    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """iupac"""

    args = get_args()
    seq=' '.join(map(str,args.seq))
    seq = seq.replace("'", "")
    seq = seq.replace("]", "")
    seq = seq.replace("[", "") 
    #args.seq = args.seq.upper()

    iupactable = {
        "A": "A",
        "C": "C",
        "G": "G",
        "T": "T",
        "U": "U",
        "R": "[AG]",
        "Y": "[CT]",
        "S": "[GC]",
        "W": "[AT]",
        "K": "[GT]",
        "M": "[AC]",
        "B": "[CGT]",
        "D": "[AGT]",
        "H": "[ACT]",
        "V": "[ACT]",
        "N": "[ACGT]"
    }

    ip = ''
    for char in seq:
        if char == '':
            ip += ","
            ip += seq
        else:
            ip +=  iupactable[char]

           
    p=''.join(seq)
    p+=" "
    p+=''.join(ip)

    print(p)


# --------------------------------------------------
if __name__ == '__main__':
    main()
