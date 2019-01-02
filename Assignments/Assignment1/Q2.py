#Write a program that asks for three numbers, and lists all three, and their sum

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
num3 = int(input("Enter a third integer."))
summ = num1+num2+num3
print('The sum of ', num1, ' and ', num2, ' and ', num3, ' is ', summ, '.', sep='')
