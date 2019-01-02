#Make up your own question on a topic not covered in the above questions.

import turtle
import random
def secretnumgame():
   secretnumber = 0
   playerguess = 0
   lowrange = 0
   highrange = 0
   turncount = 0
   keepplaying = ""
   print("This is a game that will get a random value that you have to guess.")
   lowrange = int(input("First i need to know the range that i can pick a number from randomly, enter the LOW range: "))
   highrange = int(input("Now enter the HIGH range. this is the max the number can be: "))
   secretnumber = random.randint(lowrange,highrange)
   while secretnumber != playerguess:
       playerguess = int(input("Guess the integer between numbers {} and {}:\n".format(lowrange,highrange)))
       turncount += 1
       if playerguess == secretnumber:
           continue
       else:
           print("NOPE! Try again!")

   print("YES! Good job the number was {} and it took {} turns to guess.".format(secretnumber,turncount))
   keepplaying = input("Keep playing?(Y/N) ")
   if keepplaying == "N":
       turtle.write("BYE", move=False, align="left", font=("Arial", 200, "normal"))
       turtle.done()
   else:
       secretnumgame()

secretnumgame()
