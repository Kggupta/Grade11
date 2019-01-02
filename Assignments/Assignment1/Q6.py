# Add single and multi line comments to your programs in any of #5-9 above. Add them on their own lines and/or at the end of some coded lines. Use blank lines in programs to separate blocks of code for readability.

num1 = int(input("Enter an integer: ")) #getting the input of the first number
num2 = int(input("Enter another integer: "))#getting the input of the second number

#Performing the math
divisor = num1//num2#calculating the divisor
remainder = num1%num2#calculating the remainder

#user return
print("The quotient of {} and {} is {} with a remainder of {}".format(num1, num2, divisor, remainder))
"""the last line will return the user input in the form of a scentence"""
