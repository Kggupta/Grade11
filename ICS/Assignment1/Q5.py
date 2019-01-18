#Write a program that asks for a person’s first, middle and last names then outputs their names in different formats.

firstname = input("What is your first name?").title() #defining the first name to whatever the user inputs with the .title function so that the first letter will be uppercase
middlename = input("What is your middle name?").title()#same as firstname var but for middle name
lastname = input("What is your last name?").title()#same as firstname var but for last name

print("I can list you as:")#the print that introduces the various possibilities
print("{}, {} {}".format(lastname,firstname,middlename))#print statement that will give the last name, first name, then middle name
print("{} {} {}".format(firstname,middlename,lastname))#print statement that will give the first name, middle name then last name
print("{} {}".format(firstname, lastname))#print statement that will give the first name then last name
print("{} {}. {}".format(firstname, middlename[0], lastname))#print statement that will give the first name, first LETTER of the middle name then the last name
