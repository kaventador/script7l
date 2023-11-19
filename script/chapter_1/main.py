import string
from random import choices, choice
import sys

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
    try:
        length = (int(sys.argv[1]))
    except ValueError :
        print('Enter Integer')
    else:
        print(create_password(length))
    # print(create_password(20, upper=True))
    # print(create_password(lower=True))
    # print(create_password(digit=True, upper=True))
    # print(create_password(punc=True, upper=True, digit=True))



