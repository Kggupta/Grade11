#Write a program to ask the user for a number. Print out what category the number falls into: negative, zero or positive.

usernumber = float(input("Input any number and i will tell you if it is positive or negative or zero:"))

if usernumber < 0:
   print("Your number was negative!")
elif usernumber == 0:
   print("The number was equal to zero!")
elif usernumber > 0:
   print("The number was positive")
