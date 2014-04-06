#!/bin/python2

import os
import subprocess
import getpass
import sys
sys.path.append("pyordrin")
import ordrin

GAME = "dummy"

key = os.environ.get('ORDRIN_API_KEY',"nope")
if key == "nope":
    print "API key not found!"
    exit(1)
api = ordrin.APIs(key)

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
    api.create_cc(email,"TestCard","4111111111111111","123","01/2015","Place Pl","Placetown","PL","01234","1231231234",pw)
    return email,pw

def getAccount(playerNo):
    print "What is player "+playerNo+"'s email?"
    email = raw_input().lower()
    print "What is player "+playerNo+"'s password?"
    pw = getpass.getpass("")
    print api.get_account_info(email,pw)
    return email,pw

def main():
    print "Note: If applicable, the resident of your current location"
    print "should be player 1."
    #print "Does player 1 have an account? [Y/n]"
    #ans = raw_input().lower()
    #if ans == "n" or ans == "no":
    #    player1 = createAccount("1")
    #else:
    #    player1 = getAccount("1")
    #print "Does player 2 have an account? [Y/n]"
    #ans = raw_input().lower()
    #if ans == "n" or ans == "no":
    #    player2 = createAccount("2")
    #else:
    #    player2 = getAccount("2")
    print "What address are you at?"
    street = raw_input()
    print "What city are you in?"
    city = raw_input()
    print "What is your Zip Code?"
    zip = raw_input()
    print "What is your quest?"
    raw_input()
    print api.delivery_list("ASAP",street,city,zip)





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
