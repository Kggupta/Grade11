#My python program to check if a user inputted number is prime or not
#it will then tell you how many prime numbers you entered
PrimeNumberList = []
class Error(Exception):
   pass
class InputNotPositive(Error):
   pass
class InputIs1(Error):
   pass
class InputNotInteger(Error):
   pass

def userQuits():
   print("You Entered {} prime numbers".format(len(PrimeNumberList)))

def CalculateIfPrime(UserValue):
   if UserValue > 1:
       # check for factors
       for iteration in range(2, UserValue):
           if (UserValue % iteration) == 0:
               print("That is NOT prime")
               break
       else:
           print("That IS prime")
           PrimeNumberList.append(UserValue)

print("Type 0 to quit.")
while True:
   try:
       UserInputNumber = float(input("Enter a positive integer value: "))
       if UserInputNumber < 0:
           raise InputNotPositive
       elif UserInputNumber == 1:
           raise InputIs1
       elif UserInputNumber == 0:
           userQuits()
       elif UserInputNumber.is_integer == False:
           raise InputNotInteger
       else:
           CalculateIfPrime(int(UserInputNumber))
   except InputNotInteger:
       print("That is not an integer!")
   except InputNotPositive:
       print("Enter a POSITIVE integer!")
   except InputIs1:
       print("1 is neither prime nor composite!")
   except ValueError:
       print("That is not a number!")
