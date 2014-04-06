#!/bin/python2

import os
import subprocess
import getpass
import sys
sys.path.append("pyordrin")
import ordrin

GAME = "dummy"

def createAccount(playerNo):
    print "What is player "+playerNo+"'s first name?"
    f_name = raw_input()
    print "What is player "+playerNo+"'s last name?"
    l_name = raw_input()
    print "What is player "+playerNo+"'s email?"
    email = raw_input().lower()
    print "What is player "+playerNo+"'s password? (WARNING: Not secure. Yet.)"
    pw = getpass.getpass("")
    api.create_account(email, pw, f_name, l_name)


def main():
    key = os.environ.get('ORDRIN_API_KEY',"nope")
    if key == "nope":
        print "API key not found!"
        return 1
    api = ordrin.APIs(key)
    print "Note: If applicable, the resident of your current location"
    print "should be player 1."
    print "Does player 1 have an account? [Y/n]"
    ans = raw_input().lower()
    if ans == "n" or ans == "no":
        player1 = createAccount("1")
    else:
        print "What is player 1's email?"
        email = raw_input().lower()
        print "What is player 1's password?"
        pw = getpass.getpass("")
        api.get_account_info(email,pw)
    print "Does player 2 have an account? [Y/n]"
    ans = raw_input().lower()
    if ans == "n" or ans == "no":
        player2 = createAccount("2")
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
