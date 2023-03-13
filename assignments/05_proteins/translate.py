#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@localhost>
Date   : 2023-03-13
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='HW5',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'sequence',
        help='DNA/RNA sequence',
        type=str,
    )

    parser.add_argument(
        '-c',
        '--codons',
        help='input codon file',
        nargs='?',
        metavar='FILE',
        type=argparse.FileType('rt'),
        required=True,
    )

    parser.add_argument('-o',
                        '--outfile',
                        help='output file name',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """proteins translate main"""

    args = get_args()

    out = args.outfile

    # makes codon input a dict
    codon_table = {}
    for line in args.codons:
        ln = line.rstrip().split()
        ln1 = ln[0]
        ln2 = ln[1]
        codon_table.update({ln1: ln2})
    # print(codon_table)

    k = 3
    seq = args.sequence
    codontrans = []
    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1, 3)]:
        # print(f'{codon} = {codon_table.get(codon.upper())}',end='', file=out)
        # print(codon,file=out)
        # print(codon, " = ", codon_table.get(codon.upper()))
        codontrans.append(codon_table.get(codon.upper()))

    tcodes = ''.join(str(codontrans).split(','))
    tcodes = ''.join(str(tcodes).split())
    tcodes = tcodes.replace("'", "")
    tcodes = tcodes.replace("[", "")
    tcodes = tcodes.replace("]", "")
    tcodes = tcodes.replace("None", "-")

    # print("seq = ", args.sequence, file=out)
    print(tcodes, file=out)
    # print(f'{"Output written to "}"{args.outfile.name}{"."}"',
    # end="'",file=out)
    # print("'seq =", args.sequence,end=' \n')
    # print('codons =', tcodes,end='')
    print(f'{"Output written to "}"{args.outfile.name}".', end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()

