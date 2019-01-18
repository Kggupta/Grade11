#A series of marks (numbers) is to be entered and averaged.
#Before you enter the series you are to have the program ask a user how many marks they have to enter then create a loop to ask the user for a mark and accumulate a running total.
#Calculate the average once the loop is done.
#Test your program to see that it works for series of different lengths, say four marks or six marks.

marknumber = int(input("Enter the amount of marks you want to enter: "))
number = 1
total = 0
while number <= marknumber:
   mark = int(input("Enter you mark: "))
   total += mark
   number +=1
