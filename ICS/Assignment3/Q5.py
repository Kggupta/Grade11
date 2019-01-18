#Write a program to output a backwards count by 5s from 100 down to 5. \
#Modify it so that you count from 100 down to 50.
#Modify it again so that before you start the count you can input a number between 100 and 50 so that the program will stop when the count would be less than the number input.

endnum = int(input("What number do I stop at?"))
print("Stop when count less than", endnum)
max = 100
while max >= endnum:
    print(max)
    max -=5
