#!/usr/bin/python

import sys
from math import ceil

def remains(amount, denominations):
    return[amount-i*denominations for i in range(amount//denominations+1)]

def making_change(amount, denominations, cache=None):
    if len(denominations) == 2:
        return amount//denominations[1]+1
    if cache == None:
        cache = {i: [None]*(amount+1) for i in denominations}
    if cache[denominations[-1]][amount] == None:
        cache[denominations[-1]][amount] =\
            sum([making_change(a, denominations[:-1])
                for a in remains(amount, denominations[-1])])
        return cache[denominations[-1]][amount]
    else:
        return cache[denominations[-1]][amount]

print(making_change(1000, [1, 5, 10, 25, 50]))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")

# check. It took 8 seconds though.
