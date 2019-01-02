#Write a program that asks for a radius value of a circle from a user, then calculates and displays the area of that circle. Make sure there are good descriptive instructions and comments for the user and the answer has only 1 decimal place.

import math
radius = float(input("Enter the radius of a circle in cm: "))#getting the user input of the raidus of a circle and converting it to a float so that in case the user inputs a decimal with the radius it wont crash
print("calculating the area of the circle with radius ", radius)#returning user input of radius to tell what is being used for the calculation
area = math.pi*radius**2 #calculting area of circle given the users input of radius
print("the area of a circle with radius {}cm has an area of: " .format(radius), end="")#telling the user what the area of the circle is. the end="" is meant for making the actual print of the area in teh same line as the main text. used math.pi for extra precision
print("{0:.1f}cm^2" .format(area))#printing the main area rounded to the tenth place
