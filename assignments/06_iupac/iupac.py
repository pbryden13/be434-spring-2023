#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-03-03
Purpose: Rock the Casbah
"""

import argparse
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='iupac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='SEQ', nargs='+', help='Input sequence(s)')
    
    parser.add_argument('-o',
                        '--outfile',
                        help='output file name',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    args = parser.parse_args()
    return args


# --------------------------------------------------


def main():
    """iupac"""

    args = get_args()
    seq=' '.join(map(str,args.seq))
    seq = seq.replace('"', "'")
    seq = seq.replace("]", "")
    seq = seq.replace("[", "")

    #print(seq)
    

    iupactable = {
        'A': 'A',
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

    p=''
    #p+="'"
    p+=args.seq[0]
    p+=" "
    
    for char in seq:
        if char == " ":
            p+="', '"
            p+=args.seq[1]
            p+=" "
        else:
            p+=iupactable[char]
    
    print(p)  



# --------------------------------------------------
if __name__ == '__main__':
    main()
