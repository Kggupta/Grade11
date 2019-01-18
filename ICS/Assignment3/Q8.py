#Write a program to simulate the playing of a simple dice game (played with one die).
#Roll the die to get a value from 1 to 6. This we will call your point.
#Now keep rolling until you get the same value (your point) again and see how many rolls it takes.
#Program it so you can play this game repeatedly.

import random

print("This is a dice game. I roll a die and that will be my main value. I keep rolling the die until i get the same value again.")

def maingame():
   initialdiceroll = 0
   nextroll = 0
   rollnumber = 0
   userinput = ""
   initialdiceroll = random.randint(1,6)
   print("Your first roll and point value is: {}".format(initialdiceroll))
   while initialdiceroll != nextroll:
       nextroll = random.randint(1,6)
       print("Next roll is: {}".format(nextroll))
       rollnumber += 1
   print("It took {} times to get your point again.".format(rollnumber))
   userinput = input("Do you want to play again?(Y/N)")
   if userinput == "N":
       exit()
   elif userinput == "Y":
       maingame()

maingame()
