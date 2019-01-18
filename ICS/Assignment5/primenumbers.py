#My python program to check if a user inputted number is prime or not
#it will then tell you how many prime numbers you entered
PrimeNumberList = [] #list where i will be storing the prime numbers that the user enters
class Error(Exception):#custom error detectors
   pass
class InputNotPositive(Error):#raised when input is negative
   pass
class InputIs1(Error):#raised when input is 1
   pass

def userQuits():#function for when the user wants to quit
   print("-"*10)#separator for easy readability
   print("You Entered {} prime numbers".format(len(PrimeNumberList)))#tell user how many prime numbers they added using the lenght of the list
   print("Goodbye")
   exit()#end code


def CalculateIfPrime(UserValue):#function to decide if the user input is prime or not
   if UserValue > 1:#buffer if-statement
       # check for factors
       for iteration in range(2, UserValue):#iterate through possible factors
           if (UserValue % iteration) == 0:#if the modulous of the input and iteration is 0 then the number is not prime
               print("That is NOT prime")#tell user it is not prime
               break#end for loop and go back to main code
       else:#if no modulus equates to 0 then the number is prime
           print("That IS prime")#tell user that the number is prime
           PrimeNumberList.append(UserValue)#add the prime number to array for future use

while True:#main code
   try:#body of code that will run most of the time
       UserInputNumber = int(input("Enter a positive integer value, type 0 to quit: "))#get user input for the integer then convert to int
       if UserInputNumber < 0:#if input is negative
           raise InputNotPositive#tell user to input a positive integer
       elif UserInputNumber == 1:#if input is 1
           raise InputIs1#tell user it is a special case
       elif UserInputNumber == 0:#if input is 0 then go to the userQuits function
           userQuits()#goes to userQuits function
       else:#if none of the special cases return true then go to the calculation function
           CalculateIfPrime(int(UserInputNumber))#pass the input as a parameter
   except InputNotPositive:#see above
       print("Enter a POSITIVE integer!")#see above
   except InputIs1:#see above
       print("1 is neither prime nor composite!")#see above
   except ValueError:#see above
       print("That is not an integer!")#see above
