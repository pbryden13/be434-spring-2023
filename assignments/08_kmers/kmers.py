#!/usr/bin/env python3
"""
Author : philipbryden <philipbryden@larizona.edu>
Date   : 2023-03-24
Purpose: kmers HW
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='KMERS HW',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)
    
    parser.add_argument('FILE1',
                        metavar='str',
                        help='Input File 1')
    
    parser.add_argument('FILE2',
                        metavar='str',
                        help='Input File 2')
    
    args = parser.parse_args()
    
    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')
    
    if os.path.isfile(args.FILE1)==False:
        parser.error(f"No such file or directory: '{args.FILE1}'")

    if os.path.isfile(args.FILE2)==False:
        parser.error(f"No such file or directory: '{args.FILE2}'")
    
    return args


# --------------------------------------------------

# --------------------------------------------------
def findkmers(seq,k):
    """find k-mers in string"""

    n =len(seq)-k +1

    print(n)
    
    #return [] if n <1 else [seq[i:i + k] for i in  range (n)]
# --------------------------------------------------
def main():
    """kmers HW code............"""

    args = get_args()
    k=args.kmer

    worde=[]
    with open(args.FILE1,'r')as file:
        for line in file:
            for word in line.split():
                worde.append(word)
    sorted.splitlines(worde)
                
    print(worde)

    worde2=[]
    with open(args.FILE2,'r')as file:
        for line in file:
            for word in line.split():
                worde2.append(word)
   
    #print(worde2)

    words1 = {}
    for line in args.FILE1:
        for word in line.split(" "):
            #for kmer in findkmers(word,k):
               
            words1[word] = 1
    
    print(words1)

    words2 = {}
    for line in args.FILE2:
        for word in line.split():
            #for kmer in findkmers(word,k):
                
            words2[word] = 1
    
    #print(words2)


# --------------------------------------------------
if __name__ == '__main__':
    main()
