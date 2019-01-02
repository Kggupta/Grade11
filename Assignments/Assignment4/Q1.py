#Print a table of about 10 x and y values for a linear relationship (you choose the equation, but x-values should go up by 1 and y values should be calculated) that has headings and is nicely formatted.
#The y-values should be rounded to 1 or 2 decimal places.
#Do NOT use spaces to format headings or the numbers, use the .format() method and/or {} with  numbers and symbols.

x = 0
print("{:>2}{:>10}".format("x","y"))
for i in range(0,10):
    y = 2*x+3
    print("{:>2}{:>10}".format(x,y))
    x += 1
