import string
from random import choices, choice
import sys
import argparse

def create_password(length=8, upper=False, lower=False, digit=False, punc=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if punc:
        pool += string.punctuation
    else:
        pool += string.ascii_letters

    return ''.join(choices(pool, k=length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('length',type=int , help='Length of password')
    parser.add_argument('-u','--upper', help='use upper case',action='store_true')
    parser.add_argument('-l','--lower', help='use lower case',action='store_true')
    parser.add_argument('-d','--digit', help='use digit case',action='store_true')
    parser.add_argument('-p','--punc', help='use punc case',action='store_true')

    args = parser.parse_args()
    # print(args)
    print(create_password(args.length,args.upper,args.lower,args.digit,args.punc))
    # print(create_password(20, upper=True))
    # print(create_password(lower=True))
    # print(create_password(digit=True, upper=True))
    # print(create_password(punc=True, upper=True, digit=True))



