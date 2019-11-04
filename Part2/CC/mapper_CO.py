#!/usr/bin/env python
"""mapper.py"""

import sys

top10_list = ["page", "player", "coach", "live", "servic", "use", "game", "soccer", "program", "program"]

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tweetts = line.split("\n\n")
    # increase counters

    for tweet in tweetts:
        myList = []
        words = line.split()
        for topWord in top10_list:
            if topWord in tweet:
                myList.append(topWord)

    for topWord in myList:
        for word in words:
            if word != topWord:
                print "%s|%s\t%s" % (topWord,word,1)