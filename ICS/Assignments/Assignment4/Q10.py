#Write a block of code (or procedure/function) that uses a TRY .. EXCEPT
#which will validate a person has entered a REAL number value (float) and has not made a mistake or typo by typing in a non-numerical value.
#Use casting to help you with this.

while True:
    try:
        userinput = float(input("Enter a number"))
        if (userinput).is_integer():
            print("This is a integer")
        else:
            print("This is a real")
    except ValueError:
        print("Not a number")
