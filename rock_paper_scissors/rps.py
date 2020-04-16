#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    rps = ["rock", "paper", "scissors"]
    return[[rps[i] for i in nu]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
