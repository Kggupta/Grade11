#Write a program to output a table of values of the integers starting at 1 and their squares.
#Label the table at the top of the columns.

basicnum = 0
print("NUMBER       SQUARE")
for ranged in range(1,101):
    basicnum +=1
    print("{}           {}".format(basicnum, basicnum**2))
