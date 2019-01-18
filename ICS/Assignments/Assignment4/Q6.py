#In Python, it is possible to pass a function as an argument to another function.
#Define/write a function useFunction(func, num) that takes in a function name and a number as arguments.
#The useFunction should produce the output shown in the examples given below.

def useFunction(func,num):
    print(func(num)**2)

def addOne(x):
    return x + 1

inputval = int(input("Enter a Number: "))
useFunction(addOne,inputval)
