import argparse
from math import sqrt, ceil

# add arguments and parse
parser = argparse.ArgumentParser(description='find factors of integer.')
parser.add_argument('integer', metavar='N', type=int,
                    help='an integer for the accumulator')
args = parser.parse_args()

value = args.integer

# announce our mission
print('finding factors of {}'.format(value))

factors = []
# searching for factors from 1 to square root of number
for x in range(0, ceil(sqrt(value)) + 1, 1):
    # must be greater than 1
    if x > 1:
        # must cleanly divide, if so add both factors
        if(value % x == 0):
            if x not in factors:
                factors.append(x)
            multiplier = int(value / x)
            if multiplier not in factors:
                factors.append( multiplier)

if len(factors) > 0:
    print('factors:')
    for factor in factors:
        print(factor)
else:
    print('{} is a prime number'.format(value))