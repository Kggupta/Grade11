#Write a program to ask for and then check the alphabetical order of two words by comparing them in an if statement. Print out which of the two words is alphabetically first.

firstw = str(input("Enter a word:"))
secondw = str(input("Enter another word:"))

if (secondw < firstw):
   print(secondw," is the bigger word")
elif (firstw < secondw):
   print(firstw, " is bigger")
else:
   print("They are the same")

#the code compares the values of the strings capital letters are <normal letters. z is the “biggest” letter while a capital A is the smallest.
#The letters get bigger and bigger as they go down the alphabet
