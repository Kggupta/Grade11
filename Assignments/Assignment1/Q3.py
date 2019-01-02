#Using a similar format as #2 above (input, calculations, output), write a program that prompts the user for two integers, and then prints them out in a sentence with an integer division problem, using the floor and modulus division.

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
divisor = num1//num2
remainder = num1%num2
print("The quotient of {} and {} is {} with a remainder of {}".format(num1, num2, divisor, remainder))
