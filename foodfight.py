#!/bin/python2

import subprocess
import sys
sys.path.append("pyordrin")
import ordrin

GAME = "dummy"

api = ordrin.APIs("G2emJ1PT6VbytwD9guV3mvEWEvV9TBd4r_Uh6PAm78E")

def main():
    print "Do both of you have accounts? [Y/n]"
    ans = raw_input().lower()
    if ans == "n" or ans == "no":
        print "Does player 1 have an account? [y/N]"
        ans = raw_input().lower()
        #if not(ans == "y" or ans == "yes"):


if __name__ == "__main__":
    main()

#First, get address.

#Next, find restaurants in area.

#Next, pick restaurant

#Next, list items

#Next, pick items for first person

#Then second person

#Now add first person's info

#Now add second person's info

#Now trigger game

#Now call order
