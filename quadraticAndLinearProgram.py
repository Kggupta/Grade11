#Program to give a table of values for a linear or quadratic relationship in standard form
userAandMchoice = 0 #variable to store the users input for slope
userBchoice = 0 #variable to store the users input for the b value
userCchoice = 0 #variable to store the usersers input for the c value in quadratic equation

class Error(Exception): #special error detection
   pass
class InputNotValid(Error): #an umbrella exception to dump all illegal values into one thing (save space)
   pass

def LinearLogic(): #function to calculate the linear relationship
   print("You chose linear")
   print("For the equation in the form y = mx + b")
   while True:#get the M slope of the equation, loop is to force the user to add a valid input before progressing
       try:
           userAandMchoice = float(input("Enter the 'm' value: "))#get the input
           break#if no problem comes up then continue to the next variable
       except ValueError:#if the user enters anything that is not a number it will tell them it wasnt a valid input, then prompt the user to enter their choice again
           print("Not a valid input")
   while True:#get the B value of the equation, loop is to force the user to add a valid input before progressing
       try:
           userBchoice = float(input("Enter the 'b' value: ")) #get the input for B
           break#if no problem comes up then continue to the next variable
       except ValueError:#if the user enters anything that isnt a number it will tell them it isnt a valid input and go back to prompting them to input it again
           print("Not a valid input")
   print("{:>10}{:>20}".format("X Value", "Y Value"))#setting up the table
   for iteration in range(-5, 6):#range to have 5 negative domain values and 5 positive
       print("{:>10}{:>20}".format(iteration, userAandMchoice * iteration + userBchoice))#loop that runs through all the iterations and outputs the values of the x and y
   while True:#loop to quit or keep entering relationships
       try:
           userquit = input("Would you like to continue? (Y/N)")#get user input
           if userquit.upper() == "N":#if user says he doesnt want to continue, say goodbye and end program
               print("Goodbye")
               quit()#end program
           if userquit.upper() == "Y":#if user says yes that he wants to continue, output a seperator '-' and end the loop to go back to the menu
               print("-"*25)#dash seperator
               break
           else:
               raise InputNotValid#any input except for 'y' and 'n' is invalid
       except InputNotValid:#if user didnt enter a valid number
           print("Not a valid input. Please enter 'Y' for yes and 'N' to quit")#telling user that their input was invalid

def QuadraticLogic():#function for the quadratic relationship
   print("You chose quadratic")
   print("For an equation in the form y = ax^2 + bx + c")
   while True:
       try:#get the A slope of the equation, loop is to force the user to add a valid input before progressing
           userAandMchoice = float(input("Enter the 'a' value: "))#get user input
           break#end infinite loop
       except ValueError:#if an invalid input was given (such as 'a' which isnt a number
           print("Not a valid input")
   while True:
       try:#get the B  of the equation, loop is to force the user to add a valid input before progressing
           userBchoice = float(input("Enter the 'b' value: "))#get user input
           break#end infinite loop if valid input was given
       except ValueError:#if an invalid input was given (such as 'a' which isnt a number
           print("Not a valid input")
   while True:
       try:#get the C of the equation, loop is to force the user to add a valid input before progressing
           userCchoice = float(input("Enter the 'c' value: "))#get user input
           break#end infinite loop
       except ValueError:#if an invalid input was given (such as 'a' which isnt a number
           print("Not a valid input")

   axisofsymetryoffset = (-(userBchoice/(2*userAandMchoice)))+5 #getting the axis of symetry so that we can have the table output 5 values on either side of it
   startvalue = axisofsymetryoffset - 10#the start of the table
   QuadraticList = []#list to store all the values from the start value to 5 x values aboce the AOS
   while startvalue <= axisofsymetryoffset:#getting the values of the table
       QuadraticList.append(startvalue)#appending the value to the list
       startvalue += 1#increment the start value
   print("{:>10}{:>20}".format("X Value", "Y Value"))#start the table format
   for xValue in QuadraticList:#for loop to output the values of the equation
       print("{:>10}{:>20}".format(xValue, userAandMchoice*(xValue**2) + userBchoice*xValue + userCchoice))#doing the math and outputting to the console
   while True:
       try:#ask if user wants to quit
           userquit = input("Would you like to continue? (Y/N)")
           if userquit.upper() == "N":#if user inputs 'n' then quit
               print("Goodbye")
               quit()#end program
           if userquit.upper() == "Y":#if user inputs 'y' then output a seperator and go back to the menu
               print("-"*25)#serperator
               break#break to go back to main code
           else:
               raise InputNotValid#all other inputs are invalid
       except InputNotValid:
           print("Not a valid input. Please enter 'Y' for yes and 'N' to quit")#telling user to put a valid input

while True:#main program that acts as a menu
   print("Which relationship would you like to graph?")
   print("1. Linear\n2. Quadratic")#asking user to choose a relationship to graph
   try:
       UserChoice = int(input("Choose 1 or 2"))#get user input
       if UserChoice < 1 or UserChoice > 2:#if user inputs a value above 2 or unser 1 then input isnt valid
           raise InputNotValid
       elif UserChoice == 1:#user chose linear
           LinearLogic()#go to the linear function
       elif UserChoice == 2:#user chose quadratic
           QuadraticLogic()#go to the quadratic function
   except ValueError:#exception that if the user puts in somethingt that isnt an integer then tell them its not valid
       print("That is not a valid input")
       print("-"*10)
   except InputNotValid:#if input is out of range then tell them they can only enter a one or two
       print("Only enter 1 or 2")
       print("-"*10)
