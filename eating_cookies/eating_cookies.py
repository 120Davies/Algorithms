#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# Will slight modification, this could be used for a more general problem:
# "Cookie monster may any number of cookies at once, up to {m}.
# There are {ways} ways for Cookie Monster to eat {n} cookies."
# Just add an 'm' argument, and replace all the 3's with m.
# This should work to pass the test_eating_cookies though.
def eating_cookies(n, cache=None):
    if n<2:
        return 1
    elif n==2:
        return 2

    if cache == None:
        cache = [None]*(n+1)
    else:
        cache = cache
    if cache[n] == None or cache[n] == 0:
        for i in range(3):
            cache[n-(3-i)] = eating_cookies(n - (3-i), cache)
        step = 0
        for i in range(3):
            step = step + cache[n-(3-i)]
        cache[n] = step
        return cache[n]
    else:
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
