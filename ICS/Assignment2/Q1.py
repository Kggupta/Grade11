#Write a program that asks a student for how many high school credits they have. Tell them if they have enough to graduate (in Ontario that is at least 30), otherwise tell them they do not have enough.

credits = int(input("Enter the amount of credits you have:"))

if credits >= 30:
   print("You have enough credits to graduate")
else:
   print("You do not have enough credits to graduate")
