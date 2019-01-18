#Write a block of code that will create a list of numbers based on user input
#(signal to stop, or ask first how many numbers a person will enter), then output the list sorted as well as the sum of all the values in that list.

listed = [0,]
userinput = 1
i=0
total = 0
x=0
while userinput != "quit":
    userinput = input("Enter a number to add to list. enter quit to quit")
    if userinput != "quit":
        listed.append(int(userinput))
        i+=1
listed.remove(0)
print(listed)
while x < i:
    x+=1
    total += listed[x-1]

print(total)
