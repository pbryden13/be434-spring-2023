#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@larizona.edu>
Date   : 2023-03-19
Purpose: syn dna/rna createor
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # number of seqs to make
    parser.add_argument('-n',
                        '--numseqs',
                        help='The number of sequences to generate',
                        metavar='seq num',
                        type=int,
                        default='10')

    # the min len of seqs
    parser.add_argument('-m',
                        '--minlen',
                        help='The minimum length for any sequence',
                        metavar='min len num',
                        type=int,
                        default='50')

    # the max len of seqs
    parser.add_argument('-x',
                        '--maxlen',
                        help='The maximum length for any sequence',
                        metavar='max len num',
                        type=int,
                        default='75')

    # the % of GC content per seq
    parser.add_argument('-p',
                        '--pctgc',
                        help='The percent GC content for sequence',
                        metavar='% of GC',
                        type=float,
                        default='0.5')

    # the type of seq to make
    parser.add_argument('-t',
                        '--seqtype',
                        help='seq in DNA or RNA',
                        metavar='dna or rna',
                        type=str,
                        default='dna')

    # sets seed for testing
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed num',
                        type=int,
                        default=None)

    # sets out file w/ default
    parser.add_argument('-o',
                        '--outfile',
                        help='output file name',
                        metavar='str',
                        type=str,
                        default='out.fa')

    args = parser.parse_args()

    if os.path.isfile(args.outfile):
        os.remove(args.outfile)

    if args.numseqs < 1:
        parser.error(f'--number "{args.numseqs}" must be < 1')

    if args.minlen < 1:
        parser.error(f'--number "{args.minlen}" must be < 1')

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    if args.seqtype != 'dna':
        if args.seqtype != 'rna':
            parser.error(f'--seqtype "{args.seqtype}" must be dna or rna only')

    return args


# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """Create the pool of bases"""
    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


# --------------------------------------------------
def main():
    """Make syn dna/rna"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    out_fh = open(args.outfile, 'wt')

    for n in range(args.numseqs):
        print(f'>{n+1}', file=out_fh)
        seq_len = random.randint(args.minlen, args.maxlen)
        # print(f'seqlen={seq_len}')
        for _ in range(seq_len):
            seq = ''.join(random.sample(pool, seq_len))
        print(f'{seq}', file=out_fh)

    print(
        f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile}".'
    )


# --------------------------------------------------
if __name__ == '__main__':
    main()
