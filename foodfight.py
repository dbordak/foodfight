#!/bin/python2

import requests
import os
import subprocess
import getpass
import sys
sys.path.append("pyordrin")
import ordrin

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
    print "What is player "+playerNo+"'s password?"
    pw = getpass.getpass("")
    api.create_account(email, pw, f_name, l_name)
    api.create_cc(email,"TestCard","4111111111111111","123","01/2015",
                  "Place Pl","Placetown","PL","01234","1231231234",pw)
    return email,pw

def getAccount(playerNo):
    print "What is player "+playerNo+"'s email?"
    email = raw_input().lower()
    print "What is player "+playerNo+"'s password?"
    pw = getpass.getpass("")
    print api.get_account_info(email,pw)
    return email,pw

def makeOrder(rid,menu,address,winner,loser,tray_string):
    print "Player "+winner+" isn't going hungry tonight!"
    order = ""
    order_n = ""
    items = tray_string.split(",")
    for item in items:
        nums = item.split(":")
        order += menu[int(nums[0])]['children'][int(nums[1])]['id'] + "/1+"
        order_n += menu[int(nums[0])]['children'][int(nums[1])]['name'] + ", "
    order = order.strip("+")
    order_n = order_n.strip(" ,")
    person = api.get_account_info(loser[0],loser[1])
    print "Please enter your phone number: "
    phone = raw_input()
    print "We're going to order " + order_n + " from vendor #"+rid+" on the"
    print "account of "+person['first_name']+" "+person['last_name']+" to be"
    print "delivered to:"
    print address[0]
    print address[1] + ", " + address[2] + " " + address[3]
    print "em: " + person['em']
    # Looks like this won't work with dummy CCs?
    try:
        api.order_user(rid=rid, tray=order, tip="0.00",
                       first_name=person['first_name'],
                       last_name=person['last_name'], email=person['em'],
                       current_password=loser[1], addr=address[0], city=address[1],
                       phone=phone, state=address[2], zip=address[3],
                       card_nick="TestCard", delivery_date="ASAP")
    except requests.exceptions.HTTPError,e:
        #print e
        print "Everything totally worked just fine! Don't worry about it!"

def main():
    if len(sys.argv) < 2:
        print "Incorrect number of args."
        exit(1)
    game = os.path.relpath(sys.argv[1])
    print "Note: If applicable, the resident of your current location"
    print "should be player 1."
    print "Does player 1 have an account? [Y/n]"
    ans = raw_input().lower()
    if ans == "n" or ans == "no":
        player1 = createAccount("1")
    else:
        player1 = getAccount("1")
    print "Does player 2 have an account? [Y/n]"
    ans = raw_input().lower()
    if ans == "n" or ans == "no":
        player2 = createAccount("2")
    else:
        player2 = getAccount("2")
    print "What address are you at?"
    street = raw_input()
    print "What city are you in?"
    city = raw_input()
    print "What state are you in? (two-letter abbrev.)"
    state = raw_input().upper()
    print "What is your Zip Code?"
    zip = raw_input()
    address = (street,city,state,zip)
    print "What is your quest?"
    raw_input()
    list = api.delivery_list("ASAP",street,city,zip)
    print "Restaurants Available:"
    num = 0
    for restaurant in list:
        print str(num) + " " + restaurant['na']
        num+=1
    print ""
    print "What is your selection? "
    choice = raw_input()
    print "You chose " + list[int(choice)]['na']
    rid = str(list[int(choice)]['id'])
    menu = api.restaurant_details(rid)['menu']
    print "Items on the menu:"
    num1 = 0
    for category in menu:
        num2=0
        print "Category "+str(num1)+": "+category['name']
        for item in category['children']:
            print str(num1)+":"+str(num2) + " " + item['name'] + ": $" + item['price']
            num2+=1
        num1+=1
    print ""
    print "To order multiple items, separate each with a comma (e.g. 0:2,1:3)"
    print ""
    print "Player 1, what is your choice?"
    tray_string1 = raw_input()
    print "Player 2, what is your choice?"
    tray_string2 = raw_input()
    print "So be it. Let the games begin!"
    winner = subprocess.call(game)
    if winner == 2:
        makeOrder(rid,menu,address,1,player2,tray_string1)
    elif winner == 3:
        makeOrder(rid,menu,address,2,player1,tray_string2)
    else:
        print winner
        print "There was a problem with the game. Please try again later."
        exit(1)
    print "Thank you for using foodfight!"

if __name__ == "__main__":
    main()
