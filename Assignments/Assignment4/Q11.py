#Challenge: Create your own custom exception that will handle user input that is NOT in the appropriate range of values you want them to enter (such as a percentage mark must be between 0 and 100)
#HINT: You will need to use classes!

class Error(Exception):
   pass
class valNotInRange(Error):
   pass

while True:
   try:
       yournum = int(input("What is your percentage mark?"))
       if yournum < 0 or yournum > 100:
           raise valNotInRange
       break
   except valNotInRange:
       print("your input was not in range")
