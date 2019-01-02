#Write a program to generate 10 random integer numbers between:
#       5 and 25
#       x and y where x and y are integer inputs.

#5-25 range
import random
i = 1
while i <= 10:
    print(int(random.uniform(5,25)))
    i += 1

#X-Y inputed range
i = 1
low = int(input("What low range do you want?"))
high = int(input("What high range do you want?"))
while i <= 10:
    print(int(random.uniform(low,high)))
    i += 1
