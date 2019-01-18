#Ask the user for an integer. Output the number of digits in the integer. Then output the sum of the digits.

num = input("Enter a number")
print("{} has {} digits".format(num,len(num)))
i = 1
total = 0
for i in range(int(len(num))):
    total += int(num[i])
print(total)
