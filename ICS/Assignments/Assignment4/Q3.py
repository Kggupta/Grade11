#Define/write a function getBiggerNumber(x, y) that takes in two numbers as arguments and returns the bigger number.
#Write some main code that calls and tests this definition.

def getBiggerNumber(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    elif num1 == num2:
        return num1

inputnumber1 = int(input("Enter number: "))
inputnumber2 = int(input("Enter second number: "))
print("The larger number is: {} ".format(getBiggerNumber(inputnumber1,inputnumber2)))
