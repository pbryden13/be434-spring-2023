#! /usr/bin/env python3

# Say hello
#print('Hello, World!') #say hello!

#print('Hello, Universe')

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
name= args.name
print('Hello, ' + args.name + '!')