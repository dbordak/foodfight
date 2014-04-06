print "I am thinking of a number between 1 and 10. \n Whoever is closer is the winner."
guess1 = raw_input("player 1 enter your guess:")
guess2 = raw_input("player 2 enter your guess:")

guess1= (int)(guess1)
guess2= (int)(guess2)

answer = (guess1+guess2)*8 %10

ans1=abs(answer-guess1)
ans2=abs(answer-guess2)

while(ans1==ans2):
  print "There is a tie, please try again"

  guess1 = raw_input("player 1 enter your guess:")
  guess2 = raw_input("player 2 enter your guess:")
  guess1= (int)(guess1)
  guess2= (int)(guess2)
  answer = ((guess1+guess2)*8) %10

  ans1=abs(answer-guess1)
  ans2=abs(answer-guess2)

if(ans1==0 or ans1<ans2):
  print ("player 1 is the winner")
elif(ans2==0 or ans1>ans2):
  print ("player 2 is the winner")