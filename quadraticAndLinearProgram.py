#Program to give a table of values for a linear or quadratic relationship in standard form
userAandMchoice = 0
userBchoice = 0
userCchoice = 0

class Error(Exception):
   pass
class InputNotValid(Error):
   pass



def LinearLogic():
   print("You chose linear")
   print("For the equation in the form y = mx + b")
   while True:
       try:
           userAandMchoice = float(input("Enter the 'm' value: "))
           break
       except ValueError:
           print("Not a valid input")
   while True:
       try:
           userBchoice = float(input("Enter the 'b' value: "))
           break
       except ValueError:
           print("Not a valid input")
   print("{:>10}{:>20}".format("X Value", "Y Value"))
   for iteration in range(-5, 6):
       print("{:>10}{:>20}".format(iteration, userAandMchoice * iteration + userBchoice))
   while True:
       try:
           userquit = input("Would you like to continue? (Y/N)")
           if userquit.upper() == "N":
               print("Goodbye")
               quit()
           if userquit.upper() == "Y":
               print("-"*25)
               break
           else:
               raise InputNotValid
       except InputNotValid:
           print("Not a valid input. Please enter 'Y' for yes and 'N' to quit")

def QuadraticLogic():
   print("You chose quadratic")
   print("For an equation in the form y = ax^2 + bx + c")
   while True:
       try:
           userAandMchoice = float(input("Enter the 'a' value: "))
           break
       except ValueError:
           print("Not a valid input")
   while True:
       try:
           userBchoice = float(input("Enter the 'b' value: "))
           break
       except ValueError:
           print("Not a valid input")
   while True:
       try:
           userCchoice = float(input("Enter the 'c' value: "))
           break
       except ValueError:
           print("Not a valid input")
   axisofsymetryoffset = (-(userBchoice/(2*userAandMchoice)))+5
   startvalue = axisofsymetryoffset - 10
   QuadraticList = []
   while startvalue <= axisofsymetryoffset:
       QuadraticList.append(startvalue)
       startvalue += 1
   print("{:>10}{:>20}".format("X Value", "Y Value"))
   for xValue in QuadraticList:
       print("{:>10}{:>20}".format(xValue, userAandMchoice*(xValue**2) + userBchoice*xValue + userCchoice))
   while True:
       try:
           userquit = input("Would you like to continue? (Y/N)")
           if userquit.upper() == "N":
               print("Goodbye")
               quit()
           if userquit.upper() == "Y":
               print("-"*25)
               break
           else:
               raise InputNotValid
       except InputNotValid:
           print("Not a valid input. Please enter 'Y' for yes and 'N' to quit")

while True:
   print("Which relationship would you like to graph?")
   print("1. Linear\n2. Quadratic")
   try:
       UserChoice = int(input("Choose 1 or 2"))
       if UserChoice < 1 or UserChoice > 2:
           raise InputNotValid
       elif UserChoice == 1:
           LinearLogic()
       elif UserChoice == 2:
           QuadraticLogic()
   except ValueError:
       print("That is not a valid input")
       print("-"*10)
   except InputNotValid:
       print("Only enter 1 or 2")
       print("-"*10)
