#Write a program that will produce a formatted table of values for a list generated from user input and each item’s square.
#Have ONE print statement that will output ALL values in line and right justified, using formatting techniques.

startval = int(input("Enter the starting value: "))
endval = int(input("Enter the end value: "))
increment = int(input("What is the increment: "))
newval = startval
print("{:>2}{:>20}".format("List value", "End value"))
while newval <= endval:
    print("{:>2}{:>20}".format(newval, newval ** 2))
    newval += increment
