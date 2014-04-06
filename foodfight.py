#!/bin/python2

import subprocess
import sys
sys.path.append("pyordrin")
import ordrin

GAME = "dummy"

api = ordrin.APIs("G2emJ1PT6VbytwD9guV3mvEWEvV9TBd4r_Uh6PAm78E")

def main():
    print "Does player 1 have an account? [Y/n]"
    ans = raw_input().lower()
    if ans == "n" or ans == "no":
        player1 = createAccount()
    else:
        print "What is player 1's username?"
    print "Does player 2 have an account? [Y/n]"
    ans = raw_input().lower()
    if ans == "n" or ans == "no":
        player2 = createAccount()
    else:
        print "What is player 2's username?"




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
